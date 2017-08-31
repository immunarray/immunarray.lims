# -*- coding: utf-8 -*-
from immunarray.lims.permissions import AddClinicalAliquot, AddClinicalSample, \
    AddRandDSample, AddRandDAliquot, AddQCAliquot, AddQCSample, AddNCE,AddAssayRequest,AddAssayBillingRequest
from bika.lims.permissions import disallow_default_contenttypes
from bika.lims.utils.limsroot import getLims

def ClinicalSampleAdded(clinicalsample, event):
    """A new Clinical Sample has been created!
    """
    clinicalsample.manage_permission(AddClinicalAliquot, ['LabManager', 'LabClerk'], 0)
    clinicalsample.manage_permission(AddAssayRequest, ['LabManager', 'LabClerk'], 0)
    clinicalsample.manage_permission(AddNCE, ['LabManager', 'LabClerk'], 0)
    # Don't allow samples to be nested in each other!
    clinicalsample.manage_permission(AddQCSample, [], 0)
    clinicalsample.manage_permission(AddRandDSample, [], 0)
    clinicalsample.manage_permission(AddClinicalSample, [], 0)
    # Don't allow other aliquots to be added (only R&D Aliquots should be added)
    clinicalsample.manage_permission(AddRandDAliquot, [], 0)
    clinicalsample.manage_permission(AddQCAliquot, [], 0)
    disallow_default_contenttypes(clinicalsample)


def RandDSampleAdded(randdsample, event):
    randdsample.manage_permission(AddRandDAliquot, ['LabManager', 'LabClerk','RandDLabClerk', 'RandDLabManager'], 0)
    randdsample.manage_permission(AddAssayRequest, ['LabManager', 'LabClerk','RandDLabClerk', 'RandDLabManager'], 0)
    randdsample.manage_permission(AddNCE, ['LabManager', 'LabClerk','RandDLabClerk', 'RandDLabManager'], 0)
    # Don't allow samples to be nested in each other!
    randdsample.manage_permission(AddClinicalSample, [], 0)
    randdsample.manage_permission(AddRandDSample, [], 0)
    randdsample.manage_permission(AddQCSample, [], 0)
    # Don't allow other aliquots to be added (only R&D Aliquots should be added)
    randdsample.manage_permission(AddClinicalAliquot, [], 0)
    randdsample.manage_permission(AddQCAliquot, [], 0)
    disallow_default_contenttypes(randdsample)



def QCSampleAdded(qcsample, event):
    qcsample.manage_permission(AddQCAliquot, ['LabManager', 'LabClerk'], 0)
    qcsample.manage_permission(AddAssayRequest, ['LabManager', 'LabClerk'], 0)
    qcsample.manage_permission(AddNCE, ['LabManager', 'LabClerk'], 0)
    # Don't allow samples to be nested in each other!
    qcsample.manage_permission(AddRandDSample, [], 0)
    qcsample.manage_permission(AddQCSample, [], 0)
    qcsample.manage_permission(AddClinicalSample, [], 0)
    # Don't allow other aliquots to be added (only QC Aliquots should be added)
    qcsample.manage_permission(AddClinicalAliquot, [], 0)
    qcsample.manage_permission(AddRandDAliquot, [], 0)
    disallow_default_contenttypes(qcsample)

