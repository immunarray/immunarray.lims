# -*- coding: utf-8 -*-
import csv
from cStringIO import StringIO

from Products.Five import BrowserView
from immunarray.lims import normalize
from immunarray.lims.browser.analysisrequest.commercial_run import \
    InvalidSample, MissingIChipForSlide
from immunarray.lims.interfaces.clinicalaliquot import IClinicalAliquot
from immunarray.lims.interfaces.sample import ISample
from plone.api.content import find


class DownloadCSV(BrowserView):
    def __init__(self, context, request):
        BrowserView.__init__(self, context, request)
        self.context = context
        self.request = request

    def __call__(self):
        fieldnames = [
            'iChipLot', 'Slide_ID', 'Well_ID', 'Plate', 'TestSession',
            'SampleID', 'Analyze', 'Run_Number', 'SampleClass',
            'Aliqout_ID']

        io = StringIO()
        writer = csv.DictWriter(io, fieldnames=fieldnames)
        writer.writerow(dict(zip(fieldnames, fieldnames)))
        for plate_nr, plate in enumerate(self.context.plates):
            plate_nr += 1
            for chip_nr in range(1, 5):

                # get chip for this slide
                uid = plate['chip-id-%s' % chip_nr]
                if not uid:
                    raise MissingIChipForSlide(
                        "plate %s, slide %s" % (plate_nr, chip_nr))
                chip = find(UID=uid)[0].getObject()

                for well_nr in range(1, 9):
                    uid = plate['chip-%s_well-%s' % (chip_nr, well_nr)]
                    if uid:
                        aliquot = find(UID=uid)[0].getObject()
                        sample = self.get_parent_sample_from_aliquot(aliquot)
                        if IClinicalAliquot.providedBy(aliquot):
                            SampleClass = '1'
                            Aliquot_ID = aliquot.title
                            SampleID = '-'.join(
                                aliquot.title.split('-')[:2])
                            Analyze = '1'
                        elif self.is_hqc(sample):
                            SampleClass = '3'
                            Aliquot_ID = aliquot.title
                            SampleID = sample.source_id_one
                            Analyze = '1'
                        elif self.is_lqc(sample):
                            SampleClass = '5'
                            Aliquot_ID = aliquot.title
                            SampleID = sample.source_id_one
                            Analyze = '1'
                        else:
                            raise InvalidSample(
                                "Aliquot %s" % aliquot.title)
                    else:
                        SampleClass = '1'
                        Aliquot_ID = 'Blank'
                        SampleID = 'Blank'
                        Analyze = '0'

                    # noinspection PyUnboundLocalVariable
                    writer.writerow({
                        'iChipLot': chip.title.split("_")[0],
                        'Slide_ID': chip.title.split("_")[1],
                        'Well_ID': str(well_nr),
                        'Plate': str(plate_nr),
                        'TestSession': '1',
                        'SampleID': SampleID,
                        'Analyze': Analyze,
                        'Run_Number': self.context.run_number,
                        'SampleClass': SampleClass,
                        'Aliqout_ID': Aliquot_ID,
                    })

        fn = self.context.assay_name + "-" + self.context.run_number
        fn = normalize(fn) + ".csv"
        setheader = self.request.RESPONSE.setHeader
        setheader('Content-Type', 'text/csv')
        setheader("Content-Disposition", 'attachment;filename="%s"' % fn)
        self.request.RESPONSE.write(io.getvalue())

    def get_parent_sample_from_aliquot(self, aliquot):
        parent = aliquot.aq_parent
        while not ISample.providedBy(parent):
            parent = parent.aq_parent
        return parent

    def is_hqc(self, sample):
        assay = find(UID=self.context.assay_uid)[0].getObject()
        hqc_id = assay.qc_high_choice
        return sample.id.split('-')[0] == hqc_id

    def is_lqc(self, sample):
        assay = find(UID=self.context.assay_uid)[0].getObject()
        lqc_id = assay.qc_low_choice
        return sample.id.split('-')[0] == lqc_id
