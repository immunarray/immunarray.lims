def guard_release(instance):
    """
    """
    if not all([instance.temp_log,
                instance.cofa,
                instance.batch_release,
                instance.gal_file]):
        return False

    return True


def guard_quarantine(instance):
    """
    """
    return True


def guard_close(instance):
    """
    """
    return True
