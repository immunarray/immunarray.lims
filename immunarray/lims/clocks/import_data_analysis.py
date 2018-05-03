import datetime
import logging
import os
from os.path import exists, join
from pprint import pformat
from shutil import rmtree
from time import time

import openpyxl
from AccessControl import Unauthorized
from Products.Five import BrowserView
from bika.lims.interfaces.limsroot import ILIMSRoot
from immunarray.lims.interfaces.aliquot import IAliquot
from immunarray.lims.interfaces.assayrequest import IAssayRequest
from immunarray.lims.interfaces.clinicalsample import IClinicalSample
from immunarray.lims.interfaces.ichip import IiChip
from immunarray.lims.interfaces.qcaliquot import IQCAliquot
from immunarray.lims.interfaces.sample import ISample
from immunarray.lims.interfaces.veracisrunbase import IVeracisRunBase
from plone.api.content import create, find, get_state, transition
from plone.protect.interfaces import IDisableCSRFProtection
from zExceptions import BadRequest
from zope.interface import alsoProvides

logger = logging.getLogger('ImportDataAnalysis')

all_cols = [chr(x) for x in range(65, 91)]  # A..Z


class SpreadsheetParseError(Exception):
    """Error getting required values from spreadsheet.  The parser
    is quite brittle, if anything is unexpected we will probably end up here.
    """


class RunInIncorrectState(Exception):
    """Test run is in the incorrect state.  Test run must be in state 'scanning'
    before results can be imported, and state changed to 'resulted' here.
    """


