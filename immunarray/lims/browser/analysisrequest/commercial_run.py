# -*- coding: utf-8 -*-
import json
from operator import itemgetter

from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.resources import add_resource_on_request
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from immunarray.lims.vocabularies.ichipassay import IChipAssayListVocabulary
from plone.api.content import get_state, find
from plone.i18n.normalizer.interfaces import IIDNormalizer
from zope.component import queryUtility


class NoIchipLotsFound(Exception):
    pass


class NotEnoughUniqueIChipLots(Exception):
    pass


class QCSampleNotFound(Exception):
    pass

class QCAliquotNotFound(Exception):
    pass


class NoWorkingAliquotsFound(Exception):
    pass


class AddCommercialEightFrameTestRunView(BrowserView):
    template = ViewPageTemplateFile(
        "templates/aliquot_testing/SLE-key_v_2_0_commercial.pt")

    def __init__(self, context, request):
        BrowserView.__init__(self, context, request)
        self.context = context
        self.request = request
        self.errors = []

    def __call__(self):
        add_resource_on_request(self.request, "static.js.test_run.js")
        request = self.request

        if "assaySeleced" in request.form:
            # gives me the assay value from the ctest form
            assay = request.form.get("assaySeleced")
            if assay == 'None':
                return self.template()  # setup for "custom"

            assay_parameters = self.getInfoAboutSelectedAssay(assay)
            if assay_parameters == 0:
                return json.dumps({"TestRun": "No Assay Paramater Found"})

            if assay_parameters['desired_use'] == 'Commercial':
                plates = self.makeTestPlan(assay, assay_parameters)
                return json.dumps({"TestRun": plates})

            # if assay_parameters['desired_use'] == 'Development':
            #     samples_to_get = 'RandDSample'
            #     # make a development run
            #     development_samples = {}
            #     ichips_for_session = {}
            #     solutions_for_session = {}

            if assay == 'Custom':
                all_samples_in_lims = {}
                ichips_for_session = {}
                solutions_for_session = {}
                # button push
                # commercial_samples_finial = []
                # ichips_for_session_finial = []

        return self.template()

    def getInfoAboutSelectedAssay(self, assay):
        """Use end user selection to pull needed number of working aliquots 
        for assay
        """
        ichipassays = {}
        variables_to_get = [
            'creation_date',
            'creators',
            'description',
            'desired_working_aliquot_volume',
            'framecount',
            'id',
            'max_number_of_plates_per_test_run',
            'minimum_working_aliquot_volume',
            'modification_date',
            'number_of_high_value_controls',
            'number_of_low_value_controls',
            'number_of_same_lot_replication_needed_for_samples',
            'number_of_unique_ichips_lots_needed',
            'number_of_working_aliquots_needed',
            'portal_type',
            'qc_high_choice',
            'qc_low_choice',
            'desired_use',
            'sample_qc_dilution_factor',
            'sample_qc_dilution_material',
            'title',
        ]
        normalize = queryUtility(IIDNormalizer).normalize
        brains = find(portal_type='iChipAssay', Title=assay)
        if brains:
            assay_obj = brains[0].getObject()
            params = {t: assay_obj._get_request_var_or_attr(t, '')
                      for t in variables_to_get}
            return params
        else:
            return 0

    def maxNumberOfSamplesToRun(self, assay_parameters):
        """take the assay parameters and determine the max number of samples
        that can be tested in a single run
        """
        max_plates = assay_parameters['max_number_of_plates_per_test_run']
        hqc = assay_parameters['number_of_high_value_controls']
        lqc = assay_parameters['number_of_low_value_controls']
        number_same_lot = assay_parameters[
            'number_of_same_lot_replication_needed_for_samples']
        number_unique_lot = assay_parameters[
            'number_of_unique_ichips_lots_needed']
        frame_count = assay_parameters['framecount']
        # update type to be frame type (int)
        wells_needed_per_sample = number_same_lot * number_unique_lot
        max_wells = max_plates * frame_count
        testing_wells_for_hqc = wells_needed_per_sample * hqc
        testing_wells_for_lqc = wells_needed_per_sample * lqc
        sample_wells = max_wells - (
            testing_wells_for_hqc + testing_wells_for_lqc)
        max_samples_to_test = sample_wells - wells_needed_per_sample
        return max_samples_to_test

    def get_assay_request_from_sample(self, sample, assay_name):
        """Return
        """
        wf = getToolByName(sample, 'portal_workflow')
        for obj in sample.getObjectValues():
            if obj.portal_type == 'AssayRequest' \
                    and obj.title == assay_name \
                    and get_state(obj) in ['re_run', 'to_be_tested']:
                return obj

    def queryClinicalSamples(self, assay, max_nr_samples):
        """Get all the samples that are review_state='received', and which
        contain an "AssayRequest" who's title matches the assay_name, and who
        have a review_state of (re_run or to_be_tested).
        """
        sample_data = []

        for testable_state in ['re_run', 'to_be_tested']:
            # this does get Clinical Samples keep reading jp
            brains = find(portal_type="AssayRequest",
                          Title=assay,
                          review_state=testable_state)
            tmp = []
            for brain in brains:
                assay_request = brain.getObject()
                sample = assay_request.aq_parent
                tmp.append({'uid': sample.UID(),
                            'draw_date': sample.collection_date,
                            'test_status': get_state(assay_request),
                            'sample': sample})
            tmp = sorted(tmp, key=itemgetter('draw_date'))
            sample_data.extend(tmp)

        return sample_data[:max_nr_samples]

    def queryClinicalWorkingAliquots(self, clinical_samples, assay_parameters):
        """Query to get QC and Clinical working aliquots to test with.
        """
        aliquot_objects_for_testing = []
        # loop over all the samples coming into search
        for sample_dict in clinical_samples:
            # object passed in from full_set
            parent = sample_dict['sample']  # parent is sample object
            aliquots = self.collectAliquots(parent, Type='Clinical Aliquot (Working)')
            for c in aliquots:
                vol = assay_parameters['desired_working_aliquot_volume']
                if c.remaining_volume >= vol:
                    aliquot_objects_for_testing.append(c)
                    break
        if not aliquot_objects_for_testing:
            raise NoWorkingAliquotsFound
        return aliquot_objects_for_testing


    # noinspection PyPep8Naming
    def collectAliquots(self, sample_object, **kwargs):
        """Get in array of objects to see if they are the last in the chain
        and return a list of objects back.  Check if each is a working aliquot
        that meets the needs of the assay

        Type is the value of the index called 'Type'.  It's set (for aliquots)
        in the adapters/indexers.py.
        """
        path = '/'.join(sample_object.getPhysicalPath())
        brains = find(path={'query': path, 'depth': -1}, sort_on='id', **kwargs)
        items = [b.getObject() for b in brains]
        return items



    def iChipAssayList(self):
        vocab_keys = IChipAssayListVocabulary.__call__(self).by_value.keys()
        return vocab_keys

    def get_vocab_keys(self, vocab):
        vocab_keys = vocab.__call__(self).by_value.keys()
        return vocab_keys

    def makeTestPlan(self, assay, assay_parameters):
        """use ordered [ichiplot, [ichips]], assay parameters{},
        [working aliquots] to build test plan

        XXX

        # asdf = create(ichiplot)
        # asdf1 = create(ichiplot)
        # asdf2 = create(clinicals)
        # asdf3 = create(qc hi)
        # asdf4 = create(qc lo)
        # asdf5 = create(assay)
        # makeTestPlan(assay_params, ich, max)
        [[id_of_x, [y,z,yy,zz], [...], ]]


        """
        slide_per_plate = 4  # constant that needs to be defined

        max_plates = assay_parameters['max_number_of_plates_per_test_run']
        number_same_lot = assay_parameters[
            'number_of_same_lot_replication_needed_for_samples']
        number_unique_lot = assay_parameters[
            'number_of_unique_ichips_lots_needed']
        frame_count = assay_parameters['framecount']
        min_volume_per_sample = assay_parameters[
            'minimum_working_aliquot_volume']
        frames = assay_parameters['framecount']

        max_nr_samples = self.maxNumberOfSamplesToRun(assay_parameters)
        clinical_samples = self.queryClinicalSamples(assay, max_nr_samples)
        sample_count = len(clinical_samples)
        ichips_for_assay = self.getiChipsForTesting(assay, sample_count, frames)
        working_aliquots = self.queryClinicalWorkingAliquots(clinical_samples, assay_parameters)

        number_of_ichip_lots_available = len(ichips_for_assay)
        # [[<ichiplot>,[<ichip>,<ichip>]],[<ichiplot>,[<ichip>,<ichip>]]]

        if not number_of_ichip_lots_available >= number_unique_lot:
            raise NotEnoughUniqueIChipLots

        plate_count = 0
        _used_ichiplots = []
        _used_ichips = []
        result = []  # thing that will be sent back each entry is a "plate"

        # condition that lets me know to keep making plates both parts must
        # be true
        while plate_count <= max_plates and len(working_aliquots) > 0:
            # add QC to working_aliquots is no ichiplots have been used
            if not _used_ichiplots:
                qc_list = self.getQCAliquots(assay_parameters)
                for qc in qc_list:
                    working_aliquots.insert(0, qc)
            active_lots = []
            required_ichips_for_testing = []
            for xx in ichips_for_assay:
                ichiplot, ichips = xx
                # That tells me if we have used this lot before
                if ichiplot.title.split(".")[0] not in (
                        active_lots[j][0].title.split(".")[0] for j in
                        range(len(active_lots))):
                    # faulty because we don't update the ichips,
                    # if true once it will always be true!
                    if len(ichips) >= number_same_lot:
                        if ichiplot not in _used_ichiplots:
                            active_lots.append(xx)
                            _used_ichiplots.append(ichiplot)
                        elif ichiplot in _used_ichiplots:
                            running_chip_count_in_lot = 0
                            for chip in _used_ichips:
                                if chip.getParentNode() == ichiplot:
                                    running_chip_count_in_lot += 1  # count
                                    # of how many ichips have been used from
                                    # current lot
                            if len(
                                    ichips) - running_chip_count_in_lot >= number_same_lot:
                                active_lots.append(xx)
                # Need to account for how many ichips are left in the lot and
                # if len(list_of_ichip_objects)-len(_used_ichips from that lot)
                #  > number_same_lot
                if len(active_lots) == number_unique_lot:
                    # have the ichiplots selected for the current set of
                    # sample slots
                    for lot in _used_ichiplots:
                        if lot in (active_lots[i][0] for i in
                                   range(number_unique_lot)):
                            continue  # Using the same lot as in a previous
                            # run, no new qc needed
                        else:
                            qc_list = self.getQCAliquots(assay_parameters)
                            for qc in qc_list:
                                working_aliquots.insert(0, qc)
                            break  # we know at least one lot is new and as such
                            #  we need to run qc on the current set of samples
                    break
            # Code section to select iChips
            # number_same_lot
            for a in active_lots:
                ichiplot = a[0]
                ichips = a[1]
                j = []
                # active_lots has the needed number of ichiplots, and has
                # enough chips for at least one pass!
                if plate_count != 0:
                    for ichip in ichips:
                        if ichip in _used_ichips:
                            continue
                        else:
                            j.append(ichip)
                            _used_ichips.append(ichip)
                            if len(j) == number_same_lot:
                                break
                    for d in j:
                        required_ichips_for_testing.append(d)
                if plate_count == 0:
                    required_ichips_for_testing.extend(ichips[:number_same_lot])
                    _used_ichips.extend(ichips[:number_same_lot])

            # a this point we have a selection of ichips, we now need to get
            # samples to be run on them.
            # Pick QC to run on ichips in the plate, will need to do this if and
            # when ichip lots change
            # make variable
            # sample slots (max of *) want to make it dynamic range(
            # 1:frame_count)
            # wrap this in an if statement
            sample_slots = []
            for i in range(frame_count - len(sample_slots)):
                if working_aliquots:
                    sample_slots.append(working_aliquots[0])
                    working_aliquots = working_aliquots[1:]
            # We have the objects to this point, shoudn't we send the id's to
            #  the GUI,
            # but keep the objects in variables that can be used when the
            # user confirms the run?
            # I think it will save time of looking all this up again
            sample_ids = [x.id for x in sample_slots]
            # XXX Use residual slots for aliquots from Under Review QC samples.
            result.append(
                [[x.id, sample_ids] for x in required_ichips_for_testing])
            plate_count += 1

        return result

    def getQCSampleObject(self, veracis_id):
        """input veracis_id, get qc sample object
        """
        brains = find(portal_type='QCSample', review_state='in_use',
                                  veracis_id=veracis_id)
        if not brains:
            raise QCSampleNotFound
        return brains[0].getObject()


    # def queryQCWorkingAliquots(self, assay_parameters):
    #     """Query to get QC and Clinical working aliquots to test with.
    #     """
    #     aliquot_objects_for_testing = []
    #     # loop over all the samples coming into search
    #     for sample_dict in full_set:
    #         # object passed in from full_set
    #         parent = sample_dict['sample']  # parent is sample object
    #
    #         aliquots = self.collectAliquots(parent, Type='QC Aliquot (Working)')
    #         for c in aliquots:
    #             vol = assay_parameters['desired_working_aliquot_volume']
    #             if c.remaining_volume >= vol:
    #                 aliquot_objects_for_testing.append(c)
    #                 break
    #     if not aliquot_objects_for_testing:
    #         raise NoWorkingAliquotsFound
    #     return aliquot_objects_for_testing


    def getQCAliquots(self, assay_parameters):
        """Get QC's aliquots
        """
        hqc = assay_parameters['number_of_high_value_controls']
        hqc_veracis_id = assay_parameters['qc_high_choice']
        hqc_object = self.getQCSampleObject(hqc_veracis_id)
        lqc = assay_parameters['number_of_low_value_controls']
        lqc_veracis_id = assay_parameters['qc_low_choice']
        lqc_object = self.getQCSampleObject(lqc_veracis_id)
        max_plates = assay_parameters['max_number_of_plates_per_test_run']
        number_same_lot = assay_parameters[
            'number_of_same_lot_replication_needed_for_samples']
        number_unique_lot = assay_parameters[
            'number_of_unique_ichips_lots_needed']
        frame_count = assay_parameters['framecount']
        min_volume_per_sample = assay_parameters[
            'minimum_working_aliquot_volume']

        hqc_aliquots = self.collectAliquots(
            hqc_object,
            Type='QC Aliquot (Working)',
            remaining_volume = {'query':min_volume_per_sample,'range':'min'})
        if not hqc_aliquots:
            raise QCAliquotNotFound(
                "%s has no aliquots that meet assay parameters"%hqc_object)
        hqc_aliquot_to_add_to_plate = hqc_aliquots[0]

        lqc_aliquots = self.collectAliquots(
            lqc_object,
            Type='QC Aliquot (Working)',
            remaining_volume = {'query':min_volume_per_sample,'range':'min'})
        if not lqc_aliquots:
            raise QCAliquotNotFound(
                "%s has no aliquots that meet assay parameters"%lqc_object)
        lqc_aliquot_to_add_to_plate = lqc_aliquots[0]

        import pdb;pdb.set_trace()
        qc_to_add_to_plate = [hqc_aliquot_to_add_to_plate] * hqc
        qc_to_add_to_plate += [lqc_aliquot_to_add_to_plate] * lqc
        print qc_to_add_to_plate
        return qc_to_add_to_plate

    def makePullList(self):
        """Make a simple pull list of box location number and sample IDs to pull
        for test run
        """
        pass

    def makePlateHTML(self, plates, frame_count):
        """Get in the Plate Number from AJAX request, build HTML code,
        pass back to be inserted into form
        """
        # thinks to know plates[0] = plate 1 for assay
        # plates[0][0] is plate1 chip 1
        # plates[0][0][0] is ichip id as a string
        # plates[0][0][1] is aliquot ids as strings in a list
        for index, plate in enumerate(plates):
            plate_number = index + 1
            for ichips in plate:
                pass

    def getiChipsForTesting(self, assay, sample_count, frame):
        """Get ALL iChips that can be used for the selected assay
        [[<iChipLotID>,[<iChip>,<iChip>,<iChip>]]]
        """
        ichips_for_assay = []

        brains = find(portal_type='iChipLot',
                      review_state='released',
                      sort_on='expires')
        if not brains:
            raise NoIchipLotsFound

        ichiplots = []
        for brain in brains:
            ichiplot = brain.getObject()
            if assay in ichiplot.intended_assay \
                    and int(ichiplot.frames) == int(frame):
                # commercial needs, correct assay
                # want to order the ichiplots in this list by exp date
                ichiplots.append(ichiplot)

        for ichiplot in ichiplots:
            ichips_for_assay.append([ichiplot, ichiplot.objectValues()])

        return ichips_for_assay
