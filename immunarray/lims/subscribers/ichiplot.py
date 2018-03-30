# -*- coding: utf-8 -*-
from AccessControl.Permissions import copy_or_move, delete_objects
from bika.lims.permissions import disallow_default_contenttypes
from immunarray.lims.permissions import AddiChip
from plone.api.content import create


def iChipLotAdded(instance, event):
    """iChipLot has been added, some configuration and permissions
    to set on the new folder
    """

    # Set default permissions for a new ichiplot
    instance.manage_permission(copy_or_move, [], 0)
    instance.manage_permission(delete_objects, [], 0)
    instance.manage_permission(AddiChip, ['LabManager', 'LabClerk'], 0)
    disallow_default_contenttypes(instance)

    # I want to create X amount of iChips from form value.
    for x in range(1, instance.nr_ichips + 1):
        ichip = create(container=instance,
                       title = "{0}_{1:03d}".format(instance.title, x),
                       type='iChip',
                       ichip_id="{0}_{1:03d}".format(instance.title, x))
        # Configure each ichip to reflect the parent's settings
        ichip.frames = instance.frames