class ImportDataAnalysis(BrowserView):
    """This runner requires modification of the buildout. Example:

    ```buildout.cfg
        [buildout]
        environment-vars +=
            DATA_ANALYSIS_PATH /path/to/file/drop/folder
            DATA_ANALYSIS_AGE_THRESHOLD 120

        parts =
            import_data_analysis

        [import_data_analysis]
        <= client_base
        recipe = plone.recipe.zope2instance
        zeo-address = ${zeoserver:zeo-address}
        http-address = <some unused port number>
        zope-conf-additional =
            <clock-server>
               method /Plone/import_data_analysis
               period 60
               user admin
               password adminsecret
               host localhost
            </clock-server>
    ```

    The script can then be invoked with `bin/import_data_analysis start`,
    like any other zeo client, and it will execute the associated method
    every <period> minutes.

    Environment variables are:

    - DATA_ANALYSIS_PATH:
        The full path to the location in which folder containing data analysis
        outputs will be dropped.

    - DATA_ANALYSIS_AGE_THRESHOLD:
        Prevent action while data analysis folders are being uploaded.
        If the current time is not at least this many seconds greater than
        the most recent mtime of all files in the data analysis folder, no
        action is taken.
    
    """

    def __init__(self, context, request):
        alsoProvides(request, IDisableCSRFProtection)
        BrowserView.__init__(self, context, request)
        self.context = context
        self.request = request
        self.filepath = os.environ.get('DATA_ANALYSIS_PATH')
        self.threshold = int(
            os.environ.get('DATA_ANALYSIS_AGE_THRESHOLD', 12000))

    def __call__(self):
        if self.locked():
            return
        try:
            self.lock()
            map(self.process_results, self.get_pending_folders())
        finally:
            self.unlock()

    def locked(self):
        pid = str(os.getpid())
        fn = join(self.filepath, 'lock')
        if exists(fn) and pid in open(fn).read():
            return True
        else:
            self.unlock()
            return False

    def lock(self):
        fn = join(self.filepath, 'lock')
        open(fn, 'w').write(str(os.getpid()))

    def unlock(self):
        fn = join(self.filepath, 'lock')
        if exists(fn):
            os.unlink(fn)

    def get_pending_folders(self):
        """Return a list of full paths, who's file mtimes are outisde
        the safety threshold.
        """
        paths = []
        for fn in os.listdir(self.filepath):
            path = join(self.filepath, fn)
            if not exists(join(path, 'Out', 'Results', 'SLEkey_Results.xlsx')):
                continue
            # Check the modified time
            mtime = os.stat(path).st_mtime
            if time() < mtime + self.threshold:
                logger.info("%s: Newer than threshold." % path)
                continue
            paths.append(path)
        return paths

    def process_results(self, path):
        # import results and files from path
        log = self.process_results_xlsx(path)
        log += self.process_out_figures(path)
        log += self.process_raw_flipped(path)
        # transition run to 'resulted'
        run = self.get_run(path)
        run.import_log = log
        transition(run, 'result')
        # remove uploaded directory
        rmtree(path)

    def process_results_xlsx(self, path):
        """Take values from path/Out/Results/SLEkey_Results.xlsx, and write
        them to the database
        """
        run = self.get_run(path)

        # Get the first sheet
        filename = join(path, 'Out', 'Results', 'SLEkey_Results.xlsx')
        wb = openpyxl.load_workbook(filename)
        ws = wb.get_sheet_by_name('Sheet1')

        # header rows for blocks containg QC and Clinical aliquot/sample info
        qc_head_row = self.findnextSerial_Numberrow(ws, 1)
        clin_head_row = self.findnextSerial_Numberrow(ws, qc_head_row + 1)

        # get column letters of all qc headers that start with "ichip*"
        qc_ichip_cols = []
        passfail_col = None
        for col in all_cols:
            coord = "%s%s" % (col, qc_head_row)
            val = "%s" % ws[coord].value
            if val:
                if val.lower().startswith("fina"):
                    passfail_col = coord
                if val.lower().startswith("ichip"):
                    qc_ichip_cols.append(col)

        ichip_passfail_combos = []
        if passfail_col:
            for row in range(qc_head_row + 1, clin_head_row):
                passfail = "%s" % ws["%s%s" % (passfail_col, row)].value
                ichip_titles = []
                for col in qc_ichip_cols:
                    ichip_titles.append(ws["%s%s" % (col, row)].value)
                ichip_passfail_combos.append([ichip_titles, passfail])

        # for each plate
        for plate in run.plates:
            plate_ichips = []
            plate_ichiplot_titles = []

            # get all unique ichip lot numbers in a list
            for key, uid in plate.items():
                if key.startswith('ichip-id'):
                    ichip = find(UID=uid)[0].getObject()
                    plate_ichips.append(ichip)
                    ichiplot_title = ichip.title.upper().split('-')[0]
                    if ichiplot_title not in plate_ichiplot_titles:
                        plate_ichiplot_titles.append(ichiplot_title)
            for combo in ichip_passfail_combos:
                if sorted(plate_ichiplot_titles) == sorted(combo[0]):
                    for ichip in plate_ichips:
                        transition(ichip, 'qc_' + combo[1].lower())

            # 'consume' qc aliquots.
            for uid in plate.values():
                brains = find(object_provides=IQCAliquot.__identifier__,
                              UID=uid, review_state='in_process')
                if brains:
                    transition(brains[0].getObject(), 'done')

        # find the column at which the following headers are located:
        cols = {'Sample_ID': '',
                'SLE_key_Score': '',
                'SLE_key_Classification': '',
                'Assay_QC_Status': ''}
        if not all(cols):
            msg = "One of the column headers can't be located:" % pformat(cols)
            raise SpreadsheetParseError(msg)
        for col in all_cols:
            coord = "%s%s" % (col, clin_head_row)
            value = ws[coord].value
            if value in cols:
                cols[value] = col

        # get values from each row and colum into aliquot_results. results is:
        # {sample_id: [SLE_key_Score,
        #              SLE_key_Classification,
        #              Assay_QC_Status],}
        aliquot_results = {}
        first_empty = self.get_first_empty_row(ws, clin_head_row)
        for row in range(clin_head_row + 1, first_empty):
            sample_id = ws["%s%s" % (cols['Sample_ID'], row)].value
            score = ws["%s%s" % (cols['SLE_key_Score'], row)].value
            classif = ws["%s%s" % (cols['SLE_key_Classification'], row)].value
            status = ws["%s%s" % (cols['Assay_QC_Status'], row)].value
            aliquot_results[sample_id] = {
                'SLE_key_Score': score,
                'SLE_key_Classification': "%s" % classif,
                'Assay_QC_Status': "%s" % status
            }

        log = []

        _used_uids = []
        for plate in run.plates:
            for uid in plate.values():
                if uid in _used_uids:
                    continue
                _used_uids.append(uid)
                brains = find(UID=uid)
                if not brains:
                    continue
                aliquot = brains[0].getObject()
                if not IAliquot.providedBy(aliquot):
                    continue
                sample = self.get_sample_from_aliquot(aliquot)
                if IClinicalSample.providedBy(sample):
                    if sample.title not in aliquot_results:
                        msg = "Sample '%s' not in spreadsheet results: %s" % \
                              (sample.title, pformat(aliquot_results))
                        raise RuntimeError(msg)
                    result = aliquot_results[sample.title]
                    ar = self.get_ar_from_sample(sample, run.assay_name)
                    state = result['Assay_QC_Status'].lower()
                    ar.aliquot_evaluated = aliquot.title
                    ar.date_resulted = self.get_date(ws)
                    # assayrequest is associated with multiple aliquots,
                    # so we only transition if the AR's state is expected.
                    if get_state(ar) == 'in_process':
                        transition(ar, 'qc_' + state)
                aliquot.numeric_result = result['SLE_key_Score']
                aliquot.text_result = result['SLE_key_Classification']
                log.append("Sample: %s, Aliquot: %s, Results: %s, %s" % (
                    sample.title,
                    aliquot.title,
                    result['SLE_key_Score'],
                    result['SLE_key_Classification'],
                ))
        return log

    def process_out_figures(self, path):
        """Store images in samples
        """
        figpath = join(path, 'Out', 'Figures')
        log = []
        for fn in os.listdir(figpath):
            if 'png' not in fn:
                continue
            sample_id = fn.split('_')[0]
            brains = find(object_provides=ISample.__identifier__, id=sample_id)
            if not brains:
                msg = "%s/%s: Can't find sample '%s'" % (figpath, fn, sample_id)
                raise RuntimeError(msg)
            sample = brains[0].getObject()
            try:
                img = create(container=sample, type='Image', id=fn, title=fn)
            except BadRequest as e:
                msg = "Run import has already been performed! (%s)" % e.message
                raise BadRequest(msg)
            except Unauthorized:
                msg = "Failed to create %s in sample %s" % (fn, sample.title)
                raise Unauthorized(msg)
            log.append("Added image to sample: " % img)
            return log

    def process_raw_flipped(self, path):
        """Store flipped images in ichips
        """
        flpath = join(path, 'Raw', 'Flipped')
        log = []
        for fn in os.listdir(flpath):
            if 'jpg' not in fn:
                continue
            splits = fn.lower().split('_')
            ichip_id = splits[1].replace('.', '-') + "_%03d" % int(splits[2])
            brains = find(object_provides=IiChip.__identifier__, id=ichip_id)
            if not brains:
                msg = "%s/%s: Can't find ichip '%s'" % (flpath, fn, ichip_id)
                raise RuntimeError(msg)
            ichip = brains[0].getObject()
            try:
                img = create(container=ichip, type='Image', id=fn, title=fn)
            except BadRequest as e:
                msg = "Run import has already been performed! (%s)" % e.message
                raise BadRequest(msg)
            except Unauthorized:
                msg = "Failed to create %s in ichip %s" % (fn, ichip.title)
                raise Unauthorized(msg)
            log.append("Added image to sample: " % img)
            return log

    def get_run(self, path):
        run_nr = self.get_run_nr(path)
        # get the run nr so we can loop the plates
        brains = find(object_provides=IVeracisRunBase.__identifier__,
                      run_number=run_nr)
        if not brains:
            msg = "No test run found with run_number=%s." % run_nr
            raise RuntimeError(msg)
        run = brains[0].getObject()

        # verify that run is in correct state for import.
        state = get_state(run)
        if state != 'scanning':
            msg = "Test run %s is in state '%s'.  Expected state: 'scanning'" \
                  % (run.title, state)
            raise RunInIncorrectState(msg)

        return run

    def get_run_nr(self, path):
        try:
            csv = [i for i in os.listdir(path) if i.lower().endswith('.csv')][0]
        except Exception as e:
            msg = "Cannot discover run for %s: (%s)" % (path, e.message)
            raise RuntimeError(msg)
        run_nr = int(csv.split('.')[0])
        return run_nr

    def get_sample_from_aliquot(self, aliquot):
        parent = aliquot.aq_parent
        while not (ISample.providedBy(parent)):
            parent = parent.aq_parent
            if ILIMSRoot.providedBy(parent):
                msg = "Cannot find ISample parent of Aliquot: %s" % aliquot
                raise RuntimeError(msg)
        return parent

    def get_ar_from_sample(self, sample, assay_name):
        for y in sample.objectValues():
            if IAssayRequest.providedBy(y) and y.assay_name == assay_name:
                return y

    def get_first_empty_row(self, ws, start):
        for y in range(start, 999):
            if not ws['A%s' % y].value:
                return y

    def findnextSerial_Numberrow(self, ws, start_row):
        """Dig up the next row who's first column contains 'Serial_Number'
        """
        for i in range(start_row, 999):
            value = "%s" % ws['A%s' % i].value
            if value.lower() == 'serial_number':
                return i
        msg = "Can't find cell 'serial_number' in range(A%s,A999)" % start_row
        raise SpreadsheetParseError(msg)

    def get_date(self, ws):
        for y in range(1, 999):
            headervalue = "%s" % ws['A%s' % y].value
            if headervalue.lower() == 'analysis date':
                xy = 'C%s' % y
                value = ws[xy].value
                if isinstance(value, datetime.datetime):
                    return value
                msg = "Check that cell has valid date and Date format: %s" % xy
                raise SpreadsheetParseError(msg)
        msg = "Can't find cell 'analysis date' in range(A1,A999)"
        raise SpreadsheetParseError(msg)

    def get_qc_aliquots_from_run(self, run):
        aliquots = []
        plates = run.plates
        for plate in plates:
            for uid in plate.values():
                brains = find(object_provides=IQCAliquot.__identifier__,
                              UID=uid)
                if brains:
                    aliquots.append(brains[0].getObject())
        return aliquots
