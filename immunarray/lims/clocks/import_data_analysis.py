import logging
import os
from os.path import exists, join
from time import time

import openpyxl
from Products.Five import BrowserView
from immunarray.lims.interfaces.qcaliquot import IQCAliquot
from immunarray.lims.interfaces.veracisrunbase import IVeracisRunBase
from plone.api.content import find

logger = logging.getLogger('ImportDataAnalysis')


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
        self.threshold = int(os.environ.get('DATA_ANALYSIS_AGE_THRESHOLD', 120))

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
        fn = join(self.filepath, 'lock')
        return exists(fn)

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
        filename = join(path, 'Out', 'Results', 'SLEkey_Results.xlsx')
        wb = openpyxl.load_workbook(filename)
        ws = wb.get_sheet_by_name('Sheet1')

        # Collect QC info
        run_number = ws['I13'].value
        qc_final_status = ws['F13'].value

        # Transition QC Aliquots
        test_run = self.get_test_run(run_number)
        aliquots = self.get_qc_aliquots_from_run(test_run)
        # for aliquot in aliquots:
        #     transition(aliquot, qc_final_status.lower())

        # Edit and transition clinical samples.
        # info is in row 19+:
        #     - sample ID is in B
        #     - qc state is in F
        #     - numeric_result is in C
        row = 19
        while 1:

            SLE_key_Score = ws['C%s' % row].value
            SLE_key_Classification = ws['E%s' % row].value
            if not all([SLE_key_Score, SLE_key_Classification]):
                break

            sample_id = ws['B%s' % row].value
            assay_qc_status = ws['F%s' % row].value

            from commands import getoutput as go
            go("/usr/bin/play /home/rockfruit/pdb.wav")
            import pdb
            pdb.set_trace()
            pass

            # # Add results
            # aliquot.numeric_result = SLE_key_Score
            # aliquot.text_result = SLE_key_Classification
            # # Transition aliquot
            # transition(aliquot, qc_final_status.lower())

            row += 1

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
