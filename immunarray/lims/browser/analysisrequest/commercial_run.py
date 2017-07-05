# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.dexterity.utils import createContentInContainer
from plone import api
from bika.lims.permissions import disallow_default_contenttypes
from plone.dexterity.utils import createContentInContainer
from Products.CMFPlone.resources import add_resource_on_request
from Products.statusmessages.interfaces import IStatusMessage
import plone.protect
import json
import datetime



class AddCommercialEightFrameTestRunView(BrowserView):

    template = ViewPageTemplateFile("templates/aliquot_testing/SLE-key_v_2_0_commercial.pt")

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.errors = []


    def __call__(self):
        add_resource_on_request(self.request, "static.js.commercial_run.js")
        # request = self.request
        #assay = self.request('testtorun')

        #if "buildrun" in request.form:
        #    authenticator = request.form.get('_authenticator')
        #    try:

        return self.template()


    def querysamples(self, assay):
        """Get all the samples that have pending test and arrange them by
        collection date
        """

        values = api.content.find(context=api.portal.get(), portal_type='ClinicalSample')
        sample_ids_to_be_tested = []
        # get ClinicalSamples where values.sample_status = 'Received'
        for u in values:
            if u.sample_status == 'Received':
                uids = [u.UID for u in values]
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


