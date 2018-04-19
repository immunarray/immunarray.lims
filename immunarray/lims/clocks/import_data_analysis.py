import logging
import os
from os.path import exists, join
from time import strptime, time

import openpyxl
from Products.Five import BrowserView
from immunarray.lims.interfaces.assayrequest import IAssayRequest
from immunarray.lims.interfaces.clinicalsample import IClinicalSample
from immunarray.lims.interfaces.qcaliquot import IQCAliquot
from immunarray.lims.interfaces.veracisrunbase import IVeracisRunBase
from plone.api.content import find, transition

logger = logging.getLogger('ImportDataAnalysis')

all_cols = [chr(x) for x in range(65, 91)]  # A..Z


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
        import pdb;pdb.set_trace()
        BrowserView.__init__(self, context, request)
        self.context = context
        self.request = request
        self.filepath = os.environ.get('DATA_ANALYSIS_PATH')
        self.threshold = int(os.environ.get('DATA_ANALYSIS_AGE_THRESHOLD', 12000))

    def __call__(self):
        if self.locked():
            return
        try:
            self.lock()
            paths = self.get_pending_folders()
            for path in paths:
                self.process_results_xlsx(path)
                self.process_out_figures(path)
                self.process_raw_flipped(path)
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
        import pdb;pdb.set_trace()
        paths = []
        for fname in os.listdir(self.filepath):
            if fname == 'lock':
                continue
            path = join(self.filepath, fname)
            # Check the modified time of all files inside this path:
            for root, dirs, files in os.walk(path):
                if files:
                    mtimes = [os.stat(join(root, f)).st_mtime for f in files]
                    if time() < max(mtimes) + self.threshold:
                        logger.info("%s: Newer than threshold." % path)
                        break
            else:
                paths.append(path)
        return paths

    def process_results_xlsx(self, path):
        """Take values from path/Out/Results/SLEkey_Results.xlsx, and write
        them to the database
        """
        # Get the first sheet
        import pdb;pdb.set_trace()
        filename = join(path, 'Out', 'Results', 'SLEkey_Results.xlsx')
        wb = openpyxl.load_workbook(filename)
        ws = wb.get_sheet_by_name('Sheet1')

        # header rows for blocks containg QC and Clinical aliquot/sample info
        qc_head_row = self.findnextSerial_Numberrow(ws, 1)
        clin_head_row = self.findnextSerial_Numberrow(ws, qc_head_row)

        # get the run nr so we can loop the plates
        for col in all_cols:
            if 'session' in ws["%s%s" % (col, qc_head_row)].value.lower():
                run_number = int(ws["%s%s" % (col, qc_head_row + 1)].value)
        # noinspection PyUnboundLocalVariable
        run = self.get_test_run(run_number)

        # get column letters of all qc headers that start with "ichip*"
        qc_ichip_cols = []
        for col in all_cols:
            coord = "%s%s" % (col, qc_head_row)
            if ws[coord].value.lower().startswith("fina"):
                passfail_col = coord
            if ws[coord].value.lower().startswith("ichip"):
                qc_ichip_cols.append(col)

        ichip_passfail_combos = []
        for row in range(qc_head_row + 1, clin_head_row):
            # noinspection PyUnboundLocalVariable
            passfail = ws["%s%s" % (passfail_col, row)].value
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
        for col in all_cols:
            coord = "%s%s" % (col, clin_head_row)
            value = ws[coord].value
            if value in cols:
                cols[value] = col

        # get values from each row and colum into aliquot_results.
        # aliquot results is:
        # key=sample_id: [SLE_key_Score,
        #                 SLE_key_Classification,
        #                 Assay_QC_Status]
        aliquot_results = {}
        first_empty = self.get_first_empty_row(ws, clin_head_row)
        for row in range(clin_head_row + 1, first_empty):
            sample_id = ws["%s%s" % (cols['Sample_ID'], row)].value
            aliquot_results[sample_id] = {
                'SLE_key_Score':
                    ws["%s%s" % (cols['SLE_key_Score'], row)].value,
                'SLE_key_Classification':
                    ws["%s%s" % (cols['SLE_key_Classification'], row)].value,
                'Assay_QC_Status':
                    ws["%s%s" % (cols['Assay_QC_Status'], row)].value
            }

        _used_uids = []
        for plate in run.plates:
            for uid in plate.values():
                if uid in _used_uids:
                    continue
                _used_uids.append(uid)
                brains = find(UID=uid)
                if brains:
                    aliquot = brains[0].getObject()
                    sample = aliquot.aq_parent
                    if IClinicalSample.providedBy(sample):
                        if sample.title not in aliquot_results:
                            raise Exception("What do.")
                        ar = self.get_ar_from_sample(sample, run.assay_name)
                        state = aliquot_results['Assay_QC_Status'].lower()
                        ar.aliquot_evaluated = aliquot.title
                        ar.date_resulted = self.get_date(ws)
                        transition(ar, 'qc_' + state)
                    numeric_result = aliquot_results['SLE_key_Score']
                    aliquot.numeric_result = numeric_result
                    text_result = aliquot_results['SLE_key_Classification']
                    aliquot.text_result = text_result

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
            if ws['A%s' % i].value.lower() == 'serial_number':
                return i

    def get_date(self, ws):
        for y in range(1, 999):
            if ws['A%s' % y].value.lower() == 'analysis date':
                val = ws['B%s' % y].value
                return strptime(val, '%d-%b-%y')

    def get_test_run(self, run_number):
        """get test run object
        """
        brains = find(IVeracisRunBase.__identifier__, run_number=run_number)
        if not brains:
            msg = "No test run found with run_number=%s." % run_number
            raise RuntimeError(msg)
        return brains[0].getObject()

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
        """
        """

    def process_raw_flipped(self, path):
        """
        """
