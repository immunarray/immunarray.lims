# -*- coding: utf-8 -*-
from AccessControl.Permissions import copy_or_move, delete_objects
from bika.lims.permissions import disallow_default_contenttypes
from immunarray.lims.permissions import AddAssayBillingRequest, AddAssayRequest, \
    AddNCE, AddClinicalAliquot


def AssayRequest(assayrequest, event):
    """A new assay request been created!
    """
    assayrequest.manage_permission(copy_or_move, [], 0)
    assayrequest.manage_permission(delete_objects, [], 0)
    assayrequest.manage_permission(AddAssayBillingRequest, ['LabManager', 'BillingExec'], 0)
    assayrequest.manage_permission(AddNCE, ['LabManager', 'BillingExec', 'LabClerk'], 0)
    # Don't allow assay request to be nested in each other!
    assayrequest.manage_permission(AddAssayRequest, [], 0)
    assayrequest.manage_permission(AddClinicalAliquot, [], 0)

    disallow_default_contenttypes(assayrequest)
