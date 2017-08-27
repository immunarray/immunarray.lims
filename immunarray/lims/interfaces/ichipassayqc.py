# -*- coding: utf-8 -*-
from immunarray.lims import messageFactory as _
from immunarray.lims.vocabularies.ichipassay import IChipAssayListVocabulary
from plone.autoform import directives as form
from plone.namedfile.field import NamedFile
from plone.supermodel import model
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from zope import schema


class IiChipAssayQC(model.Schema):
    """An iChip Lot that will contain iChip objects.
    """

    title = schema.TextLine(
        title=_(u"iChip Assay QC Name"),
        description=_(u""),
        required=True,
    )

    # Allow mutiple selections!
    # Need to connect this to iChipAssay.name
    form.widget(intended_assay=CheckBoxFieldWidget)
    intended_assay = schema.List(
        title=_(u"Intended Assay(s)"),
        description=_(u"Intended Assay(s)"),
        required=False,
        value_type=schema.Choice(source=IChipAssayListVocabulary),
    )

    type_of_control = schema.Choice(
        title=_(u"Type of Control"),
        description=_(u"Type of Control"),
        values=[_(u"High/Positive"),
                _(u"Low/Negative")],
        required=True,
    )

    parent_ID = schema.TextLine(
        title=_(u"Parent ID"),
        description=_(u"Parent ID"),
        required=False,
    )

    source_report = NamedFile(
        title=_(u"Source Report"),
        description=_(u"Source Report"),
        required=False,
    )

    release_report = NamedFile(
        title=_(u"Release Report"),
        description=_(u"Release Report"),
        required=False,
    )

    stauts = schema.Choice(
        title=_(u"Stauts"),
        description=_(u"Status"),
        values=[_(u"In-Validation"),
                _(u"Released"),
                _(u"Consumed"),
                _(u"Quarantined")],
        required=True,
    )
    release_date = schema.Date(
        title=_(u"Release Date"),
        description=_(u"Release Date"),
        required=False,
    )

    close_date = schema.Date(
        title=_(u"Closed Date"),
        description=_(u"Closed Date"),
        required=False,
    )
