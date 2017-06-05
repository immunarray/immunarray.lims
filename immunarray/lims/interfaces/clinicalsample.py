# -*- coding: utf-8 -*-
from datetime import date
from plone.app.textfield import RichText
from zope import schema
from plone.supermodel import model
from immunarray.lims import messageFactory as _
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.utils import createContentInContainer
from bika.lims.interfaces.sample import ISample
from plone.autoform import directives
from plone.autoform import directives as form
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from z3c.form.browser.radio import RadioFieldWidget
from zope.interface import alsoProvides
from immunarray.lims.vocabularies.provider import ProvidersVocabulary
from plone.formwidget.autocomplete import AutocompleteFieldWidget
from plone.formwidget.autocomplete import AutocompleteMultiFieldWidget
from immunarray.lims.vocabularies.ichipassay import IChipAssayListVocabulary

class IClinicalSample(model.Schema):
    """Sample that will contain all the billing info and high level information
        that is applicable to all aliquots made from this material, location of
        tests ordered on sample
    """
    title = schema.TextLine(
        title=_(u"Unique Sample Number"),
        description=_(u"Sample ID from the blood draw kit"),
        required=False,
    )

    #want to index this field
    sample_serial_number = schema.Int(
        title=_(u"Sample Serial Number"),
        description=_(u"Sample Serial Number"),
        required=False,
    )
    """ Want to do an n+1 but allow be edited, should be unique"""

    sample_status = schema.Choice(
        title = _(u"Status of Testing"),
        description = _(u"Status of Testing"),
        required = True,
        values=[_(u"Received"),
                _(u"All Tests Closed"),],
    )
    # list or tuple? JP 3-14-17, let this be blank for remote order
    # option at a later date, need test ordered and status!
    # use this to drive a setup handler that will make the lists of what should
    # be tested! (jp 4-11-17)

    front_end_qa = schema.Choice(
        title = _(u"Front End QA Status"),
        description = _(u"Front End QA Status"),
        required = True,
        values=[_(u"Initial"),
                _(u"Review Pass"),
                _(u"Held"),],
    )
    # dictonary with value stauts and key test ordered
    test_ordered_status = schema.Dict(
        key_type=schema.Choice(source=IChipAssayListVocabulary, required=False),
        value_type=schema.Choice(values=[_(u"Recived"),
                                         _(u"To Be Tested"),
                                         _(u"In Que"),
                                         _(u"Testing"),
                                         _(u"Rerun"),
                                         _(u"Resulted"),
                                         _(u"Billing Message Sent"),
                                         _(u"Closed"), ], required=True)
    )

    sample_primary_insurance_name = schema.TextLine(
        title=_(u"Primary Insurance Name"),
        description =_(u"Primary Insurance Name"),
        required=False,
    )

    sample_primary_insurance_payerID = schema.TextLine(
        title=_(u"Primary Insurance Payer ID"),
        description =_(u"Primary Insurance Payer ID"),
        required=False,
    )

    sample_primary_insurance_policy_number = schema.TextLine(
        title=_(u"Primary Insurance Policy Number"),
        description =_(u"Primary Insurance Policy Number"),
        required=False,
    )

    sample_primary_insurance_plan_number = schema.TextLine(
        title=_(u"Primary Insurance Plan Number"),
        description =_(u"Primary Insurance Plan Number"),
        required=False,
    )

    sample_primary_insurance_authorization_precertificate = schema.TextLine(
        title=_(u"Primary Insurance Authorization"),
        description =_(u"Primary Insurance Authorization"),
        required=False,
    )

    sample_primary_insurance_subscriber_name = schema.TextLine(
        title=_(u"Primary Insurance Subscriber Name"),
        description =_(u"Primary Insurance Subscriber Name"),
        required=False,
    )

    """directives.widget(level=RadioFieldWidget)"""
    sample_primary_insurance_relation_to_insured = schema.Choice(
        title=_(u"Primary Insurance Relation to Insured"),
        description =_(u"Primary Insurance Relation to Insured"),
        values=[_(u"Self"),
                _(u"Spouse"),
                _(u"Child"),
                _(u"Other")],
        required=False,
    )

    sample_primary_insurance_subscriber_DOB = schema.Date(
        title=_(u"Primary Insurance Subscriber DOB"),
        description =_(u"Primary Insurance Subscriber DOB"),
        required=False,
    )

    sample_primary_insurance_effective_date = schema.Date(
        title=_(u"Primary Insurance Effective Date"),
        description =_(u"Primary Insurance Effective Date"),
        required=False,
    )

    sample_primary_insurance_address = schema.TextLine(
        title=_(u"Primary Insurance Address"),
        description =_(u"Primary Insurance Address"),
        required=False,
    )

    sample_primary_city = schema.TextLine(
        title=_(u"Primary Insurance City"),
        description =_(u"Primary Insurance City"),
        required=False,
    )

    sample_primary_state = schema.TextLine(
        title=_(u"Primary Insurance State"),
        description =_(u"Primary Insurance State"),
        required=False,
    )

    sample_primary_insurance_zip_code = schema.TextLine(
        title=_(u"Primary Insurance Zip Code"),
        description =_(u"Primary Insurance Zip Code"),
        required=False,
    )

    sample_secondary_insurance_name = schema.TextLine(
        title=_(u"Secondary Insurance Name"),
        description =_(u"Secondary Insurance Name"),
        required=False,
    )

    sample_secondary_insurance_payerID = schema.TextLine(
        title=_(u"Secondary Insurance Payer ID"),
        description =_(u"Secondary Insurance Payer ID"),
        required=False,
    )

    sample_secondary_insurance_policy_number = schema.TextLine(
        title=_(u"Secondary Insurance Policy Number"),
        description =_(u"Secondary Insurance Policy Number"),
        required=False,
    )

    sample_secondary_insurance_plan_number = schema.TextLine(
        title=_(u"Secondary Insurance Plan Number"),
        description =_(u"Secondary Insurance Plan Number"),
        required=False,
    )

    sample_secondary_insurance_authorization_precertificate = schema.TextLine(
        title=_(u"Secondary Insurance Authorization"),
        description =_(u"Secondary Insurance Authorization"),
        required=False,
    )

    sample_secondary_insurance_subscriber_name = schema.TextLine(
        title=_(u"Secondary Insurance Subscriber Name"),
        description =_(u"Secondary Insurance Subscriber Name"),
        required=False,
    )

    """directives.widget(level=RadioFieldWidget)"""
    sample_secondary_insurance_relation_to_insured = schema.Choice(
        title=_(u"Secondary Insurance Relation to Insured"),
        description =_(u"Secondary Insurance Relation to Insured"),
        values=[_(u"Self"),
                _(u"Spouse"),
                _(u"Child"),
                _(u"Other")],
        required=False,
    )

    sample_secondary_insurance_subscriber_DOB = schema.Datetime(
        title=_(u"Secondary Insurance Subscriber DOB"),
        description =_(u"Secondary Insurance Subscriber DOB"),
        required=False,
    )

    sample_secondary_insurance_effective_date = schema.Datetime(
        title=_(u"Secondary Insurance Effective Date"),
        description =_(u"Secondary Insurance Effective Date"),
        required=False,
    )

    sample_secondary_insurance_address = schema.TextLine(
        title=_(u"Secondary Insurance Address"),
        description =_(u"Secondary Insurance Address"),
        required=False,
    )

    sample_secondary_city = schema.TextLine(
        title=_(u"Secondary Insurance City"),
        description =_(u"Secondary Insurance City"),
        required=False,
    )

    sample_secondary_state = schema.TextLine(
        title=_(u"Secondary Insurance State"),
        description =_(u"Secondary Insurance State"),
        required=False,
    )

    sample_secondary_insurance_zip_code = schema.TextLine(
        title=_(u"Secondary Insurance Zip Code"),
        description =_(u"Secondary Insurance Zip Code"),
        required=False,
    )

    """directives.widget(level=RadioFieldWidget)"""
    billable_code = schema.Choice(
        title=_(u"Commercail Status"),
        description=_(u"Commercial Status"),
        required=True,
        values=[_(u'Billable'),
                _(u'No Charge'),
                _(u'RUO')],
    )

    sample_ordering_healthcare_provider = schema.Choice(
        title=_(u"Ordering Healthcare Provider"),
        description=_(u"Ordering Healthcare Provider"),
        vocabulary=u"immunarray.lims.vocabularies.provider.ProvidersVocabulary",
        required=False,
    )
    sample_ordering_healthcare_provider_signature = schema.Bool(
        title=_(u"Ordering Healthcare Provider Signature Provided"),
        description=_(u"Ordering Healthcare Provider Signature Provided"),
        required=False,
    )

    directives.widget(primary_healthcare_provider=AutocompleteFieldWidget)
    primary_healthcare_provider = schema.Choice(
        title=_(u"Primary Healthcare Provider"),
        description=_(u"Primary Healthcare Provider"),
        vocabulary=u"immunarray.lims.vocabularies.provider.ProvidersVocabulary",
        required=False,
    )
    """directives.widget(level=RadioFieldWidget)"""
    ana_teesting = schema.Choice(
        title=_(u"ANA Testing Results"),
        description=_(u"ANA Testing Results"),
        required=True,
        values=[_(u'No Response'),
                _(u'Not Performed'),
                _(u'Negative'),
                _(u'Positive')],
    )

    clinical_impression = schema.Choice(
        title=_(u"Clinical Impression"),
        description=_(u"Clinical Impression"),
        required=True,
        values=[_(u'Not Specified'),
                _(u'Uncertain'),
                _(u'Yes'),
                _(u'No')],
    )

    other_test_ordered = schema.List(
        title=_(u"Other Test(s) Ordered"),
        description =_(u"Other Test(s) Ordered Enter One Per Line"),
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
                _(u"Mouth sores"),
                _(u"Joint Pain if yes, please specify"),
                _(u"Inflammation, if yes, please specify"),
                _(u"Seizures or psychosis"),
                _(u"Hair loss")]),
    )

    symptoms_text = schema.List(
        title=_(u"Symptom(s)"),
        description =_(u"Symptom(s) Enter One Per Line"),
        missing_value=None,
        required=False,
        value_type=schema.TextLine()
    )
    form.widget(diagnosis_code=CheckBoxFieldWidget)
    diagnosis_code = schema.List(
        title=_(u"Diagnosis & ICD-10 Codes"),
        description=_(u"Diagnosis & ICD-10 Codes"),
        required=True,
        value_type=schema.Choice(
            values=[_(u"D89.89-Other specified disorders involving the immune mechanism, not elsewhere classified"),
                _(u"D89.9-Disorder involving the immune mechanism, unspecified"),
                _(u"L93.2-Other local lupus erythematosus"),
                _(u"M32.10-Systemic lupus erythematosus, organ or system involvement unspecified"),
                _(u"M35.9-Systemic involvement of connective tissue, unspecified"),
                _(u"Other, please specify")]),
    )

    diagnosis_code_other = schema.List(
        title=_(u"Other Diagnosis Code(s)"),
        description =_(u"Other Diagnosis Code(s) Enter one Per Line"),
        missing_value=None,
        required=False,
        value_type=schema.TextLine()
    )

    phlebotomist_last_name = schema.TextLine(
        title=_(u"Phlebotomist Last Name"),
        description =_(u"Phlebotomist Last Name"),
        required=False,
    )

    phlebotomist_signature_provided=schema.Bool(
        title=_(u"Ordering Healthcare Provider Signature Provided"),
        description=_(u"Ordering Healthcare Provider Signature Provided"),
    )

    collection_date = schema.Date(
        title=_(u"Sample Collection Date"),
        description =_(u"Sample Collection Date"),
        required=False,
        default=date.today(),
    )

    received_date = schema.Date(
        title=_(u"Sample Received Date"),
        description =_(u"Sample Received Date"),
        required=False,
        default=date.today(),
    )

    assignment_of_benefits_patient_name = schema.TextLine(
        title=_(u"Assignment of Benefits Patient Name"),
        description =_(u"Assignment of Benefits Patient Name"),
        required=False,
    )

    release_signed = schema.Bool(
        title=_(u"Release Signed"),
        description=_(u"Release Signed"),
    )

    assignment_of_benefits_signature_date = schema.Date(
        title=_(u"Assignment of Benefits Signature Date"),
        description =_(u"Assignment of Benefits Signature Date"),
        required=False,
        default=date.today(),
    )

    authorization_signature_patient_name = schema.TextLine(
        title=_(u"Authorization Signature Patient Name"),
        description =_(u"Authorization Signature Patient Name"),
        required=False,
    )
    payment_signed = schema.Bool(
        title=_(u"Payment Signed"),
        description=_(u"Payment Signed"),
    )

    authorization_signature_date = schema.Date(
        title=_(u"Authorization Signature Date"),
        description =_(u"Authorization Signature Date"),
        required=False,
        default=date.today(),
    )
alsoProvides(IClinicalSample, IFormFieldProvider)
