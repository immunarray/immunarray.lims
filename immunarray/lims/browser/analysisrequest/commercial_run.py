# -*- coding: utf-8 -*-
import datetime
import json
from operator import itemgetter

from Products.CMFPlone.resources import add_resource_on_request
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from immunarray.lims.vocabularies.ichipassay import IChipAssayListVocabulary
from plone import api
from plone.i18n.normalizer.interfaces import IIDNormalizer
from zope.component import queryUtility


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
            frames = assay_parameters['framecount']

            # get dictionary of all the samples that need to be tested for the
            # selected assay. logic on what samples to be tested can make
            # decisions based on the assay_parameters status

            if assay_parameters['status'] == 'Commercial':
                max_nr_samples = self.maxNumberOfSamplesToRun(assay_parameters)
                full_set = self.queryClinicalSamples(assay, max_nr_samples)
                sample_count = len(full_set)
                # insert feedback for not samples needing to be tested status
                # =210
                ichips = self.getiChipsForTesting(assay, sample_count, frames)
                working_aliquots = self.queryWorkingAliquots(full_set,
                                                             assay_parameters)
                plates = self.makeTestPlan(assay_parameters, ichips,
                                           max_nr_samples, sample_count,
                                           working_aliquots)
                return json.dumps({"TestRun": plates})

            if assay_parameters['status'] == 'Development':
                samples_to_get = 'RandDSample'
                # make a development run
                development_samples = {}
                ichips_for_session = {}
                solutions_for_session = {}

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
            'sample_qc_dilution_factor',
            'sample_qc_dilution_material',
            'status',
            'title',
        ]
        normalize = queryUtility(IIDNormalizer).normalize
        for brain in api.content.find(portal_type='iChipAssay'):
            assay_obj = brain.getObject()
            assay_pretty_name = normalize(
                "{}-{}".format(assay_obj.title, assay_obj.status)).upper()
            ichipassays[assay_pretty_name] = assay_obj
        assay_obj = ichipassays[assay]
        params = {t: assay_obj._get_request_var_or_attr(t, '')
                  for t in variables_to_get}
        return params

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

    def queryClinicalSamples(self, assay, max_nr_samples):
        """Get all the samples that are 'received', order them by date, 
        and filter them for those who's test_ordered_status is one of 
        'Received', 'Rerun', or 'To Be Tested'.
        """
        brains = api.content.find(
            portal_type='ClinicalSample', review_state='received')
        tmp = {}
        for sample in (b.getObject() for b in brains):
            # collate the samples by the test_ordered_status.

            if assay in sample.test_ordered_status:
                status = sample.test_ordered_status[assay]
                if status not in tmp:
                    tmp[status] = []
                tmp[status].append({'uid': sample.UID(),
                                    'draw_date': sample.collection_date,
                                    'test_status': sample.test_ordered_status,
                                    'sample': sample})
        # now sort all the lists in tmp
        for key in tmp.keys():
            tmp[key] = sorted(tmp[key], key=itemgetter('draw_date'))

        a = tmp.get('Rerun', []) + \
            tmp.get('Received', []) + \
            tmp.get('To Be Tested', [])

        return a[:max_nr_samples]

    def queryWorkingAliquots(self, full_set, assay_parameters):
        """Query to get working aliquots to test with
        """
        aliquot_uids_for_testing = []
        # loop over all the samples coming into search
        for sample_dict in full_set:
            # object passed in from full_set
            parent = sample_dict['sample']  # parent is sample object
            # get child items
            children = parent.items()
            aliquots = self.collectAliquots(children)
            print aliquots
            for c in aliquots:
                # wrap a safety net on checking aliquots
                try:
                    vol = assay_parameters['desired_working_aliquot_volume']
                    if c.aliquot_type == "Working" \
                            and c.consume_date is None\
                            and c.volume >= vol:
                        aliquot_uids_for_testing.append(c)
                        break
                except:
                    print "object " + c.id + " lacks the ability to be checked"
        return aliquot_uids_for_testing

    def collectAliquots(self, array_of_aliquots):
        """Get in array of objects to see if they are the last in the chain
        and return a list of objects back.  Check if each is a working aliquot
        that meets the needs of the assay
        """
        all_child_objects = []
        for n in array_of_aliquots:
            all_child_objects.append(n[1])
        for n in array_of_aliquots:
            if n[1].items() is None:
                all_child_objects.append(n[1])
            else:
                all_child_objects.extend(self.collectAliquots(n[1].items()))
        return all_child_objects

    def getiChipsForTesting(self, assay, sample_count, frame):
        """Get ALL iChips that can be used for the selected assay
        [[<iChipLotID>,[<iChip>,<iChip>,<iChip>]]]
        """
        # convert frame to string
        st_frame = str(frame)
        values = api.content.find(portal_type='iChipLot')
        ichiplot_uid = [u.UID for u in values]
        # get the UID for each iChipLot in the LIMS
        list_ichiplot_and_ichips = []
        # get iChipLots in order first, then get child objects
        tmp = []
        today = datetime.date.today()
        for v in ichiplot_uid:
            ichiplot = api.content.get(UID=v)
            for n in ichiplot.intended_assay:
                if n == assay \
                        and ichiplot.acceptance_status == 'Passed' \
                        and ichiplot.frames == st_frame \
                        and ichiplot.ichip_lot_expiration_date > today:
                    # commercial needs, correct assay
                    # want to order the ichiplots in this list by exp date
                    tmp.append([ichiplot.ichip_lot_expiration_date, ichiplot])
        tmp.sort()
        for a in tmp:
            ichiplot = a[1]
            ichips_in_lot = ichiplot.contentIds()
            list_ichip_objects = []
            for ichip in ichips_in_lot:
                chip_object = ichiplot.__getitem__(ichip)
                if chip_object.ichip_status == 'Released':
                    list_ichip_objects.append(chip_object)
            # list_ichip_objects.sort() #Places objects in reverse order?
            list_ichiplot_and_ichips.append([ichiplot, list_ichip_objects])
        return list_ichiplot_and_ichips

    def iChipAssayList(self):
        vocab_keys = IChipAssayListVocabulary.__call__(self).by_value.keys()
        return vocab_keys

    def get_vocab_keys(self, vocab):
        vocab_keys = vocab.__call__(self).by_value.keys()
        return vocab_keys

    def makeTestPlan(self, assay_parameters, ichips_for_assay,
                     max_nr_samples, sample_count, working_aliquots):
        """use ordered [ichiplot, [ichips]], assay parameters{},
        [working aliquots] to build test plan
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

        wells_needed_per_sample = number_same_lot * number_unique_lot
        number_of_ichip_lots_available = len(ichips_for_assay)
        # [[<ichiplot>,[<ichip>,<ichip>]],[<ichiplot>,[<ichip>,<ichip>]]]
        if number_of_ichip_lots_available >= number_unique_lot:
            print "Enough iChip Lots To Start Evaluation Process"
        else:
            print "Can Run Selected Assay, Not Enough Unique iChip Lots"
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
            for n in ichips_for_assay:
                ichip_lot_object = n[0]
                list_of_ichip_objects = n[1]
                # That tells me if we have used this lot before
                if ichip_lot_object.title.split(".")[0] not in (
                        active_lots[j][0].title.split(".")[0] for j in
                        range(len(active_lots))):
                    # faulty because we don't update the list_of_ichip_objects,
                    # if true once it will always be true!
                    if len(list_of_ichip_objects) >= number_same_lot:
                        if ichip_lot_object not in _used_ichiplots:
                            active_lots.append(n)
                            _used_ichiplots.append(ichip_lot_object)
                        elif ichip_lot_object in _used_ichiplots:
                            running_chip_count_in_lot = 0
                            for chip in _used_ichips:
                                if chip.getParentNode() == ichip_lot_object:
                                    running_chip_count_in_lot += 1  # count
                                    # of how many ichips have been used from
                                    # current lot
                            if len(
                                    list_of_ichip_objects) - \
                                    running_chip_count_in_lot >= \
                                    number_same_lot:
                                active_lots.append(n)
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
                ichip_objects = a[1]
                ichip_lot_object = a[0]
                c = []
                # active_lots has the needed number of ichiplots, and has
                # enough chips for at least one pass!
                if plate_count != 0:
                    for ichip in ichip_objects:
                        if ichip in _used_ichips:
                            continue
                        else:
                            c.append(ichip)
                            _used_ichips.append(ichip)
                            if len(c) == number_same_lot:
                                break
                    for d in c:
                        required_ichips_for_testing.append(d)
                if plate_count == 0:
                    required_ichips_for_testing.extend(
                        ichip_objects[:number_same_lot])
                    _used_ichips.extend(ichip_objects[:number_same_lot])

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
            result.append(
                [[x.id, sample_ids] for x in required_ichips_for_testing])
            plate_count += 1
        return result

    def getQCSampleObject(self, veracis_id):
        """input veracis_id, get qc sample object
        """
        qc = veracis_id
        values = api.content.find(context=api.portal.get(),
                                  portal_type='QCSample')
        qc_sample_ids = [v.UID for v in values]
        d = []
        for i in qc_sample_ids:
            a = api.content.get(UID=i)
            if qc == a.veracis_id:
                d.append(a)
                break
        return d

    def selectQCAliquot(self, number_of_controls, min_working_volume,
                        number_same_lot_replication, number_of_unique_ichips,
                        array_of_qc_samples):
        """Input of wells to test, array of qc aliquots, return aliquot that can
         be used for testing
        """
        wells_to_test = number_of_controls * number_same_lot_replication * \
                        number_of_unique_ichips
        min_volume = wells_to_test * min_working_volume
        for c in array_of_qc_samples:
            # wrap a safety net on checking aliquots
            try:
                if c.aliquot_type == "Working" and c.consume_date is None and\
                                c.volume >= min_volume:
                    return c
                else:
                    print "Aliquot Does Not Meet Needs of Assay UID of Object " \
                          "Checked is " + c.UID()
            except:
                print "object " + c.UID() + " lacks the ability to be checked"

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

        hqc_aliquots = self.collectAliquots(hqc_object[0].items())
        hqc_aliquot_to_add_to_plate = self.selectQCAliquot(
            hqc, min_volume_per_sample, number_same_lot, number_unique_lot,
            hqc_aliquots)

        lqc_aliquots = self.collectAliquots(lqc_object[0].items())
        lqc_aliquot_to_add_to_plate = self.selectQCAliquot(
            lqc, min_volume_per_sample, number_same_lot, number_unique_lot,
            lqc_aliquots)
        # Check to see if set of ichip lots have been used in previous run?

        qc_to_add_to_plate = [hqc_aliquot_to_add_to_plate] * assay_parameters[
            'number_of_high_value_controls']
        qc_to_add_to_plate += [lqc_aliquot_to_add_to_plate] * assay_parameters[
            'number_of_low_value_controls']
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
