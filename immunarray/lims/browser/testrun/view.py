# -*- coding: utf-8 -*-
import json
from datetime import datetime

import transaction
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from immunarray.lims.browser.testrun import DuplicateWellSelected, \
    InvalidAssaySelected, ObjectInInvalidState, get_serializeArray_form_values
from immunarray.lims.interfaces import ITestRuns
from immunarray.lims.interfaces.aliquot import IAliquot
from immunarray.lims.interfaces.assayrequest import IAssayRequest
from immunarray.lims.interfaces.clinicalsample import IClinicalSample
from immunarray.lims.interfaces.ichip import IiChip
from immunarray.lims.interfaces.sample import ISample
from immunarray.lims.vocabularies.ichipassay import IChipAssayListVocabulary
from immunarray.lims.vocabularies.users import LabUsersUserVocabulary
from plone.api.content import find, transition
from plone.api.exc import InvalidParameterError


class ViewTestRunView(BrowserView):
    template = ViewPageTemplateFile("templates/testrun_view.pt")

    def __init__(self, context, request):
        BrowserView.__init__(self, context, request)
        self.context = context
        self.request = request
        self.errors = []

    def __call__(self):
        request = self.request

        try:

            if request.form.get('ctest_action', '') == 'save_run':
                self.save_run()
                return json.dumps(
                    {'success': True,
                     'redirect_url': self.context.absolute_url() + '/view'})

        except Exception as e:
            transaction.abort()
            return json.dumps({'success': False, 'message': self.error(e)})

        import pdb, traceback
        from commands import getoutput as go
        go("/usr/bin/play /home/rockfruit/pdb.wav")
        pdb.set_trace()
        pass

        return self.template()

    def error(self, e):
        """Make a nice string from a traceback, to print in the browser
        """
        return "{}: {} ({})".format(e.__class__.__name__, e.__doc__, e.message)

    def render_title(self, uid):
        obj = find(UID=uid)
        if obj:
            return obj[0].Title
        else:
            return ''

    @property
    def assay_name(self):
        """get assay name from the form, or from self.context for edit views
        """
        if 'assay_name' not in self.request \
                and not hasattr(self.context, 'assay_name'):
            return None

        assay_name = self.request.get('assay_name', None)
        if not assay_name and not ITestRuns.providedBy(self.context):
            assay_name = self.context.assay_name
        if not assay_name:
            raise InvalidAssaySelected(self.assay_name)
        return assay_name

    def lab_users(self):
        items = LabUsersUserVocabulary(self).by_value.values()
        return [(i.value, i.title) for i in items]

    def iChipAssayList(self):
        vocab_keys = IChipAssayListVocabulary.__call__(self).by_value.keys()
        return vocab_keys

    def get_assay_solutions(self):
        """Dynamically return a list of possible batches, for each type of
        solution required by the assay
        """
        vocabs = []
        assay = self.get_assay()
        if not assay:
            return vocabs
        for solution_type_name in assay.needed_solutions:
            type_batches = find(Type=solution_type_name,
                                expires={'query': datetime.today().date(),
                                         'range': 'min'},
                                sort_on='expires')

            tmp = []
            for batch in type_batches:
                tmp.append([batch.id,
                            batch.Title,
                            batch.expires.strftime('%Y-%m-%d')])
            vocabs.append([solution_type_name, tmp])
        return vocabs

    def get_assay(self):
        assay_name = self.assay_name
        if assay_name:
            brains = find(portal_type='iChipAssay', Title=assay_name)
            if not brains:
                raise InvalidAssaySelected(self.assay_name)
            return brains[0].getObject()

    def save_run(self):
        """Modify the run located at self.contexet with values entered in
        the testrun_view form.
        """
        values = get_serializeArray_form_values(self.request)

        plates, ichips, aliquots = self.transmogrify_inputs(values['plates'])
        plates = self.remove_empty_plates(plates)
        plates = self.reorder_plates(plates)

        solutions = [values[x] for x in values if x.startswith('solution-')]

        run = self.context
        run.plates = plates
        run.run_date = values.get('run_date', run.run_date)
        run.solutions = solutions

    def transmogrify_inputs(self, plates):
        """Convert titles to UIDs for all ichips and aliquots
        """
        ichips, aliquots = [], []
        for plate in plates:
            for chip_nr in range(1, 5):
                for well_nr in range(1, 9):
                    key = "chip-{}_well-{}".format(chip_nr, well_nr)
                    if plate[key]:
                        brains = find(object_provides=IAliquot.__identifier__,
                                      Title=plate[key])
                        plate[key] = brains[0].UID
                        aliquots.append(brains[0].getObject())
                key = "chip-id-{}".format(chip_nr)
                if plate[key]:
                    brains = find(object_provides=IiChip.__identifier__,
                                  Title=plate[key])
                    plate[key] = brains[0].UID
                    ichips.append(brains[0].getObject())

        return plates, ichips, aliquots

    def reorder_plates(self, plates):
        """Maybe user selected new well numbers for existing plate.
        This changes the order of the plates, and passes them back.
        """
        # Re-order the well-numbers of aliquots according to the "well-number"
        # This allows analyst to re-order wells if aliquots were transposed
        newplates = []
        for plate_nr, plate in enumerate(plates):
            newplate = plate.copy()
            # a list to check for used well numbers, to prevent user from
            # setting the same well-number twice on a plate when re-ordering
            _used_wells = []
            for w_nr in range(1, 9):
                w_nr = str(w_nr)
                nw = plate['well-number-%s' % w_nr]
                if nw in _used_wells:
                    msg = "Well number %s on plate %s" % (nw, plate_nr + 1)
                    raise DuplicateWellSelected(msg)
                _used_wells.append(nw)
                for c_nr in range(1, 5):
                    key = 'chip-%s_well-%s'
                    newplate[key % (c_nr, nw)] = plate[key % (c_nr, w_nr)]
            newplates.append(newplate)
        return newplates

    def remove_empty_plates(self, plates):
        """Remove all plates that don't have (meaningful) values.
        """
        newplates = []
        for plate in plates:
            values = [plate[x] for x in plate.keys()
                      if not x.startswith('well-number-')]
            if any(values):
                newplates.append(plate)
        return newplates

    def transition_plate_contents(self, ichips, aliquots, action_id):
        """Chips, aliquots, and assay requests move together through
        identical states during the test run.
        """
        transitioned = []
        try:
            for ichip in ichips:
                if ichip not in transitioned:
                    transition(ichip, action_id)
                    transitioned.append(ichip)
        except InvalidParameterError:
            # noinspection PyUnboundLocalVariable
            msg = "Can't invoke '%s' transition on %s" % (action_id, ichip)
            raise ObjectInInvalidState(msg)

        try:
            for aliquot in aliquots:
                if aliquot not in transitioned:
                    transition(aliquot, action_id)
                    transitioned.append(aliquot)
        except InvalidParameterError:
            # noinspection PyUnboundLocalVariable
            msg = "Can't invoke '%s' transition on %s" % (action_id, aliquot)
            raise ObjectInInvalidState(msg)

        # get AssayRequests associated with all aliquots, and queue them.
        for aliquot in aliquots:
            sample = self.get_parent_sample_from_aliquot(aliquot)
            if IClinicalSample.providedBy(sample):
                assayrequest = self.get_assay_request_from_sample(sample)
                if assayrequest not in transitioned:
                    transition(assayrequest, action_id)
                    transitioned.append(assayrequest)

    def get_parent_sample_from_aliquot(self, aliquot):
        parent = aliquot.aq_parent
        while not ISample.providedBy(parent):
            parent = parent.aq_parent
        return parent

    def get_assay_request_from_sample(self, sample):
        for child in sample.objectValues():
            if IAssayRequest.providedBy(child):
                return child
