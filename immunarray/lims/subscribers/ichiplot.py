# -*- coding: utf-8 -*-
from immunarray.lims.permissions import AddiChip


def iChipLotAdded(instance, event):
    """iChipLot has been added, some permissions to set on the new folder
    """
    instance.manage_permission(
        AddiChip, ['Manager', 'LabManager', 'LabClerk', 'Owner'], 0)
