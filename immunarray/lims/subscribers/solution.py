# -*- coding: utf-8 -*-
from immunarray.lims.permissions import AddClinicalAliquot, AddClinicalSample, \
    AddRandDSample, AddRandDAliquot, AddQCAliquot, AddQCSample
from bika.lims.permissions import disallow_default_contenttypes
from bika.lims.utils.limsroot import getLims

def SolutionAdded(clinicalaliquot, event):
    """A new Solution Type has been added!
    """
    clinicalaliquot.manage_permission(AddClinicalAliquot, ['Manager', 'LabManager', 'LabClerk', 'Owner'], 0)
    # Don't allow samples to be nested in each other!
    clinicalaliquot.manage_permission(AddQCSample, [], 0)
    clinicalaliquot.manage_permission(AddRandDSample, [], 0)
    clinicalaliquot.manage_permission(AddClinicalSample, [], 0)
    # Don't allow other aliquots to be added (only R&D Aliquots should be added)
    clinicalaliquot.manage_permission(AddRandDAliquot, [], 0)
    clinicalaliquot.manage_permission(AddQCAliquot, [], 0)
    disallow_default_contenttypes(clinicalaliquot)

