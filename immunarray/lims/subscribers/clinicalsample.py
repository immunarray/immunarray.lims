# -*- coding: utf-8 -*-
from immunarray.lims.permissions import AddClinicalAliquot
from bika.lims.permissions import disallow_default_contenttypes


def ClinicalSampleAdded(instance, event):
    """A new Clinical Sample has been created!
    """
    instance.manage_permission(AddClinicalAliquot, ['Manager', 'LabManager', 'LabClerk', 'Owner'], 0)
    disallow_default_contenttypes(instance)
