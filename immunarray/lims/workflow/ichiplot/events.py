from plone.api.content import transition, get_state


def after_release(instance):
    """
    """
    for ichip in instance.objectValues():
        if get_state(ichip) == "quarantined":
            transition(ichip, "release")


def after_quarantine(instance):
    """
    """
    for ichip in instance.objectValues():
        if get_state(ichip) == "released":
            transition(ichip, "quarantine")


def after_close(instance):
    """
    """
    pass
