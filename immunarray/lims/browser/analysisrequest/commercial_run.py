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
from zope.schema.interfaces import IVocabularyFactory



class AddCommercialEightFrameTestRunView(BrowserView):

    template = ViewPageTemplateFile("templates/aliquot_testing/SLE-key_v_2_0_commercial.pt")

    def __init__(self, context, request):
        ichip_assays_terms = IChipAssayListVocabulary.__call__(self).by_value.keys()
        self.context = context
        self.request = request
        self.errors = []


    def __call__(self):
        add_resource_on_request(self.request, "static.js.commercial_run.js")
        # import pdb;pdb.set_trace()
        # request = self.request
        #assay = self.request('testtorun')

        #if "buildrun" in request.form:
        #    authenticator = request.form.get('_authenticator')
        #    try:

        return self.template()
    def getInfoAboutSelectedAssay(self, assay):
        """Use end user selection to pull needed number of working aliqutots for assay
        """
        #from IiChipAssay
        #title
        #ichiptype
        #number_of_unique_ichips_lots_needed
        #number_of_same_lot_replication_needed_for_samples
        #number_of_high_value_controls
        #number_of_low_value_controls
        #max_number_of_plates_per_test_run
        #number_of_working_aliquots_needed
        #sample_qc_dilution_factor
        #desired_working_aliquot_volume

        
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

    def get_ichip_assays(self):
        ichip_assays_terms = IChipAssayListVocabulary.__call__(self).by_value.keys()


