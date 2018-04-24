import logging
import os
from os.path import exists, join
from pprint import pformat
from shutil import rmtree
from time import strptime, time

import datetime
import openpyxl
from Products.Five import BrowserView
from bika.lims.interfaces.limsroot import ILIMSRoot
from immunarray.lims.interfaces.assayrequest import IAssayRequest
from immunarray.lims.interfaces.clinicalsample import IClinicalSample
from immunarray.lims.interfaces.qcaliquot import IQCAliquot
from immunarray.lims.interfaces.sample import ISample
from immunarray.lims.interfaces.veracisrunbase import IVeracisRunBase
from plone.api.content import find, transition

logger = logging.getLogger('ImportDataAnalysis')

all_cols = [chr(x) for x in range(65, 91)]  # A..Z


class SpreadsheetParseError(Exception):
    """Error getting required values from spreadsheet.  The parser
    is quite brittle, if anything is unexpected we will probably end up here.
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
        for x in os.listdir(self.filepath):
            path = join(self.filepath, x)
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
        self.process_results_xlsx(path)
        self.process_out_figures(path)
        self.process_raw_flipped(path)
        # If we made it this far without raising an exception,
        # then everything's fine and we can remove the folder.
        rmtree(path)

    def process_results_xlsx(self, path):
        """Take values from path/Out/Results/SLEkey_Results.xlsx, and write
        them to the database
        """
        # Get the first sheet
        filename = join(path, 'Out', 'Results', 'SLEkey_Results.xlsx')
        wb = openpyxl.load_workbook(filename)
        ws = wb.get_sheet_by_name('Sheet1')

        # header rows for blocks containg QC and Clinical aliquot/sample info
        qc_head_row = self.findnextSerial_Numberrow(ws, 1)
        clin_head_row = self.findnextSerial_Numberrow(ws, qc_head_row + 1)

        run = self.get_run(qc_head_row, ws)

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
            # @formatter:off
            aliquot_results[sample_id] = {
                'SLE_key_Score': ws["%s%s" % (cols['SLE_key_Score'], row)].value,
                'SLE_key_Classification': "%s" % ws["%s%s" % (cols['SLE_key_Classification'], row)].value,
                'Assay_QC_Status': "%s" % ws["%s%s" % (cols['Assay_QC_Status'], row)].value
            }
            # @formatter:on

        _used_uids = []
        for plate in run.plates:
            for uid in plate.values():
                if uid in _used_uids:
                    continue
                _used_uids.append(uid)
                brains = find(UID=uid)
                if brains:
                    aliquot = brains[0].getObject()
                    sample = self.get_sample_from_aliquot(aliquot)
                    if IClinicalSample.providedBy(sample):
                        if sample.title not in aliquot_results:
                            msg = "Sample '%s' not in aliquot results: %s" % \
                                  (sample.title, pformat(aliquot_results))
                            raise RuntimeError(msg)
                        result = aliquot_results[sample.title]
                        ar = self.get_ar_from_sample(sample, run.assay_name)
                        state = result['Assay_QC_Status'].lower()
                        ar.aliquot_evaluated = aliquot.title
                        ar.date_resulted = self.get_date(ws)
                        import pdb
                        pdb.set_trace()
                        pass
                        transition(ar, 'qc_' + state)
                    numeric_result = result['SLE_key_Score']
                    aliquot.numeric_result = numeric_result
                    text_result = result['SLE_key_Classification']
                    aliquot.text_result = text_result

    def get_run(self, qc_head_row, ws):
        # get the run nr so we can loop the plates
        for col in all_cols:
            if 'session' in ws["%s%s" % (col, qc_head_row)].value.lower():
                run_number = int(ws["%s%s" % (col, qc_head_row + 1)].value)
                break
        else:
            msg = "Can't find cell 'session' in range(%s%s,%s%s)" % \
                  (min(all_cols), qc_head_row, max(all_cols), qc_head_row)
            raise SpreadsheetParseError(msg)
        brains = find(object_provides=IVeracisRunBase.__identifier__,
                      run_number=run_number)
        if not brains:
            msg = "No test run found with run_number=%s." % run_number
            raise RuntimeError(msg)
        run = brains[0].getObject()
        return run

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

    def process_out_figures(self, path):
        """Store and log.
        """

    def process_raw_flipped(self, path):
        """Store and log.
        """
