# -*- coding: utf-8 -*-
from immunarray.lims import messageFactory as _
from immunarray.lims.interfaces import BaseModel
from plone.autoform import directives as form
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from zope import schema


class IMedicalHistoryPatient(BaseModel):
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


class ICaseReportFormPhysician(BaseModel):
    """ Interface for clinial information input given by physician"""
    pass
