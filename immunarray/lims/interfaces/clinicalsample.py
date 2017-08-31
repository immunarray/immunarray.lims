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
    usn = schema.TextLine(
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
    other_test_ordered = schema.TextLine(
        title=_(u"Other Test(s) Ordered"),
        description=_(u"Other Test(s) Ordered Enter One Per Line"),
        required=False,
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

    joint_pain_text = schema.TextLine(
        title=_(u"Joint Pain Specifics"),
        description=_(u"Joint Pain Specifics (Enter One Per Line)"),
    )

    inflammation_text = schema.TextLine(
        title=_(u"Inflammation Specifics"),
        description=_(u"Inflammation Specifics (Enter One Per Line)"),
    )

    other_symptoms_text = schema.TextLine(
        title=_(u"Other Symptom(s)"),
        description=_(u"Other Symptom(s) Enter One Per Line"),
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

alsoProvides(IClinicalSample, IFormFieldProvider)
