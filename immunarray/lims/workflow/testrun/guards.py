from immunarray.lims.interfaces import testrrun

def guard_queue(instance):
    """
    """
    return True


def guard_begin_process(instance):
    """
    if testrun.solutions(instance):
        return False
    """
    return True


def guard_result(instance):
    """
    """
    return True


def guard_report(instance):
    """
    """
    return True


def guard_wet_work_done(instance):
    """
    """
    return True


def guard_scanning(instance):
    """
    """
    return True


def guard_abort_run(instance):
    """
    """
    return True


def guard_cancel_run(instance):
    """
    """
    return True
