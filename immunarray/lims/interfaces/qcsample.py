# -*- coding: utf-8 -*-
import datetime

from immunarray.lims import messageFactory as _
from immunarray.lims.content.abstractsample import assignVeracisId
from immunarray.lims.interfaces.sample import ISample
from immunarray.lims.interfaces.solution import *
from zope import schema
from zope.interface import alsoProvides


def currentTime():
    return datetime.datetime.now()


def currentDate():
    return datetime.datetime.now().date()


class IQCSample(ISample):
    """QC Sample!
    """
    # Unlike Clinical Samples which store this value in "usn" field,
    # RandD/QC samples have a dedicated veracis_id field.
    veracis_id = schema.TextLine(
        title=_(u"QC Veracis Sample ID"),
        description=_(u"QC Veracis Sample ID"),
        defaultFactory=assignVeracisId(),
        required=True,
    )

    source_id_one = schema.TextLine(
        title=_(u"Primary QC Source Sample ID"),
        description=_(u"Primary QC Source Sample ID"),
        required=True,
    )

    source_id_two = schema.TextLine(
        title=_(u"Secondary QC Source Sample ID"),
        description=_(u"Secondary QC Source Sample ID"),
        required=False,
    )

    source_id_three = schema.TextLine(
        title=_(u"Tertiary QC Source Sample ID"),
        description=_(u"Tertiary QC Source Sample ID"),
        required=False,
    )

    date_added = schema.Date(
        title=_(u"Date QC Sample was added to LIMS"),
        description=_(u"Date QC Sample was added to LIMS"),
        defaultFactory=currentDate,
        required=True,
    )

    added_by = schema.Choice(
        title=_(u"Operator that Added QC Sample to LIMS"),
        description=_(u"Operator that Added QC Sample to LIMS"),
        vocabulary=u"plone.principalsource.Users",
        required=False,
    )

    source = schema.TextLine(
        title=_(u"Source of QC Sample"),
        description=_(u"Source of QC Sample"),
        required=False,
    )

    description = schema.TextLine(
        title=_(u"Description of QC Sample"),
        description=_(u"Description of QC Sample"),
        required=False,
    )

    fluid_type = schema.Choice(
        title=_(u"QC Fluid Type"),
        description=_(u"QC Fluid Type"),
        values=[_(u"Serum"), _(u"Plasma"), _(u"CSF"), _(u"Tissue")],
        required=True,
    )

    date_received = schema.Date(
        title=_(u"Date QC Sample was Received"),
        description=_(u"Date QC Sample was Received"),
        required=True,
    )

    comment = schema.Text(
        title=_(u"Any Notes or Comments About the QC Sample"),
        description=_(u"Any Notes or Comments About the QC Sample"),
        required=False,
    )


alsoProvides(IQCSample, IFormFieldProvider)
