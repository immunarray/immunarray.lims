# -*- coding: utf-8 -*-
from datetime import date

from immunarray.lims import messageFactory as _
from immunarray.lims.interfaces.sample import ISample
from immunarray.lims.vocabularies.ichipassay import IChipAssayListVocabulary
from plone.autoform import directives as form
from plone.autoform.interfaces import IFormFieldProvider
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from zope import schema
from zope.interface import alsoProvides


class IClinicalSample(ISample):
    """Sample that will contain all the billing info and high level information
    that is applicable to all aliquots made from this material, location of
    tests ordered on sample
    """
    title = schema.TextLine(
        title=_(u"Unique Sample Number"),
        description=_(u"Sample ID from the blood draw kit"),
        required=False,
    )

    # want to index this field
    sample_serial_number = schema.Int(
        title=_(u"Sample Serial Number"),
        description=_(u"Sample Serial Number"),
        required=False,
    )
    """ Want to do an n+1 but allow be edited, should be unique"""

    # list or tuple? JP 3-14-17, let this be blank for remote order
    # option at a later date, need test ordered and status!
    # use this to drive a setup handler that will make the lists of what should
    # be tested! (jp 4-11-17)

    research_consent = schema.Choice(
        title=_(u"Patient Consent to Research"),
        description=_(u"Patient Gives consent to research use"),
        values=[_(u'No'), _(u'Yes')],
        required=True,
    )

    front_end_qa = schema.Choice(
        title=_(u"Front End QA Status"),
        description=_(u"Front End QA Status"),
        required=False,
        values=[_(u"Initial"),
                _(u"Review Pass"),
                _(u"Held"), ],
    )
    
    sample_ordering_healthcare_provider = schema.TextLine(
        title=_(u"Ordering Healthcare Provider"),
        description=_(u"Ordering Healthcare Provider"),
        required=False,
    )

    sample_ordering_healthcare_provider_signature = schema.Bool(
        title=_(u"Ordering Healthcare Provider Signature Provided"),
        description=_(u"Ordering Healthcare Provider Signature Provided"),
        required=False,
    )

    # directives.widget(primary_healthcare_provider=AutocompleteFieldWidget)
    primary_healthcare_provider = schema.TextLine(
        title=_(u"Primary Healthcare Provider"),
        description=_(u"Primary Healthcare Provider"),
        required=False,
    )
    """directives.widget(level=RadioFieldWidget)"""
    ana_testing = schema.Choice(
        title=_(u"ANA Testing Results"),
        description=_(u"ANA Testing Results"),
        required=True,
        values=[_(u'No Response'),
                _(u'Not Performed'),
                _(u'Negative'),
                _(u'Positive')],
    )

    clinical_impression = schema.Choice(
        title=_(u"Clinical Impression of SLE"),
        description=_(u"Clinical Impression of SLE"),
        required=True,
        values=[_(u'Not Specified'),
                _(u'Uncertain'),
                _(u'Yes'),
                _(u'No')],
    )

    xray_ordered = schema.Bool(
        title=_(u"Other Test(s) Ordered"),
        description=_(u"Other Test(s) Ordered Enter One Per Line"),
    )
    other_test_ordered = schema.List(
        title=_(u"Other Test(s) Ordered"),
        description=_(u"Other Test(s) Ordered Enter One Per Line"),
        missing_value=None,
        required=False,
        value_type=schema.TextLine()
    )

    """working example of multi choice input jp 1-31-17"""
    form.widget(symptoms_choice=CheckBoxFieldWidget)
    symptoms_choice = schema.List(
        title=_(u"Symptoms"),
        description=_(u"Symptoms, Select All That Apply"),
        required=False,
        value_type=schema.Choice(
            values=[_(u"Rash"),
                    _(u"Mouth Sores"),
                    _(u"Joint Pain"),
                    _(u"Inflammation"),
                    _(u"Seizures or Psychosis"),
                    _(u"Hair Loss")]),
    )

    joint_pain_text = schema.List(
        title=_(u"Joint Pain Specifics"),
        description=_(u"Joint Pain Specifics (Enter One Per Line)"),
        missing_value=None,
        required=False,
        value_type=schema.TextLine()
    )

    inflammation_text = schema.List(
        title=_(u"Inflammation Specifics"),
        description=_(u"Inflammation Specifics (Enter One Per Line)"),
        missing_value=None,
        required=False,
        value_type=schema.TextLine()
    )

    other_symptoms_text = schema.List(
        title=_(u"Other Symptom(s)"),
        description=_(u"Other Symptom(s) Enter One Per Line"),
        missing_value=None,
        required=False,
        value_type=schema.TextLine()
    )

    form.widget(diagnosis_code=CheckBoxFieldWidget)
    diagnosis_code = schema.List(
        title=_(u"Diagnosis & ICD-10 Codes"),
        description=_(u"Diagnosis & ICD-10 Codes"),
        required=False,
        value_type=schema.Choice(
            values=[_(u"D89.89"),
                    _(u"D89.9"),
                    _(u"L93.2"),
                    _(u"M32.10"),
                    _(u"M35.9"),
                    _(u"Other, please specify")]),
    )

    diagnosis_code_other = schema.List(
        title=_(u"Other Diagnosis Code(s)"),
        description=_(u"Other Diagnosis Code(s) Enter one Per Line"),
        missing_value=None,
        required=False,
        value_type=schema.TextLine()
    )

    phlebotomist_name = schema.TextLine(
        title=_(u"Phlebotomist Name"),
        description=_(u"Phlebotomist Name"),
        required=False,
    )

    phlebotomist_signature_provided = schema.Bool(
        title=_(u"Ordering Healthcare Provider Signature Provided"),
        description=_(u"Ordering Healthcare Provider Signature Provided"),
    )

    collection_date = schema.Date(
        title=_(u"Sample Collection Date"),
        description=_(u"Sample Collection Date"),
        required=False,
        default=date.today(),
    )

    received_date = schema.Date(
        title=_(u"Sample Received Date"),
        description=_(u"Sample Received Date"),
        required=False,
        default=date.today(),
    )

    sample_primary_insurance_name = schema.TextLine(
        title=_(u"Primary Insurance Name"),
        description=_(u"Primary Insurance Name"),
        required=False,
    )

    sample_primary_insurance_payerID = schema.TextLine(
        title=_(u"Primary Insurance Payer ID"),
        description=_(u"Primary Insurance Payer ID"),
        required=False,
    )

    sample_primary_insurance_policy_number = schema.TextLine(
        title=_(u"Primary Insurance Policy Number"),
        description=_(u"Primary Insurance Policy Number"),
        required=False,
    )

    sample_primary_insurance_plan_number = schema.TextLine(
        title=_(u"Primary Insurance Plan Number"),
        description=_(u"Primary Insurance Plan Number"),
        required=False,
    )

    sample_primary_insurance_authorization_precertificate = schema.TextLine(
        title=_(u"Primary Insurance Authorization"),
        description=_(u"Primary Insurance Authorization"),
        required=False,
    )

    sample_primary_insurance_subscriber_name = schema.TextLine(
        title=_(u"Primary Insurance Subscriber Name"),
        description=_(u"Primary Insurance Subscriber Name"),
        required=False,
    )

    """directives.widget(level=RadioFieldWidget)"""
    sample_primary_insurance_relation_to_insured = schema.Choice(
        title=_(u"Primary Insurance Relation to Insured"),
        description=_(u"Primary Insurance Relation to Insured"),
        values=[_(u"Self"),
                _(u"Spouse"),
                _(u"Child"),
                _(u"Other")],
        required=False,
    )

    sample_primary_insurance_subscriber_DOB = schema.Date(
        title=_(u"Primary Insurance Subscriber DOB"),
        description=_(u"Primary Insurance Subscriber DOB"),
        required=False,
    )

    sample_primary_insurance_effective_date = schema.Date(
        title=_(u"Primary Insurance Effective Date"),
        description=_(u"Primary Insurance Effective Date"),
        required=False,
    )

    sample_primary_insurance_address = schema.TextLine(
        title=_(u"Primary Insurance Address"),
        description=_(u"Primary Insurance Address"),
        required=False,
    )

    sample_primary_city = schema.TextLine(
        title=_(u"Primary Insurance City"),
        description=_(u"Primary Insurance City"),
        required=False,
    )

    sample_primary_state = schema.TextLine(
        title=_(u"Primary Insurance State"),
        description=_(u"Primary Insurance State"),
        required=False,
    )

    sample_primary_insurance_zip_code = schema.TextLine(
        title=_(u"Primary Insurance Zip Code"),
        description=_(u"Primary Insurance Zip Code"),
        required=False,
    )

    sample_secondary_insurance_name = schema.TextLine(
        title=_(u"Secondary Insurance Name"),
        description=_(u"Secondary Insurance Name"),
        required=False,
    )

    sample_secondary_insurance_payerID = schema.TextLine(
        title=_(u"Secondary Insurance Payer ID"),
        description=_(u"Secondary Insurance Payer ID"),
        required=False,
    )

    sample_secondary_insurance_policy_number = schema.TextLine(
        title=_(u"Secondary Insurance Policy Number"),
        description=_(u"Secondary Insurance Policy Number"),
        required=False,
    )

    sample_secondary_insurance_plan_number = schema.TextLine(
        title=_(u"Secondary Insurance Plan Number"),
        description=_(u"Secondary Insurance Plan Number"),
        required=False,
    )

    sample_secondary_insurance_authorization_precertificate = schema.TextLine(
        title=_(u"Secondary Insurance Authorization"),
        description=_(u"Secondary Insurance Authorization"),
        required=False,
    )

    sample_secondary_insurance_subscriber_name = schema.TextLine(
        title=_(u"Secondary Insurance Subscriber Name"),
        description=_(u"Secondary Insurance Subscriber Name"),
        required=False,
    )

    """directives.widget(level=RadioFieldWidget)"""
    sample_secondary_insurance_relation_to_insured = schema.Choice(
        title=_(u"Secondary Insurance Relation to Insured"),
        description=_(u"Secondary Insurance Relation to Insured"),
        values=[_(u"Self"),
                _(u"Spouse"),
                _(u"Child"),
                _(u"Other")],
        required=False,
    )

    sample_secondary_insurance_subscriber_DOB = schema.Datetime(
        title=_(u"Secondary Insurance Subscriber DOB"),
        description=_(u"Secondary Insurance Subscriber DOB"),
        required=False,
    )

    sample_secondary_insurance_effective_date = schema.Datetime(
        title=_(u"Secondary Insurance Effective Date"),
        description=_(u"Secondary Insurance Effective Date"),
        required=False,
    )

    sample_secondary_insurance_address = schema.TextLine(
        title=_(u"Secondary Insurance Address"),
        description=_(u"Secondary Insurance Address"),
        required=False,
    )

    sample_secondary_city = schema.TextLine(
        title=_(u"Secondary Insurance City"),
        description=_(u"Secondary Insurance City"),
        required=False,
    )

    sample_secondary_state = schema.TextLine(
        title=_(u"Secondary Insurance State"),
        description=_(u"Secondary Insurance State"),
        required=False,
    )

    sample_secondary_insurance_zip_code = schema.TextLine(
        title=_(u"Secondary Insurance Zip Code"),
        description=_(u"Secondary Insurance Zip Code"),
        required=False,
    )

    """directives.widget(level=RadioFieldWidget)"""
    billable_code = schema.Choice(
        title=_(u"Commercial Status"),
        description=_(u"Commercial Status"),
        required=True,
        values=[_(u'Billable'),
                _(u'No Charge')],
    )

    # will allow for sub categorization of billing status ie, vulture,
    # non ball bill ect
    billable_code_designation = schema.TextLine(
        title=_(u"Billing Designation of Sample"),
        description=_(u"Billing Designation of Sample"),
        required=False,
    )

    assignment_of_benefits_patient_name = schema.TextLine(
        title=_(u"Assignment of Benefits Patient Name"),
        description=_(u"Assignment of Benefits Patient Name"),
        required=False,
    )

    release_signed = schema.Bool(
        title=_(u"Release Signed"),
        description=_(u"Release Signed"),
    )

    assignment_of_benefits_signature_date = schema.Date(
        title=_(u"Assignment of Benefits Signature Date"),
        description=_(u"Assignment of Benefits Signature Date"),
        required=False,
        default=date.today(),
    )

    authorization_signature_patient_name = schema.TextLine(
        title=_(u"Authorization Signature Patient Name"),
        description=_(u"Authorization Signature Patient Name"),
        required=False,
    )
    payment_signed = schema.Bool(
        title=_(u"Payment Signed"),
        description=_(u"Payment Signed"),
    )

    authorization_signature_date = schema.Date(
        title=_(u"Authorization Signature Date"),
        description=_(u"Authorization Signature Date"),
        required=False,
        default=date.today(),
    )


alsoProvides(IClinicalSample, IFormFieldProvider)
