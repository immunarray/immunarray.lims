# -*- coding: utf-8 -*-
from AccessControl.Permissions import copy_or_move, delete_objects
from bika.lims.permissions import disallow_default_contenttypes
from immunarray.lims.permissions import AddAssayBillingRequest, AddAssayRequest, \
    AddNCE, AddClinicalAliquot


def AssayBillingRequest(assaybillingrequest, event):
    """A new assay billing request been created!
    """
    assaybillingrequest.manage_permission(delete_objects, [], 0)
    assaybillingrequest.manage_permission(AddNCE, ['LabManager', 'LabClerk','BillingExec'], 0)
    # Don't allow assay request to be nested in each other!
    assaybillingrequest.manage_permission(AddAssayRequest, [], 0)
    assaybillingrequest.manage_permission(AddClinicalAliquot, [], 0)
    assaybillingrequest.manage_permission(AddAssayBillingRequest, [], 0)

    disallow_default_contenttypes(assaybillingrequest)
