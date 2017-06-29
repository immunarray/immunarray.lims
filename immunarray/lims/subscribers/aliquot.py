# -*- coding: utf-8 -*-
from immunarray.lims.permissions import AddClinicalAliquot, AddClinicalSample, \
    AddRandDBox, AddRandDAliquot, AddQCAliquot
from bika.lims.permissions import disallow_default_contenttypes
from bika.lims.utils.limsroot import getLims

def ClinicalAliquotAdded(clinicalaliquot, event):
    """A new Clinical Sample has been created!
    """
    clinicalaliquot.manage_permission(AddClinicalAliquot, ['Manager', 'LabManager', 'LabClerk', 'Owner'], 0)
    # Don't allow samples to be nested in each other!
    clinicalaliquot.manage_permission(AddClinicalSample, [], 0)
    clinicalaliquot.manage_permission(AddRandDAliquot, [], 0)
    clinicalaliquot.manage_permission(AddQCAliquot, [], 0)
    disallow_default_contenttypes(clinicalaliquot)


def RandDAliquotAdded(randdaliquot, event):
    randdaliquot.manage_permission(AddRandDAliquot, ['Manager', 'LabManager', 'LabClerk', 'Owner','RandDLabClerk', 'RandDLabManager'], 0)
    # Don't allow samples to be nested in each other!
    randdaliquot.manage_permission(AddClinicalSample, [], 0)
    randdaliquot.manage_permission(AddClinicalAliquot, [], 0)
    randdaliquot.manage_permission(AddQCAliquot, [], 0)
    disallow_default_contenttypes(randdaliquot)


def QCAliquotAdded(qcaliquot, event):
    qcaliquot.manage_permission(AddQCAliquot, ['Manager', 'LabManager', 'LabClerk', 'Owner'], 0)
    # Don't allow samples to be nested in each other!
    qcaliquot.manage_permission(AddClinicalSample, [], 0)
    qcaliquot.manage_permission(AddRandDAliquot, [], 0)
    qcaliquot.manage_permission(AddClinicalAliquot, [], 0)
    disallow_default_contenttypes(qcaliquot)

