# -*- coding: utf-8 -*-
from immunarray.lims.interfaces.assayrequest import IAssayRequest
from immunarray.lims.interfaces.clinicalsample import IClinicalSample
from immunarray.lims.interfaces.sample import ISample
from plone.api.content import transition
from plone.api.exc import InvalidParameterError
from plone.api.portal import get_tool

class InvalidAliquotIdentifier(Exception):
    """Value of Aliquot (title?) entered in ctest form
    cannot be resolved to an aliquot in the sytem
    """

class InvalidAssaySelected(Exception):
    """Selected iChip Assay not found
    """


class NoIchipLotsFound(Exception):
    """No iChipLots Found
    """


class NotEnoughUniqueIChipLots(Exception):
    """Not enough unique iChipLots found
    """


class QCSampleNotFound(Exception):
    """QC Sample not found
    """


class QCAliquotNotFound(Exception):
    """Available QC Aliquots meeting assay parameters not found
    """


class NoWorkingAliquotsFound(Exception):
    """No working aliquots found
    """


class ObjectInInvalidState(Exception):
    """At least one object is in an invalid state!  Re-create the run
    """


class DuplicateWellSelected(Exception):
    """You cannot use the same well number twice on a single plate
    """


class InvalidSample(Exception):
    """The sample is not Clinical, HQC, or LQC, so we cannot use it
    """


class MissingIChipForSlide(Exception):
    """The IChip ID is invalid, or blank, but aliquots exist
    """


def get_serializeArray_form_values(request):
    """Parse the form_values list into a single dictionary.
    The plates are taken care of particularly, like this:

    {'thing1': 'value1',
     'thing2': 'value2'...
     'plates': [
         {plate1-stuff}, 
         {plate2-stuff}
     ]
    }
    """
    raw = request.form
    count = len([x for x in raw if 'form_values' in x])

    # gather intermediate data dictionary
    intermediate = {}
    for x in range(0, count / 2):
        name = raw['form_values[%s][name]' % x]
        value = raw['form_values[%s][value]' % x]
        if name in intermediate:
            if type(intermediate[name]) == list:
                intermediate[name].append(value)
            else:
                intermediate[name] = [intermediate[name], value]
        else:
            intermediate[name] = value

    # The count of 'well-number-1' decides how many plates were submitted.
    nr_plates = len(intermediate['well-number-1'])

    # Separate the plates from the rest of the form values, and convert
    # them to a single list of dictionaries. any key in the form who's
    # name starts with one plate_keys, will be included in the "plates"
    # element of the returned list
    plate_keys = ['chip-', 'comments', 'scan-slot', 'well-number']
    plates = [{}] * nr_plates
    form_values = {}
    for k, v in intermediate.items():
        if any([k.startswith(pk) for pk in plate_keys]):
            if not isinstance(v, (list, tuple)):
                v = [v]
            for nr in range(nr_plates):
                plates[nr][k] = v[nr]

        else:
            form_values[k] = v

    form_values['plates'] = plates
    return form_values


def transition_plate_contents(ichips, aliquots, action_id):
    """Chips, aliquots, and assay requests move together through
    identical states during the test run.

    This function is made use of wherever plate contents must be moved
    together through some state.
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
        sample = get_parent_sample_from_aliquot(aliquot)
        if IClinicalSample.providedBy(sample):
            assayrequest = get_assay_request_from_sample(sample)
            wf = get_tool('portal_workflow')
            t_ids = [t['id'] for t in wf.getTransitionsFor(assayrequest)]
            if action_id in t_ids \
                    and assayrequest not in transitioned:
                transition(assayrequest, action_id)
                transitioned.append(assayrequest)


def get_parent_sample_from_aliquot(aliquot):
    parent = aliquot.aq_parent
    while not ISample.providedBy(parent):
        parent = parent.aq_parent
    return parent


def get_assay_request_from_sample(sample):
    for child in sample.objectValues():
        if IAssayRequest.providedBy(child):
            return child
