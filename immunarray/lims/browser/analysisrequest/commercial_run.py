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
            # get dictionary of all the samples that need to be tested for the selected assay
            all_to_be_tested_sample_ids={}
            import pdb;pdb.set_trace()

        return self.template()
    def getInfoAboutSelectedAssay(self, assay):
        """Use end user selection to pull needed number of working aliqutots for assay
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
            # import pdb;pdb.set_trace()

        
    def querySamples(self, assay):
        """Get all the samples that have pending test and arrange them by
        collection date
        """
        values = api.content.find(context=api.portal.get(), portal_type='ClinicalSample')
        things_to_test = {}
        #key = id, values = [uid,draw_date,test_status]
        sample_ids_to_be_tested = []
        sample_uids_to_be_tested = []
        # get ClinicalSamples where values.sample_status = 'Received'
        for u in values:
            if u.sample_status == 'Received':
                uids = [u.UID for u in values]
                # need to open the samples that have pending tests and get the SLE
                # get a.test_ordered_status
                # u'SLEKEY-RO-V2-0-COMMERCIAL': u'Received', only want to test the ones that are in "To Be Tested"
                # append UIDs to list, that will be used to update all selected samples on save of test plan
                # need to get all reruns first
                # get all "To Be Tested" next
        # get UIDs
        pass



    def getiChipsForTesting(self, assay, sample_count):
        """Get iChips needed for testing
        """
        pass
        # Get iChipLots that are not expired
        # ichip_lot_expiration_date
        # Get iChipLots that have the correct layout
        # frames == '8 Frame iChips'
        # Get iChipLots that are for the correct test
        # intended_assay = 'SLEKEY-RO-V2-0-COMMERCIAL'
        # Get iChipLots that passed QC process
        # iChipAcceptanceStatus =='Passed'
        # Have to open up the iChipLots, then walk them!
        #values = api.content.find(context=api.portal.get(), portal_type='iChipLot')
        #ichip_uids = [u.UID for u in values]
        #for i in ichip_uids:

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
