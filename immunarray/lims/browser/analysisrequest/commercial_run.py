# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from immunarray.lims.interfaces.clinicalsample import IClinicalSample
from plone.dexterity.utils import createContentInContainer
from plone import api
from bika.lims.permissions import disallow_default_contenttypes
from immunarray.lims.permissions import AddClinicalSample
from immunarray.lims.permissions import AddClinicalAliquot
from immunarray.lims.permissions import AddPatient
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
        request = self.request
        return self.template()
