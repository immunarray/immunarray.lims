# -*- coding: utf-8 -*-
from bika.lims.permissions import disallow_default_contenttypes
from immunarray.lims.permissions import AddAssayBillingRequest, AddAssayRequest


def AssayRequest(assayrequest, event):
    """A new assay request been created!
    """
    assayrequest.manage_permission(AddAssayBillingRequest, ['LabManager', 'BillingExec'], 0)
    # Don't allow assay request to be nested in each other!
    assayrequest.manage_permission(AddAssayRequest, [], 0)
    disallow_default_contenttypes(assayrequest)
