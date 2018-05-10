# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from immunarray.lims.interfaces.assayrequest import IAssayRequest
from immunarray.lims.interfaces.clinicalsample import IClinicalSample
from immunarray.lims.interfaces.qcsample import IQCSample
from immunarray.lims.interfaces.sample import ISample
from plone.api.content import find, get_state


class ResultsView(BrowserView):
    template = ViewPageTemplateFile("templates/results.pt")

    def __init__(self, context, request):
        BrowserView.__init__(self, context, request)
        self.context = context
        self.request = request
        self.errors = []

    def __call__(self):
        # noinspection PyArgumentList
        return self.template()

    def state(self):
        """return the current review_state of context
        """
        return get_state(self.context)

    def get_parent_sample_from_aliquot(self, aliquot):
        parent = aliquot.aq_parent
        while not ISample.providedBy(parent):
            parent = parent.aq_parent
        return parent

    def get_assay_request_from_sample(self, sample):
        for child in sample.objectValues():
            if IAssayRequest.providedBy(child):
                return child

    def get_all_samples(self):
        return self.get_qc_samples() + self.get_clinical_samples()

    def get_qc_samples(self):
        samples = set()
        for plate in self.context.plates:
            for key, val in plate.items():
                brains = find(object_provides=IQCSample.__identifier__,
                              run_number=self.run_number)
                if brains:
                    samples.add(brains[0].getObject())
        return samples

    def get_clinical_samples(self):
        samples = set()
        for plate in self.context.plates:
            for key, val in plate.items():
                brains = find(object_provides=IClinicalSample.__identifier__,
                              run_number=self.run_number)
                if brains:
                    samples.add(brains[0].getObject())
        return samples
