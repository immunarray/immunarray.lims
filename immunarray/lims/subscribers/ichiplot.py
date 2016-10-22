# -*- coding: utf-8 -*-
from immunarray.lims.permissions import AddiChip
from bika.lims.permissions import disallow_default_contenttypes

def iChipLotAdded(instance, event):
    """iChipLot has been added, some configuration and permissions
    to set on the new folder
    """
    instance.manage_permission(
        AddiChip, ['Manager', 'LabManager', 'LabClerk', 'Owner'], 0)
    disallow_default_contenttypes(instance)

    # I want the Title to be set from the ichiplot ID
    instance.title = instance.ichiplotID
    instance.reindexObject(idxs=['Title'])
