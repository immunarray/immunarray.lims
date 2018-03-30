from immunarray.lims.browser.testrun import ObjectInInvalidState
from plone.api.content import find, transition
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


def after_cancel_run(instance):
    """When cancelling a test run, all objects that were linked here must
    be freed for use in a future test run.  This should be logged in this
    test run's attributes, and the widget's view should be printed on the
    testrun's view page.
    """
    action_id = "make_available"
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


def after_abort_run(instance):
    """There are only one type of object supporting abort, and that is the
    Test Run itself.  So, I guess we don't abort any other objects here when
    the run is aborted.
    """
    # XXX: need a way to show aborted links in the UI



def get_object(uid):
    brains = find(UID=uid)
    if brains:
        return brains[0].getObject()
