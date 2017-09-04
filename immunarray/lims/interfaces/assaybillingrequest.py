# -*- coding: utf-8 -*-

import datetime
from zope import schema

from immunarray.lims import messageFactory as _
from immunarray.lims.interfaces import BaseModel
from immunarray.lims.vocabularies.billingprogrmas import \
    BillingProgramsVocabulary
from immunarray.lims.vocabularies.ichipassay import IChipAssayListVocabulary
from plone.autoform import directives as form
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from plone.autoform.interfaces import IFormFieldProvider
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from zope.interface import alsoProvides


def currentDate():
    return datetime.datetime.now().date()


class IAssayBillingRequest(BaseModel):
    """Object that will be attached to sample.  It will be the instance object
    that has a workflow that can be tracked in the LIMS.
    """
    assay_name = schema.Choice(
        title=_(u"Assay to be Billed"),
        description=_(u"Assay to be Billed"),
        source=IChipAssayListVocabulary,
        required=True
    )

    billing_program = schema.Choice(
        title=_(u"Billing Program"),
        description=_(u"Billing Program"),
        source=BillingProgramsVocabulary,
        required=False
    )
    # Need to make content file and title from sampleid and assay name
    sample_id = schema.TextLine(
        title=_(u"Billing Sample ID`"),
        description=_(u"Billing Sample ID`"),
        required=False,
    )

    date_ordered = schema.Date(
        title=_(u"Date Billing Requste was added to LIMS"),
        description=_(u"Date Billing Requste was added to LIMS"),
        defaultFactory=currentDate,
        required=True,
    )

    date_resulted = schema.Date(
        title=_(u"Assay Billing Resolved Date"),
        description=_(u"Assay Billing Resolved Date"),
        required=False,
    )

    date_billed = schema.Date(
        title=_(u"Assay Billed on Date"),
        description=_(u"Assay Billed on Date"),
        required=False,
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

    primary_insurance_name = schema.TextLine(
        title=_(u"Primary Insurance Name"),
        description=_(u"Primary Insurance Name"),
        required=False,
    )

    primary_insurance_payerID = schema.TextLine(
        title=_(u"Primary Insurance Payer ID"),
        description=_(u"Primary Insurance Payer ID"),
        required=False,
    )

    primary_insurance_policy_number = schema.TextLine(
        title=_(u"Primary Insurance Policy Number"),
        description=_(u"Primary Insurance Policy Number"),
        required=False,
    )

    primary_insurance_plan_number = schema.TextLine(
        title=_(u"Primary Insurance Plan Number"),
        description=_(u"Primary Insurance Plan Number"),
        required=False,
    )

    primary_insurance_authorization_precertificate = schema.TextLine(
        title=_(u"Primary Insurance Authorization"),
        description=_(u"Primary Insurance Authorization"),
        required=False,
    )

    primary_insurance_subscriber_name = schema.TextLine(
        title=_(u"Primary Insurance Subscriber Name"),
        description=_(u"Primary Insurance Subscriber Name"),
        required=False,
    )

    """directives.widget(level=RadioFieldWidget)"""
    primary_insurance_relation_to_insured = schema.Choice(
        title=_(u"Primary Insurance Relation to Insured"),
        description=_(u"Primary Insurance Relation to Insured"),
        values=[_(u"Self"),
                _(u"Spouse"),
                _(u"Child"),
                _(u"Other")],
        required=False,
    )

    primary_insurance_subscriber_DOB = schema.Date(
        title=_(u"Primary Insurance Subscriber DOB"),
        description=_(u"Primary Insurance Subscriber DOB"),
        required=False,
    )

    primary_insurance_effective_date = schema.Date(
        title=_(u"Primary Insurance Effective Date"),
        description=_(u"Primary Insurance Effective Date"),
        required=False,
    )

    primary_insurance_address = schema.TextLine(
        title=_(u"Primary Insurance Address"),
        description=_(u"Primary Insurance Address"),
        required=False,
    )

    primary_city = schema.TextLine(
        title=_(u"Primary Insurance City"),
        description=_(u"Primary Insurance City"),
        required=False,
    )

    primary_state = schema.TextLine(
        title=_(u"Primary Insurance State"),
        description=_(u"Primary Insurance State"),
        required=False,
    )

    primary_insurance_zip_code = schema.TextLine(
        title=_(u"Primary Insurance Zip Code"),
        description=_(u"Primary Insurance Zip Code"),
        required=False,
    )

    secondary_insurance_name = schema.TextLine(
        title=_(u"Secondary Insurance Name"),
        description=_(u"Secondary Insurance Name"),
        required=False,
    )

    secondary_insurance_payerID = schema.TextLine(
        title=_(u"Secondary Insurance Payer ID"),
        description=_(u"Secondary Insurance Payer ID"),
        required=False,
    )

    secondary_insurance_policy_number = schema.TextLine(
        title=_(u"Secondary Insurance Policy Number"),
        description=_(u"Secondary Insurance Policy Number"),
        required=False,
    )

    secondary_insurance_plan_number = schema.TextLine(
        title=_(u"Secondary Insurance Plan Number"),
        description=_(u"Secondary Insurance Plan Number"),
        required=False,
    )

    secondary_insurance_authorization_precertificate = schema.TextLine(
        title=_(u"Secondary Insurance Authorization"),
        description=_(u"Secondary Insurance Authorization"),
        required=False,
    )

    secondary_insurance_subscriber_name = schema.TextLine(
        title=_(u"Secondary Insurance Subscriber Name"),
        description=_(u"Secondary Insurance Subscriber Name"),
        required=False,
    )

    """directives.widget(level=RadioFieldWidget)"""
    secondary_insurance_relation_to_insured = schema.Choice(
        title=_(u"Secondary Insurance Relation to Insured"),
        description=_(u"Secondary Insurance Relation to Insured"),
        values=[_(u"Self"),
                _(u"Spouse"),
                _(u"Child"),
                _(u"Other")],
        required=False,
    )

    secondary_insurance_subscriber_DOB = schema.Datetime(
        title=_(u"Secondary Insurance Subscriber DOB"),
        description=_(u"Secondary Insurance Subscriber DOB"),
        required=False,
    )

    secondary_insurance_effective_date = schema.Datetime(
        title=_(u"Secondary Insurance Effective Date"),
        description=_(u"Secondary Insurance Effective Date"),
        required=False,
    )

    secondary_insurance_address = schema.TextLine(
        title=_(u"Secondary Insurance Address"),
        description=_(u"Secondary Insurance Address"),
        required=False,
    )

    secondary_city = schema.TextLine(
        title=_(u"Secondary Insurance City"),
        description=_(u"Secondary Insurance City"),
        required=False,
    )

    secondary_state = schema.TextLine(
        title=_(u"Secondary Insurance State"),
        description=_(u"Secondary Insurance State"),
        required=False,
    )

    secondary_insurance_zip_code = schema.TextLine(
        title=_(u"Secondary Insurance Zip Code"),
        description=_(u"Secondary Insurance Zip Code"),
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
        default=datetime.date.today(),
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
        default=datetime.date.today(),
    )

    comment = schema.Text(
        title=_(u"Any Notes or Comments About the Assay Billing Request"),
        description=_(u"Any Notes or Comments About the Assay Billing Request"),
        required=False,
    )

alsoProvides(IAssayBillingRequest, IFormFieldProvider)
