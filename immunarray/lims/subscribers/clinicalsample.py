# -*- coding: utf-8 -*-
from immunarray.lims.permissions import AddClinicalAliquot
from immunarray.lims.permissions import AddClinicalSample
from bika.lims.permissions import disallow_default_contenttypes
from bika.lims.utils.limsroot import getLims

def ClinicalSampleAdded(instance, event):
    """A new Clinical Sample has been created!
    """
    mp = instance.manage_permission
    mp(AddClinicalAliquot, ['Manager', 'LabManager', 'LabClerk', 'Owner'], 0)
    # Don't allow samples to be nested in each other!
    # mp(AddClinicalSample, [], 0)
    disallow_default_contenttypes(instance)


def RandDSampleAdded(instance, event):
    mp = instance.manage_permission
    disallow_default_contenttypes(instance)
    pass


def QCSampleAdded(instance, event):
    mp = instance.manage_permission
    disallow_default_contenttypes(instance)
    pass

