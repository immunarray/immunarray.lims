from plone.api.content import get_state


def guard_broken(instance):
    """
    """
    return True


def guard_discard(instance):
    """
    """
    return True


def guard_expire(instance):
    """
    """
    return True


def guard_expired(instance):
    """
    """
    return True


def guard_begin_process(instance):
    """
    """
    return True


def guard_queue(instance):
    """
    """
    return True


def guard_reject(instance):
    """
    """
    return True


def guard_release(instance):
    """
    """
    if get_state(instance.aq_parent) != "released":
        return False
    return True


def guard_cancel_run(instance):
    """
    """
    return True


def guard_reserve_for_stability_testing(instance):
    """
    """
    return True


def guard_residual(instance):
    """
    """
    return True


def guard_retain_ial(instance):
    """
    """
    return True


def guard_retain_usa(instance):
    """
    """
    return True


def guard_use_for_release_testing(instance):
    """
    """
    return True


def guard_use_for_stability_testing(instance):
    """
    """
    return True


def guard_use_for_training(instance):
    """
    """
    return True


def guard_use_for_validation(instance):
    """
    """
    return True


def guard_qc_fail(instance):
    """
    """
    return True


def guard_qc_pass(instance):
    """
    """
    return True


def guard_quarantine(instance):
    """
    """
    return True
