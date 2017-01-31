# -*- coding: utf-8 -*-
from bika.lims.permissions import disallow_default_contenttypes
from immunarray.lims.permissions import AddBox


def RackAdded(instance, event):
    """a new Rack has been created!
    """

    # Permit Boxes to be added here
    instance.manage_permission(AddBox, ['Manager', 'LabManager', 'LabClerk', 'Owner'], 0)

    disallow_default_contenttypes(instance)

