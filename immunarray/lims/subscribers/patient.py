# -*- coding: utf-8 -*-
from immunarray.lims.permissions import AddPatient
from plone import api
from bika.lims.permissions import disallow_default_contenttypes

def MakePatient(self, pt, dob, marital_status, gender,
                          ssn, mrn, consent_acquired, ethnicity):
    #set permission for new patient record
    pt.manage_permission(
        AddPatient, ['Manager', 'LabManager', 'LabClerk', 'Owner'], 0)
    disallow_default_contenttypes(pt)

    patient = api.content.create(container=pt,
                                 type = 'Patient',
                                 dob = dob,
                                 marital_status = marital_status,
                                 gender = gender,
                                 ssn = ssn,
                                 medical_record_number = mrn,
                                 research_consent = consent_acquired,
                                 race = ethnicity,
                                 )
