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


def guard_resulted(instance):
    """This action can only be taken by the importer; so we need a guard
    here to be sure that an attribute is set (by the importer), to prevent
    manually shifting to "resulted" state and bypassing the importer.
    """
    return getattr(instance, "import_log", False)


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
