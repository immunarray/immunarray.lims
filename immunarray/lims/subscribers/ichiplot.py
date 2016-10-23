# -*- coding: utf-8 -*-
from bika.lims.permissions import disallow_default_contenttypes
from immunarray.lims.permissions import AddiChip
from plone.api.content import create


def set_ichiplot_permissions(instance):
    """Set default permissions for a new ichiplot
    """
    instance.manage_permission(
        AddiChip, ['Manager', 'LabManager', 'LabClerk', 'Owner'], 0)
    disallow_default_contenttypes(instance)


def set_ichiplot_title(instance):
    """I want the Title to be set from the ichiplotID
    """
    instance.reindexObject(idxs=['Title'])


def create_ichips(instance):
    """I want to create X amount of iChips from form value.
    """

    for x in range(1, instance.nr_ichips + 1):
        ichip = create(container=instance,
                       type='iChip',
                       id="{0}_{1:02d}".format(instance.title, x),
                       title="{0}_{1:02d}".format(instance.title, x))
        # Configure each ichip to reflect the parent's settings
        ichip.frames = instance.frames


def iChipLotAdded(instance, event):
    """iChipLot has been added, some configuration and permissions
    to set on the new folder
    """
    set_ichiplot_permissions(instance)
    set_ichiplot_title(instance)
    create_ichips(instance)
