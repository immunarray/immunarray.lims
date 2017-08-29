from immunarray.lims.interfaces import IBulkAliquot


def guard_make_available(instance):
    """
    """
    if IBulkAliquot.providedBy(instance):
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
