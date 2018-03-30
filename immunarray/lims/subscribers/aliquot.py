# -*- coding: utf-8 -*-
from AccessControl.Permissions import copy_or_move, delete_objects
from immunarray.lims.permissions import AddClinicalAliquot, AddClinicalSample, \
    AddRandDSample, AddRandDAliquot, AddQCAliquot, AddQCSample
from bika.lims.permissions import disallow_default_contenttypes
from bika.lims.utils.limsroot import getLims

def ClinicalAliquotAdded(clinicalaliquot, event):
    """A new Clinical Sample has been created!
    """
    clinicalaliquot.manage_permission(copy_or_move, [], 0)
    clinicalaliquot.manage_permission(delete_objects, [], 0)
    clinicalaliquot.manage_permission(AddClinicalAliquot, ['Manager', 'LabManager', 'LabClerk', 'Owner'], 0)
    # Don't allow samples to be nested in each other!
    clinicalaliquot.manage_permission(AddQCSample, [], 0)
    clinicalaliquot.manage_permission(AddRandDSample, [], 0)
    clinicalaliquot.manage_permission(AddClinicalSample, [], 0)
    # Don't allow other aliquots to be added (only R&D Aliquots should be added)
    clinicalaliquot.manage_permission(AddRandDAliquot, [], 0)
    clinicalaliquot.manage_permission(AddQCAliquot, [], 0)
    disallow_default_contenttypes(clinicalaliquot)


def RandDAliquotAdded(randdaliquot, event):
    randdaliquot.manage_permission(AddRandDAliquot, ['Manager', 'LabManager', 'LabClerk', 'Owner','RandDLabClerk', 'RandDLabManager'], 0)
    # Don't allow samples to be nested in each other!
    randdaliquot.manage_permission(AddClinicalSample, [], 0)
    randdaliquot.manage_permission(AddRandDSample, [], 0)
    randdaliquot.manage_permission(AddQCSample, [], 0)
    # Don't allow other aliquots to be added (only R&D Aliquots should be added)
    randdaliquot.manage_permission(AddClinicalAliquot, [], 0)
    randdaliquot.manage_permission(AddQCAliquot, [], 0)
    disallow_default_contenttypes(randdaliquot)


def QCAliquotAdded(qcaliquot, event):

    qcaliquot.manage_permission(AddQCAliquot, ['Manager', 'LabManager', 'LabClerk', 'Owner'], 0)
    # Don't allow samples to be nested in each other!
    qcaliquot.manage_permission(AddRandDSample, [], 0)
    qcaliquot.manage_permission(AddQCSample, [], 0)
    qcaliquot.manage_permission(AddClinicalSample, [], 0)
    # Don't allow other aliquots to be added (only QC Aliquots should be added)
    qcaliquot.manage_permission(AddClinicalAliquot, [], 0)
    qcaliquot.manage_permission(AddRandDAliquot, [], 0)
    disallow_default_contenttypes(qcaliquot)
