# -*- coding: utf-8 -*-
"""Permission should be duplicated in permissions.py and permissions.zcml
"""
from AccessControl.Permissions import copy_or_move, delete_objects


def setup_default_permissions(portal):

    # NOT in portal.lims do we want delete permission
    mp = portal.lims.manage_permission
    mp(delete_objects, [], 0)

    mp = portal.manage_permission
    mp(AddMaterial, [], 0)
    mp(AddSolution, [], 0)
    mp(AddiChipLot, [], 0)
    mp(AddiChip, [], 0)
    mp(AddTestRun, [], 0)
    mp(AddPlate, [], 0)
    mp(AddNCE, [], 0)
    mp(AddPatient, [], 0)
    mp(AddProvider, [], 0)
    mp(AddClinicalSample, [], 0)
    mp(AddClinicalAliquot, [], 0)
    mp(AddRandDSample, [], 0)
    mp(AddRandDAliquot, [], 0)
    mp(AddQCSample, [], 0)
    mp(AddQCAliquot, [], 0)
    mp(AddiChipAssay, [], 0)
    mp(AddCustomerServiceCall, [], 0)
    mp(AddFreezer, [], 0)
    mp(AddShelf, [], 0)
    mp(AddRack, [], 0)
    mp(AddRandDBox, [], 0)
    mp(AddQCBox, [], 0)
    mp(AddCommercialBox, [], 0)
    mp(AddSite, [], 0)
    mp(AddAssayBillingRequest, [], 0)
    mp(AddAssayRequest, [], 0)
    mp(AddBillingProgram, [], 0)
    mp(AddAliquotPlate, [], 0)


AddClinicalAliquot = "LIMS: Add Clinical Aliquot"
AddClinicalSample = "LIMS: Add Clinical Sample"
AddCommercialBox = "LIMS: Add Commercial Box"
AddCustomerServiceCall = "LIMS: Add Customer Service Call"
AddFreezer = "LIMS: Add Freezer"
AddiChip = "LIMS: Add iChip"
AddiChipAssay = "LIMS: Add iChip Assay"
AddiChipLot = "LIMS: Add iChip Lot"
AddMaterial = "LIMS: Add Material"
AddNCE = "LIMS: Add NCE"
AddPatient = "LIMS: Add Patient"
AddPlate = "LIMS: Add Plate"
AddProvider = "LIMS: Add Provider"
AddQCAliquot = "LIMS: Add Quality Control Aliquot"
AddQCSample = "LIMS: Add Quality Control Sample"
AddRack = "LIMS: Add Rack"
AddRandDAliquot = "LIMS: Add Research and Development Aliquot"
AddRandDBox = "LIMS: Add RandD Box"
AddQCBox = "LIMS: Add QC Box"
AddRandDSample = "LIMS: Add Research and Development Sample"
AddShelf = "LIMS: Add Shelf"
AddSite = "LIMS: Add Site"
AddSolution = "LIMS: Add Solution"
AddTestRun = "LIMS: Add Test Run"
AddVeracisRunBase = "LIMS: Add Veracis Run Base"
AddAssayRequest = "LIMS: Add Assay Request"
AddAssayBillingRequest = "Billing: Add Assay Billing Request"
AddBillingProgram = "Billing: Add Billing Program"
AddAliquotPlate = "LIMS: Add Aliquot Plate"
