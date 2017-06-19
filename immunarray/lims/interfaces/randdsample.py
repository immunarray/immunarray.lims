"""To add custome slide content to immunarray.lims 
    (needs to be randd_aliquot, we don't have randd_samples)
"""
import datetime

from immunarray.lims import messageFactory as _
from immunarray.lims.interfaces.solution import *


def currentTime():
    return datetime.datetime.now()


def currentDate():
    return datetime.datetime.now().date()


class IRandDSample(model.Schema):
    """R and D sample!
    """

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

    veracis_id = schema.TextLine(
        title=_(u"R&D Veracis Sample ID"),
        description=_(u"R&D Veracis Sample ID"),
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

    volume_received = schema.Float(
        title=_(u"Volume of R&D Sample in micro liters (uL)"),
        description=_(u"Volume of R&D Sample in micro liters (uL)"),
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

    #Should be on the aliquot object not the sample
    """
    status = schema.Choice(
        title=_(
            u"R&D Sample Status (Available, In Process, Retained, Consumed)"),
        description=_(
            u"R&D Sample Status (Available, In Process, Retained, Consumed)"),
        values=[_(u"Available"), _(u"In Process"), _(u"Retained"),
                _(u"Quarantined"), _(u"Consumed")],
        required=False,
    )
    """
    #Should be on the aliquot object not the sample
    """
    date_disposed = schema.Date(
        title=_(u"Date R&D Sample was Disposed"),
        description=_(u"Date R&D Sample was Disposed"),
        required=False,
    )
    """
