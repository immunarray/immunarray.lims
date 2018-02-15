from immunarray.lims.interfaces import eightframerun

def gurard_queue(instance):
    """
    """
    return True


def gurard_in_process(instance):
    """
    if eightframerun.solutions(instance):
        return False
    """
    return True


def gurard_result(instance):
    """
    """
    return True


def gurard_report(instance):
    """
    """
    return True


def gurard_wet_work_done(instance):
    """
    """
    return True


def gurard_scanning(instance):
    """
    """
    return True


def gurard_abort_run(instance):
    """
    """
    return True


def gurard_cancel_run(instance):
    """
    """
    return True
