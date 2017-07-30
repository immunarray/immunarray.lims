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
            frames = assay_parameters['ichiptype']
            # get dictionary of all the samples that need to be tested for the selected assay
            # logic on what samples to be tested
            # can make decisions based on the assay_parameters status
            status_from_test_choice = assay_parameters['status']

            if status_from_test_choice == 'Commercial':
                full_set = self.queryClinicalSamples(assay)
                sample_count = full_set.__len__()
                ichips_for_assay = self.getiChipsForTesting(assay, sample_count,
                                                            frames)
                # Need to order full_set by collection_date oldest to newest, then test_ordered_status
                get_working_aliquots = self.queryWorkingAliqutos(full_set, assay_parameters)
                # how many samples are in queue?
                sample_queue_lenght = get_working_aliquots.len()
                max_number_of_samples = self.maxNumberOfSamplesToRun(assay_parameters)
                # how many plates will this test run be?
                # build test run object
                # list of cs and ichips selected for initial return to the test form

                commercial_samples_inital = []
                ichips_for_assay_initial = []

                # How do we want to get solutions?
                # Need to add it to iChip Assay?
                soluitons_for_session = {}

            if status_from_test_choice == 'Development':
                samples_to_get = 'RandDSample'
                # make a developmoent run
                development_samples = {}
                ichips_for_session = {}
                soluitons_for_session = {}

            if assay == 'Custom':
                all_samples_in_lims = {}
                ichips_for_session = {}
                soluitons_for_session = {}

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
                            'desired_working_aliquot_volume', 'ichiptype', 'id',
                            'max_number_of_plates_per_test_run',
                            'modification_date',
                            'number_of_high_value_controls',
                            'number_of_low_value_controls',
                            'number_of_same_lot_replication_needed_for_samples',
                            'number_of_unique_ichips_lots_needed',
                            'number_of_working_aliquots_needed', 'portal_type',
                            'sample_qc_dilution_factor',
                            'sample_qc_dilution_material', 'status', 'title']
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
        """take the assay paramaters and determine the max number of samples
        that can be tested in a single run
        """
        max_plates = assay_parameters['max_number_of_plates_per_test_run']
        hqc = assay_parameters['number_of_high_value_controls']
        lqc = assay_parameters['number_of_low_value_controls']
        number_same_lot = assay_parameters['number_of_same_lot_replication_needed_for_samples']
        number_unique_lot = assay_parameters['number_of_unique_ichips_lots_needed']
        frame_type = assay_parameters['ichiptype'] # update type to be frame type (int)
        wells_needed_per_sample = number_same_lot * number_unique_lot
        max_wells = max_plates * frame_type
        wells_for_hqc = wells_needed_per_sample * hqc
        wells_for_lqc = wells_needed_per_sample * lqc

    def queryClinicalSamples(self, assay):
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
        for key in tmp.keys():
            tmp[key] = sorted(tmp[key], key=itemgetter('draw_date'))

        # import pdb;pdb.set_trace()
        # then return the groups, in order.
        return tmp.get('Received', []) + \
               tmp.get('Rerun', []) + \
               tmp.get('To Be Tested', [])

    def queryWorkingAliqutos(self, full_set, assay_parameters):
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
            import pdb;pdb.set_trace()
            for c in aliquots:
                #wrap a safety net on checking aliquots
                try:
                    if c.aliquot_type == "Working" and c.consume_date is None and c.volume >= assay_parameters['desired_working_aliquot_volume']:
                        aliquot_uids_for_testing.append(c)
                        break # get out of the current loop!
                    else:
                        print "no aliquot found for at this level", c.id
                except:
                    print "object "+ c.id +" lacks the ability to be checked"
        return aliquot_uids_for_testing

    def collectAliquots(self, array_of_aliquots):
        """get in array of objects to see if they are the last in the chain and return a list of objects back
        """
        # get in array of objects to see if they are the last in the chain,
        # return a list of objects back
        all_child_objects = [] #array of objects
        for n in array_of_aliquots:
            all_child_objects.append(n[1]) #adding all objects that came into the function to the running tab of objects
        for n in array_of_aliquots:
            if n[1].items() is None: # means it doesn't have a child object and is the end of the line
                all_child_objects.append(n[1])
            else:
                a = self.collectAliquots(n[1].items()) # pass object n[1] to collectAliquots
                # return an array of child objects
                for n in a: # trick is that only objects are in the returned array
                    all_child_objects.append(n)
        return all_child_objects

    def getiChipsForTesting(self, assay, sample_count, frame):
        """Get iChips needed for testing
        """
        values = api.content.find(context=api.portal.get(),
                                  portal_type='iChipLot') # gets the catalog brains for the iChipLot objects
        ichiplot_uid = [u.UID for u in values] # get the UID for each iChipLot in the LIMS
        lots_for_selected_assay = []
        dict_ichips = {}
        for v in ichiplot_uid:
            ichiplot = api.content.get(UID=v)
            for n in ichiplot.intended_assay:
                if n == assay and ichiplot.acceptance_status == 'Passed' and ichiplot.frames == frame:
                    # commercial needs
                    dict_key = ichiplot.title
                    ichips_in_lot = ichiplot.contentIds()
                    dict_values = []
                    for ichip in ichips_in_lot:
                        a = ichiplot.__getitem__(ichip)
                        if a.ichip_status == 'Released':
                            chip_uid = a.UID()
                            dict_values.append(chip_uid)
                        dict_ichips.update({dict_key: dict_values})
        print dict_ichips
        return dict_ichips

    def makePullList(self):
        """Make a simple pull list of box location number and sample IDs to pull
        for test run
        """
        pass

    def ichipassaylist(self):
        vocab_keys = IChipAssayListVocabulary.__call__(self).by_value.keys()
        return vocab_keys

    def get_vocab_keys(self, vocab):
        vocab_keys = vocab.__call__(self).by_value.keys()
        return vocab_keys


