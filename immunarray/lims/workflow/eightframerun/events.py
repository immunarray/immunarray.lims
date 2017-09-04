from immunarray.lims.browser.analysisrequest.commercial_run import \
    ObjectInInvalidState
from immunarray.lims.interfaces.clinicalsample import IClinicalSample
from plone.api.content import transition, get_state
from plone.api.exc import InvalidParameterError


def after_queue(instance):
    """
    """


def after_in_process(instance):
    """
    """


def after_result(instance):
    """
    """


def after_report(instance):
    """
    """


def after_wet_work_done(instance):
    """
    """


def after_scanning(instance):
    """
    """


def after_abort_run(instance):
    """
    """


def after_cancel_run(instance):
    """
    """
    action_id = "available"
    try:
        for ichip in instance.objectValues():
            if get_state(ichip) == "in_queue":
                transition(ichip, action_id)

    except InvalidParameterError:  # noinspection PyUnboundLocalVariable
        msg = "Can't invoke '%s' transition on %s" % (action_id, ichip)

        raise ObjectInInvalidState(msg)

    try:
        for aliquot in aliquots:
            if get_state(aliquot) == "in_queue":
                transition(aliquot, action_id)

    except InvalidParameterError:  # noinspection PyUnboundLocalVariable
        msg = "Can't invoke '%s' transition on %s" % (action_id, aliquot)
        raise ObjectInInvalidState(msg)

    sample = instance.get_parent_sample_from_aliquot(aliquot)
    if IClinicalSample.providedBy(sample):
        assayrequest = instance.get_assay_request_from_sample(sample)
        if assayrequest == "in_queue":
            transition(assayrequest, action_id)
