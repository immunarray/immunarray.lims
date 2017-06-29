# -*- coding: utf-8 -*-
from immunarray.lims.permissions import AddClinicalAliquot, AddClinicalSample, \
    AddRandDBox, AddRandDAliquot, AddQCAliquot
from bika.lims.permissions import disallow_default_contenttypes
from bika.lims.utils.limsroot import getLims

def ClinicalSampleAdded(clinicalsample, event):
    """A new Clinical Sample has been created!
    """
    clinicalsample.manage_permission(AddClinicalAliquot, ['Manager', 'LabManager', 'LabClerk', 'Owner'], 0)
    # Don't allow samples to be nested in each other!
    clinicalsample.manage_permission(AddClinicalSample, [], 0)
    clinicalsample.manage_permission(AddRandDAliquot, [], 0)
    clinicalsample.manage_permission(AddQCAliquot, [], 0)
    disallow_default_contenttypes(clinicalsample)


def RandDSampleAdded(randdsample, event):
    randdsample.manage_permission(AddRandDAliquot, ['Manager', 'LabManager', 'RandDLabClerk', 'RandDLabManager', 'LabClerk', 'Owner'], 0)
    disallow_default_contenttypes(randdsample)



def QCSampleAdded(qcsample, event):
    qcsample.manage_permission(AddQCAliquot, ['Manager', 'LabManager', 'LabClerk', 'Owner'], 0)
    disallow_default_contenttypes(qcsample)

