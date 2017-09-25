from immunarray.lims.interfaces import IBulkAliquot
from plone.api.content import get_state


def guard_make_available(instance):
    """
    """
    if IBulkAliquot.providedBy(instance):
        return False
    if get_state(instance.aq_parent) == 'in_review':
        return False
    return True


def guard_queue(instance):
    """
    """
    if IBulkAliquot.providedBy(instance):
        return False
    return True


def guard_begin_process(instance):
    """
    """
    if IBulkAliquot.providedBy(instance):
        return False
    return True


def guard_pass(instance):
    """
    """
    if IBulkAliquot.providedBy(instance):
        return False
    return True


def guard_fail(instance):
    """
    """
    if IBulkAliquot.providedBy(instance):
        return False
    return True

def guard_throw_away(instance):
    """
    """
    return True
