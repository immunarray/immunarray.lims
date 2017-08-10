# -*- coding: utf-8 -*-
from operator import itemgetter

from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.dexterity.utils import createContentInContainer
from plone import api
from bika.lims.permissions import disallow_default_contenttypes
from plone.dexterity.utils import createContentInContainer
from Products.CMFPlone.resources import add_resource_on_request
from Products.statusmessages.interfaces import IStatusMessage
from immunarray.lims.vocabularies.ichipassay import IChipAssayListVocabulary
import plone.protect
import json
import datetime
from zope.component import getUtility
from zope.component import queryUtility
from plone.i18n.normalizer.interfaces import IIDNormalizer
from zope.schema.interfaces import IVocabularyFactory
from Products.CMFCore.utils import getToolByName
import fnmatch


class AddCommercialEightFrameTestRunView(BrowserView):
    template = ViewPageTemplateFile(
        "templates/aliquot_testing/SLE-key_v_2_0_commercial.pt")

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.errors = []

    def __call__(self):
        add_resource_on_request(self.request, "static.js.test_run.js")
        request = self.request
        iChipAssayList = self.get_vocab_keys(IChipAssayListVocabulary)
        if "assaySeleced" in request.form:
            authenticator = request.form.get('_authenticator')
            # gives me the assay value from the ctest form
            assay = request.form.get("assaySeleced")
            if assay == 'None':
                return self.template()  # setup for "custom"

            assay_parameters = self.getInfoAboutSelectedAssay(assay)
            frames = assay_parameters['framecount']
            # get dictionary of all the samples that need to be tested for the selected assay
            # logic on what samples to be tested
            # can make decisions based on the assay_parameters status
            status_from_test_choice = assay_parameters['status']

            if status_from_test_choice == 'Commercial':
                # how many samples can we test under best case?
                max_number_of_samples = self.maxNumberOfSamplesToRun(assay_parameters)
                # what samples need to be tested for the selected assay?
                full_set = self.queryClinicalSamples(assay, max_number_of_samples)
                # how many samples in the returned list?
                sample_count = len(full_set)
                # What iChipLots and iChips can be used for the selected assay?
                ichips_for_assay = self.getiChipsForTesting(assay, sample_count, frames)
                # Need to order full_set by collection_date oldest to newest,
                # then test_ordered_status
                get_working_aliquots = self.queryWorkingAliquots(full_set, assay_parameters)
                # how many samples are in queue?
                sample_queue_length = len(get_working_aliquots)
                # theoretical max samples to test under perfect conditions

                # how many plates will this test run be?
                # build test run object
                # list of cs and ichips selected for initial return to the test form
                plates = self.makeTestPlan(assay_parameters,ichips_for_assay, max_number_of_samples, sample_count, get_working_aliquots)
                commercial_samples_inital = []
                ichips_for_assay_initial = []

                # How do we want to get solutions?
                # Need to add it to iChip Assay?
                solutions_for_session = {}

            if status_from_test_choice == 'Development':
                samples_to_get = 'RandDSample'
                # make a developmoent run
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
        """Use end user selection to pull needed number of working aliquots for assay
        """
        # Code that makes the vocabulary for iChipAssay, use this to get the UID?
        values = api.content.find(context=api.portal.get(),
                                  portal_type='iChipAssay')
        ichipassays = {}
        selected_assay_paramaters = {}
        variables_to_get = ['creation_date', 'creators', 'description',
                            'desired_working_aliquot_volume', 'framecount', 'id',
                            'max_number_of_plates_per_test_run',
                            'modification_date',
                            'number_of_high_value_controls',
                            'number_of_low_value_controls',
                            'number_of_same_lot_replication_needed_for_samples',
                            'number_of_unique_ichips_lots_needed',
                            'number_of_working_aliquots_needed', 'portal_type',
                            'sample_qc_dilution_factor',
                            'sample_qc_dilution_material', 'status', 'title',
                            'qc_high_choice', 'qc_low_choice',
                            'minimum_working_aliquot_volume']
        ichipassay_ids = [v.UID for v in values]
        for i in ichipassay_ids:
            value = api.content.get(UID=i)
            assay_name_with_spaces = "-".join([value.title, value.status])
            normalizer = queryUtility(IIDNormalizer)
            assay_name_post_norml = normalizer.normalize(
                assay_name_with_spaces).upper()
            ichipassays.update({assay_name_post_norml: i})
        try:
            ichipassay_uid = ichipassays[assay]
            assay_object = api.content.get(UID=ichipassay_uid)
            for t in variables_to_get:
                selected_assay_paramaters.update(
                    {t: assay_object._get_request_var_or_attr(t, '')})
            return selected_assay_paramaters
        except:
            print "Assay Parameters Not Available"

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
        sample_wells = max_wells - (testing_wells_for_hqc + testing_wells_for_lqc)
        max_samples_to_test = sample_wells - wells_needed_per_sample
        return max_samples_to_test

    def queryClinicalSamples(self, assay, max_number_of_samples):
        """Get all the samples that are 'received', order them by date, 
        and filter them for those who's test_ordered_status is one of 
        'Received', 'Rerun', or 'To Be Tested'.
        """
        brains = api.content.find(
            portal_type='ClinicalSample', review_state='received')
        tmp = {}
        for sample in (b.getObject() for b in brains):
            # collate the samples by the test_ordered_status.
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

        # now sort all the lists in tmp by draw_date
        #for key in tmp.keys():
        #    tmp[key] = sorted(tmp[key], key=itemgetter('draw_date'))
        # Cap with max number of samples so we don't waste overhead later
        # looking or things we can't test in the run
        # import pdb;pdb.set_trace()
        # then return the groups, in order.
        a = tmp.get('Rerun', []) + \
            tmp.get('Received', []) + \
            tmp.get('To Be Tested', [])
        c = []
        # just send back a if it is smaller than max number of samples
        if len(a) < max_number_of_samples:
            return a
        else:
            for b in a:
                count=0
                while count < max_number_of_samples:
                    c.append(b)
                    count += 1
                return c

    def queryWorkingAliquots(self, full_set, assay_parameters):
        """Query to get working aliquots to test with
        """
        aliquot_uids_for_testing = []
        need_to_make_aliquots = []
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
                    if c.aliquot_type == "Working" and c.consume_date is None and c.volume >= \
                            assay_parameters['desired_working_aliquot_volume']:
                        aliquot_uids_for_testing.append(c)
                        break
                except:
                    print "object " + c.id + " lacks the ability to be checked"
        return aliquot_uids_for_testing

    def collectAliquots(self, array_of_aliquots):
        """Get in array of objects to see if they are the last in the chain
        and return a list of objects back
        """
        """Check if it is a working aliquot that meets the needs of the assay
        """
        all_child_objects = []
        for n in array_of_aliquots:
            all_child_objects.append(n[1])
        for n in array_of_aliquots:
            if n[1].items() is None:
                all_child_objects.append(n[1])
            else:
                a = self.collectAliquots(n[1].items())
                for n in a:
                    all_child_objects.append(n)
        return all_child_objects

    def getiChipsForTesting(self, assay, sample_count, frame):
        """Get ALL iChips that can be used for the selected assay
        [[<iChipLotID>,[<iChip>,<iChip>,<iChip>]]]
        """
        # convert frame to string
        st_frame = str(frame)
        values = api.content.find(context=api.portal.get(),
                                  portal_type='iChipLot')
        ichiplot_uid = [u.UID for u in values]
        # get the UID for each iChipLot in the LIMS
        list_ichiplot_and_ichips = []
        # get iChipLots in order first, then get child objects
        tmp = []
        today = datetime.date.today()
        for v in ichiplot_uid:
            ichiplot = api.content.get(UID=v)
            for n in ichiplot.intended_assay:
                if n == assay and ichiplot.acceptance_status == 'Passed' and \
                                ichiplot.frames == st_frame and \
                                ichiplot.ichip_lot_expiration_date > today :
                    # commercial needs, correct assay
                    # want to order the ichiplots in this list by exp date
                    tmp.append([ichiplot.ichip_lot_expiration_date, ichiplot])
        tmp.sort()
        for a in tmp:
            ichiplot = a[1]
            ichips_in_lot = ichiplot.contentIds()
            list_ichip_objects = []
            for ichip in ichips_in_lot:
                b = ichiplot.__getitem__(ichip)
                if b.ichip_status == 'Released':
                    chip_object = b
                    list_ichip_objects.append(b)
            #list_ichip_objects.sort() #Places objects in reverse order?
            list_ichiplot_and_ichips.append([ichiplot,list_ichip_objects])
        return list_ichiplot_and_ichips

    def iChipAssayList(self):
        vocab_keys = IChipAssayListVocabulary.__call__(self).by_value.keys()
        return vocab_keys

    def get_vocab_keys(self, vocab):
        vocab_keys = vocab.__call__(self).by_value.keys()
        return vocab_keys

    def makeTestPlan(self, assay_parameters,ichips_for_assay, max_number_of_samples, sample_count, get_working_aliquots):
        """use ordered [ichiplot, [ichips]], assay parameters{}, [working aliquots] to build test plan
        """
        #how many plates do I need?
        # vars defined for operation



        slide_per_plate = 4 # constant that needs to be defined
        max_plates = assay_parameters['max_number_of_plates_per_test_run']
        number_same_lot = assay_parameters['number_of_same_lot_replication_needed_for_samples']
        number_unique_lot = assay_parameters['number_of_unique_ichips_lots_needed']
        frame_count = assay_parameters['framecount']
        min_volume_per_sample= assay_parameters['minimum_working_aliquot_volume']

        wells_needed_per_sample = number_same_lot * number_unique_lot # 4 in this case

        # Need to ensure that lots are unique V10_1 and V10_2 are the "same" lot
        # as the materials used to make them are the same, so we need to split
        # on _'s and be sure the first part is unique.

        number_of_ichip_lots_available = len(ichips_for_assay)
        # [[<ichiplot>,[<ichip>,<ichip>]],[<ichiplot>,[<ichip>,<ichip>]]]

        if number_of_ichip_lots_available >= number_unique_lot:
            print "Enough iChip Lots To Start Evaluation Process"
        else:
            print "Can Run Selected Assay, Not Enough Unique iChip Lots"
        plate_count = 0
        _used_ichiplots = []
        _used_ichips = []
        _used_samples = []
        _used_ichiplot_length = 0
        result = []  # thing that will be sent back each entry is a "plate"

        # condition that lets me know to keep making plates both parts must be true
        while plate_count <= max_plates and len(get_working_aliquots) >= 0:
            # add QC to get_working_aliquots is no ichiplots have been used
            if not _used_ichiplots:
                qc_list = self.getQCAliquots(assay_parameters)
                for qc in qc_list:
                    get_working_aliquots.insert(0, qc)

            active_lots =[]
            required_ichips_for_testing = []
            # get lot id independent to print lot, this value should be unique
            # for selection/addition to active lots!
            # ichips_for_assay[0][0].title.split(".")[0], gives ichip lot split
            # this is added all of the ichips_for_assay if any are selected!
            # not the specific chips
            # n = [<ichiplot>,[<ichip>,<ichip>, <ichip>]]
            # Code block selects iChip Lots to use!
            # number_unique_lot
            #while len(active_lots) <= number_unique_lot:
            import pdb;pdb.set_trace()
            for n in ichips_for_assay:  # V10.1 and V10.2 can't be in the set
                ichip_lot_object = n[0]
                list_of_ichip_objects = n[1]
                # Why do I care?  This doesn't drive any decisions
                # just forces new ichiplots to be selected!
                #if ichip_lot_object in _used_ichiplots:
                    # means that we have used this lot before!
                #    continue
                # this can't ever be false! Need to compare to _used_ichiplots!
                # That tells me if we have used this lot before
                if ichip_lot_object.title.split(".")[0] not in active_lots:
                    # faulty because we don't update the list_of_ichip_objects,
                    # if true once it will always be true!
                    if len(list_of_ichip_objects) >= number_same_lot:

                        if ichip_lot_object not in _used_ichiplots:
                            active_lots.append(n)
                            _used_ichiplots.append(ichip_lot_object)

                if len(active_lots) == number_unique_lot:
                    # have the ichiplots selected for the current set of sample slots
                    for lot in _used_ichiplots:
                        if lot in (active_lots[i][0] for i in range(number_unique_lot)):
                            continue # Using the same lot as in a previous run, no new qc needed
                        else:
                            qc_list = self.getQCAliquots(assay_parameters)
                            for qc in qc_list:
                                get_working_aliquots.insert(0, qc)
                            break  # we know at least one lot is new and as such we need to run qc on the current set of sample slots
                    break

            # while len(plate) < slide_per_plate:, put this in later

            # Code section to select iChips
            # number_same_lot

            for a in active_lots:
                ichip_objects = a[1]
                ichip_lot_object = a[0]
                # active_lots has the needed number of ichiplots, and has
                # enough chips for at least one pass!
                if ichip_objects not in _used_ichips:
                    required_ichips_for_testing.extend(ichip_objects[:number_same_lot])
                    _used_ichips.extend(ichip_objects[:number_same_lot])

            # a this point we have a selection of ichips, we now need to get
            # samples to be run on them.
            # Pick QC to run on ichips in the plate, will need to do this if and
            # when ichip lots change
            # make variable
            # sample slots (max of *) want to make it dynamic range(1:frame_count)
            # wrap this in an if statement
            # Check to see if set of ichip lots have been used in previous run?
            sample_slots = []
            for i in range(frame_count - len(sample_slots)):
                if get_working_aliquots:
                    sample_slots.append(get_working_aliquots[0])
                    get_working_aliquots = get_working_aliquots[1:]
            sample_ids = [x.id for x in sample_slots]
            result.append([[x.id, sample_ids] for x in required_ichips_for_testing])
            plate_count += 1  # increase plate_count

        # define test locations
        # test location
        # is the set of wells that each aliquot needs to be placed into
        # assign sample slots to required_ichips_for_testing
        # if required_ichips_for_testing  = 4 chips make a plate
        # else need to get more things to test to add to the set
        # need qc every time we change ichip lots!



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
        wells_to_test = number_of_controls * number_same_lot_replication * number_of_unique_ichips
        min_volume = wells_to_test * min_working_volume
        for c in array_of_qc_samples:
            # wrap a safety net on checking aliquots
            try:
                if c.aliquot_type == "Working" and c.consume_date is None and c.volume >= min_volume:
                    return c
                else: print "Aliquot Does Not Meet Needs of Assay UID of Object Checked is " + c.UID()
            except:
                print "object " + c.UID() + " lacks the ability to be checked"

    def getQCAliquots(self, assay_parameters):
        """Get QC's aliquots
        """
        hqc = assay_parameters['number_of_high_value_controls']
        hqc_veracis_id = assay_parameters['qc_high_choice']
        hqc_object = self.getQCSampleObject(hqc_veracis_id)
        lqc = assay_parameters['number_of_low_value_controls']
        lqc_veracis_id= assay_parameters['qc_low_choice']
        lqc_object = self.getQCSampleObject(lqc_veracis_id)
        max_plates = assay_parameters['max_number_of_plates_per_test_run']
        number_same_lot = assay_parameters['number_of_same_lot_replication_needed_for_samples']
        number_unique_lot = assay_parameters['number_of_unique_ichips_lots_needed']
        frame_count = assay_parameters['framecount']
        min_volume_per_sample= assay_parameters['minimum_working_aliquot_volume']

        hqc_aliquots = self.collectAliquots(hqc_object[0].items())
        hqc_aliquot_to_add_to_plate = self.selectQCAliquot(
            hqc, min_volume_per_sample, number_same_lot, number_unique_lot,
            hqc_aliquots)

        lqc_aliquots = self.collectAliquots(lqc_object[0].items())
        lqc_aliquot_to_add_to_plate = self.selectQCAliquot(
            lqc, min_volume_per_sample, number_same_lot, number_unique_lot,
            lqc_aliquots)
        # Check to see if set of ichip lots have been used in previous run?

        qc_to_add_to_plate = [hqc_aliquot_to_add_to_plate]*assay_parameters['number_of_high_value_controls']
        qc_to_add_to_plate += [lqc_aliquot_to_add_to_plate]*assay_parameters['number_of_low_value_controls']
        print qc_to_add_to_plate
        return qc_to_add_to_plate

    def makePullList(self):
        """Make a simple pull list of box location number and sample IDs to pull
        for test run
        """
        pass
