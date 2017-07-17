# -*- coding: utf-8 -*-
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

class AddCommercialEightFrameTestRunView(BrowserView):

    template = ViewPageTemplateFile("templates/aliquot_testing/SLE-key_v_2_0_commercial.pt")

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
            # setup for "custom"
            assay_parameters = self.getInfoAboutSelectedAssay(assay)
            frames=assay_parameters['ichiptype']
            # get dictionary of all the samples that need to be tested for the selected assay
            # logic on what samples to be tested
            # can make decisions based on the assay_parameters status
            status_from_test_choice = assay_parameters["status"]
            if status_from_test_choice == 'Commercial':
                samples_to_get = 'ClinicalSample'
                full_set = self.queryClinicalSamples(assay,samples_to_get)
                sample_count = full_set.__len__()
                #Need to order full_set by collection_date oldest to newest, then test_ordered_status
                ichips_for_assay = self.getiChipsForTesting(assay, sample_count, frames)
                # import pdb;pdb.set_trace()
                commercial_samples={}
                ichips_for_session={}
                # How do we want to get solutions?
                # Need to add it to iChip Assay?
                soluitons_for_session={}
            if status_from_test_choice == 'Development':
                samples_to_get = 'RandDSample'
                # make a developmoent run
                development_samples={}
                ichips_for_session={}
                soluitons_for_session={}
            if assay == 'Custom':
                all_samples_in_lims={}
                ichips_for_session={}
                soluitons_for_session={}
        return self.template()

    def getInfoAboutSelectedAssay(self, assay):
        """Use end user selection to pull needed number of working aliquots for assay
        """
        # Code that makes the vocabulary for iChipAssay, use this to get the UID?
        values = api.content.find(context=api.portal.get(), portal_type='iChipAssay')
        ichipassays = {}
        selected_assay_paramaters={}
        variables_to_get=['creation_date','creators','description','desired_working_aliquot_volume','ichiptype','id','max_number_of_plates_per_test_run','modification_date','number_of_high_value_controls','number_of_low_value_controls','number_of_same_lot_replication_needed_for_samples','number_of_unique_ichips_lots_needed','number_of_working_aliquots_needed','portal_type','sample_qc_dilution_factor','sample_qc_dilution_material','status','title']
        ichipassay_ids = [v.UID for v in values]
        for i in ichipassay_ids:
            value = api.content.get(UID=i)
            assay_name_with_spaces = "-".join([value.title, value.status])
            normalizer = queryUtility(IIDNormalizer)
            assay_name_post_norml = normalizer.normalize(assay_name_with_spaces).upper()
            ichipassays.update({assay_name_post_norml:i})
        try:
            ichipassay_uid = ichipassays[assay]
            assay_object = api.content.get(UID=ichipassay_uid)
            for t in variables_to_get:
                selected_assay_paramaters.update({t:assay_object._get_request_var_or_attr(t, '')})
            return selected_assay_paramaters
        except:
            print "Assay Parameters Not Available"

    def queryClinicalSamples(self, assay,samples_to_get):
        """Get all the samples that have pending test and arrange them by
        collection date
        """
        values = api.content.find(context=api.portal.get(), portal_type=samples_to_get)
        all_to_test = {}
        #key = id, values = [uid,draw_date,test_status]
        # fast search to limit the options
        # get ClinicalSamples where values.sample_status = 'Received'
        for u in values:
            if u.sample_status == 'Received':
                open_clinical_sample_uids = [u.UID for u in values]
                for ocs in open_clinical_sample_uids:
                    #open object
                    a=api.content.get(UID=ocs)
                    # check for 'Rerun' or 'To Be Tested' or 'Received'
                    if a.test_ordered_status[assay] == "Received" or a.test_ordered_status[assay] == "Rerun" or a.test_ordered_status[assay] == "To Be Tested":
                        # add sample info to all_to_test dict, {UID:[title, collection_date, test_ordered_status]}
                        all_to_test.update({ocs:[a.title, a.collection_date, a.test_ordered_status]})
        return all_to_test

    def queryWorkingAliqutos(self):
        """Query to get working aliquots to test with
        """
        pass

    def getiChipsForTesting(self, assay, sample_count, frame):
        """Get iChips needed for testing
        """
        values = api.content.find(context=api.portal.get(), portal_type='iChipLot')
        ichiplot_uid =[u.UID for u in values]
        lots_for_selected_assay=[]
        dict_ichips={}
        for v in ichiplot_uid:
            ichiplot = api.content.get(UID=v)
            for n in ichiplot.intended_assay:
                if n == assay and ichiplot.acceptance_status == 'Passed' and ichiplot.frames == frame:
                    ichips_in_lot=[]
                    lots_for_selected_assay.append(ichiplot.title)
                    current_ichips = ichiplot.contentItems()
                    import pdb;pdb.set_trace()
        import pdb;pdb.set_trace()
                # give the ichip lot in a list
                # need to get id of ichips in each lot that can be used for testing

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
