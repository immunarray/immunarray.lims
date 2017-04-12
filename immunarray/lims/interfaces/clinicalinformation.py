# -*- coding: utf-8 -*-
from datetime import date
from plone.app.textfield import RichText
from zope import schema
from plone.supermodel import model
from immunarray.lims import messageFactory as _
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.utils import createContentInContainer
from plone.autoform import directives
from zope.interface import alsoProvides
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from plone.autoform import directives as form

class IMedicalHistoryPatient(model.Schema):
    """ Interface for clinical information input given by patient"""
    form.widget(symptoms_choice=CheckBoxFieldWidget)
    clinical_impression = schema.List(
        title=_(u"Clinical Impression"),
        description=_(u"Clinical Impression of the Referring Physicain/"
                      u", Select All That Apply"),
        required=False,
        value_type=schema.Choice(
            values=[_(u"Systemic Lupus Erythematosus (SLE)"),
                    _(u"Antiphospholipid Syndrome"),
                    _(u"Asthma"),
                    _(u"Autoimmune Hepatitis"),
                    _(u"Seizures or psychosis"),
                    _(u"Hair loss")]),
    )

class ICaseReportFormPhysician(model.Schema):
    """ Interface for clinial information input given by physician"""
    pass
