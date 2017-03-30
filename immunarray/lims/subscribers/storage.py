# -*- coding: utf-8 -*-
from bika.lims.permissions import disallow_default_contenttypes
from immunarray.lims.permissions import AddCommercialBox
from immunarray.lims.permissions import AddRandDBox
from immunarray.lims.permissions import AddRack
from bika.lims.permissions import AddAliquot


def RackAdded(instance, event):
    """A new Rack has been created!
    """

    # Permit Commercial Boxes to be added here
    instance.manage_permission(AddCommercialBox, ['Manager', 'LabManager', 'LabClerk', 'Owner'], 0)
    instance.manage_permission(AddRandDBox, ['Manager', 'LabManager', 'RandDLabClerk', 'RandDLabManager', 'Owner'], 0)
    # Prevent adding Rack in a rack!
    instance.manage_permission(AddRack, [], 0)

    disallow_default_contenttypes(instance)

def CommercialBoxAdded(instance, event):
    """a new box has been created
    """
    # Permit Aliqutos to be added here
    instance.manage_permission(AddAliquot,['Manager', 'LabManager', 'LabClerk', 'Owner'], 0)
    # Prevent adding box in a box
    instance.manage_permission(AddCommercialBox, [], 0)
    instance.manage_permission(AddRandDBox, [],0)

    disallow_default_contenttypes(instance)

def RandDBoxAdded(instance, event):
    """a new box has been created
    """
    # Permit Aliqutos to be added here
    instance.manage_permission(AddAliquot,['Manager', 'LabManager', 'LabClerk', 'Owner'], 0)
    # Prevent adding box in a box
    instance.manage_permission(AddCommercialBox, [], 0)
    instance.manage_permission(AddRandDBox, [],0)

    disallow_default_contenttypes(instance)
