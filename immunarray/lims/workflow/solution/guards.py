from datetime import datetime

def guard_quarantine(instance):
    """
    """
    return True


def guard_release(instance):
    """
    """
    return True


def guard_put_in_use(instance):
    """
    """
    if instance.expiration_date < datetime.today().date():
        return False
    return True


def guard_close(instance):
    """
    """
    return True
