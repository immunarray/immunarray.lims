# -*- coding: utf-8 -*-
import datetime

from immunarray.lims import messageFactory as _
from immunarray.lims.content.abstractsample import assignVeracisId
from immunarray.lims.interfaces.sample import ISample
from zope import schema

from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides


def currentTime():
    return datetime.datetime.now()


def currentDate():
    return datetime.datetime.now().date()


class IRandDSample(ISample):
    """R and D sample!
    """

    department = schema.Choice(
        title=_(u"Department"),
        description=_(u"Department that controls material"),
        values=[_(u"TBI"), _(u"Commercial"), _(u"BrainBox"), _(u"Other")],
        required=False,
    )

    source_id_one = schema.TextLine(
        title=_(u"Primary R&D Source Sample ID"),
        description=_(u"Primary R&D Source Sample ID"),
        required=False,
    )

    source_id_two = schema.TextLine(
        title=_(u"Secondary R&D Source Sample ID"),
        description=_(u"Secondary R&D Source Sample ID"),
        required=False,
    )

    source_id_three = schema.TextLine(
        title=_(u"Tertiary R&D Source Sample ID"),
        description=_(u"Tertiary R&D Source Sample ID"),
        required=False,
    )

    # Unlike Clinical Samples which store this value in "usn" field,
    # RandD/QC samples have a dedicated veracis_id field.
    veracis_id = schema.TextLine(
        title=_(u"R&D Veracis Sample ID"),
        description=_(u"R&D Veracis Sample ID"),
        defaultFactory=assignVeracisId(),
        required=True,
    )

    date_added = schema.Date(
        title=_(u"Date R&D Sample was added to LIMS"),
        description=_(u"Date R&D Sample was added to LIMS"),
        defaultFactory=currentDate,
        required=True,
    )

    added_by = schema.Choice(
        title=_(u"Operator that Added R&D Sample to LIMS"),
        description=_(u"Operator that Added R&D Sample to LIMS"),
        vocabulary=u"plone.principalsource.Users",
        required=False,
    )

    source = schema.TextLine(
        title=_(u"Source of R&D Sample"),
        description=_(u"Source of R&D Sample"),
        required=False,
    )

    pi = schema.TextLine(
        title=_(u"Primary Investigator (PI) of R&D Sample"),
        description=_(u"Primary Investigator (PI) of R&D Sample"),
        required=False,
    )

    description = schema.TextLine(
        title=_(u"Description of R&D Sample"),
        description=_(u"Description of R&D Sample"),
        required=False,
    )

    fluid_type = schema.Choice(
        title=_(u"R&D Fluid Type"),
        description=_(u"R&D Fluid Type"),
        values=[_(u"Serum"), _(u"Plasma"), _(u"CSF"), _(u"Tissue")],
        required=True,
    )

    date_received = schema.Date(
        title=_(u"Date R&D Sample was Received"),
        description=_(u"Date R&D Sample was Received"),
        required=True,
    )

    comment = schema.Text(
        title=_(u"Any Notes or Comments About the R&D Sample"),
        description=_(u"Any Notes or Comments About the R&D Sample"),
        required=False,
    )


alsoProvides(IRandDSample, IFormFieldProvider)
