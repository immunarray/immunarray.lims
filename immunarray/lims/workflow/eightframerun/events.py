from immunarray.lims.browser.analysisrequest.commercial_run import \
    ObjectInInvalidState
from plone.api.content import transition, find
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


def get_object(uid):
    brains = find(UID=uid)
    if brains:
        return brains[0].getObject()


def after_cancel_run(instance):
    """
    """
    action_id = "available"
    transitioned = []
    try:
        for plate in instance.plates:
            for key, value in plate.items():
                if value in transitioned:
                    continue
                transitioned.append(value)
                obj = get_object(value)
                if obj:
                    transition(obj, action_id)
    except InvalidParameterError:  # noinspection PyUnboundLocalVariable
        msg = "Can't invoke '%s' transition on %s" % (action_id, obj)
        raise ObjectInInvalidState(msg)
