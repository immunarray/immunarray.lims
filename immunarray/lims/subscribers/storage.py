# -*- coding: utf-8 -*-
from bika.lims.permissions import AddAliquot
from bika.lims.permissions import disallow_default_contenttypes
from immunarray.lims.permissions import AddCommercialBox, AddRack, AddRandDBox, \
    AddQCBox


def RackAdded(instance, event):
    """A new Rack has been created!
    """

    # Permit Commercial Boxes to be added here
    instance.manage_permission(
        AddCommercialBox,
        ['Manager', 'LabManager', 'LabClerk', 'Owner'],
        0)
    instance.manage_permission(
        AddRandDBox,
        ['Manager', 'LabManager', 'RandDLabClerk', 'RandDLabManager', 'Owner'],
        0)
    instance.manage_permission(
        AddQCBox,
        ['Manager', 'LabManager', 'RandDLabClerk', 'RandDLabManager', 'Owner'],
        0)
    # Prevent adding Rack in a rack!
    instance.manage_permission(AddRack, [], 0)

    disallow_default_contenttypes(instance)


def CommercialBoxAdded(instance, event):
    """A new  commercial box has been created
    """
    # Permit Aliquots to be added here
    instance.manage_permission(AddAliquot, [], 0)
    # Prevent adding box in a box
    instance.manage_permission(AddCommercialBox, [], 0)
    instance.manage_permission(AddRandDBox, [], 0)
    instance.manage_permission(AddQCBox, [], 0)

    disallow_default_contenttypes(instance)
    # name box
    instance.setTitle("%s - %s - %s" % (instance.box_number, instance.box_type, instance.Type()))
    # reindex for title to work
    instance.reindexObject(idxs= ['Title','sortable_title','title'])


def RandDBoxAdded(instance, event):
    """A new RandD box has been created
    """
    # Permit Aliqutos to be added here
    instance.manage_permission(AddAliquot, [], 0)
    # Prevent adding box in a box
    instance.manage_permission(AddCommercialBox, [], 0)
    instance.manage_permission(AddRandDBox, [], 0)
    instance.manage_permission(AddQCBox, [], 0)

    disallow_default_contenttypes(instance)

    # name box
    instance.setTitle("%s - %s - %s" % (instance.box_number, instance.box_type, instance.Type()))
    # reindex for title to work
    instance.reindexObject(idxs= ['Title','sortable_title','title'])


def QCBoxAdded(instance, event):
    """A new QC box has been created
    """
    # Permit Aliqutos to be added here
    instance.manage_permission(AddAliquot, [], 0)
    # Prevent adding box in a box
    instance.manage_permission(AddCommercialBox, [], 0)
    instance.manage_permission(AddRandDBox, [], 0)
    instance.manage_permission(AddQCBox, [], 0)


    disallow_default_contenttypes(instance)

    # name box
    instance.setTitle("%s - %s - %s" % (instance.box_number, instance.box_type, instance.Type()))
    # reindex for title to work
    instance.reindexObject(idxs= ['Title','sortable_title','title'])
