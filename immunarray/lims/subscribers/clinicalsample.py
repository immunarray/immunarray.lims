# -*- coding: utf-8 -*-
from immunarray.lims.permissions import AddClinicalAliquot, AddClinicalSample, AddRandDBox
from bika.lims.permissions import disallow_default_contenttypes, AddAliquot
from bika.lims.utils.limsroot import getLims

def ClinicalSampleAdded(clinicalsample, event):
    """A new Clinical Sample has been created!
    """
    clinicalsample.manage_permission(AddClinicalAliquot, ['Manager', 'LabManager', 'LabClerk', 'Owner'], 0)
    clinicalsample.manage_permission(AddClinicalSample, [], 0)
    import pdb;pdb.set_trace()
    # Don't allow samples to be nested in each other!
    disallow_default_contenttypes(clinicalsample)


def RandDSampleAdded(randdsample, event):
    randdsample.manage_permission
    disallow_default_contenttypes(randdsample)
    pass


def QCSampleAdded(qcsample, event):
    qcsample.manage_permission
    disallow_default_contenttypes(qcsample)
    pass

