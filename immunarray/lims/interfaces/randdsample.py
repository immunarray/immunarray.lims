"""To add custome slide content to immunarray.lims
"""
import datetime

from immunarray.lims import messageFactory as _
from immunarray.lims.interfaces.solution import *


def currentTime():
    return datetime.datetime.now()
def currentDate():
    return datetime.datetime.now().date()

class IRandDSample(model.Schema):
    """General NCE Item to be used to track non conformance events in the lab"""
    RandDSampleVeracisID=schema.TextLine(
            title=_(u"R&D Veracis Sample ID"),
            description=_(u"NCE Tracking Numbe"),
            required=True,
    )
    RandDSampleDateAdded=schema.Datetime(
            title=_(u"Date R&D Sample was added to LIMS"),
            description=_(u"Date R&D Sample was added to LIMS"),
            defaultFactory=currentDate,
            required=True,
    )
    RandDSampleAddedby=schema.Choice(
            title=_(u"Operator that Added R&D Sample to LIMS"),
            description=_(u"Operator that Added R&D Sample to LIMS"),
            vocabulary=u"plone.principalsource.Users",
            required=False,
    )
    RandDSampleSource=schema.TextLine(
            title=_(u"Source of R&D Sample"),
            description=_(u"Source of R&D Sample"),
            required=False,
    )
    RandDSamplePI=schema.TextLine(
            title=_(u"Primary Investigator (PI) of R&D Sample"),
            description=_(u"Primary Investigator (PI) of R&D Sample"),
            required=False,
    )
    RandDSampleDescription=schema.TextLine(
            title=_(u"Description of R&D Sample"),
            description=_(u"Description of R&D Sample"),
            required=False,
    )
    RandDSampleSourceID=schema.TextLine(
            title=_(u"Source ID of R&D Sample"),
            description=_(u"Source ID of R&D Sample"),
            required=False,
    )
    RandDSampleVolume=schema.Float(
            title=_(u"Volume of R&D Sample in micro liters (uL)"),
            description=_(u"Volume of R&D Sample in micro liters (uL)"),
            required=False,
    )
    RandDSampleType=schema.Choice(
            title=_(u"R&D Sample Type (Bulk or Working)"),
            description=_(u"R&D Sample Type (Bulk or Working)"),
            values=[_(u"Working"),_(u"Bulk")],
            required=False,
    )
    RandDSampleStatus=schema.Choice(
            title=_(u"R&D Sample Status (Available, In Process, Retained, Consumed)"),
            description=_(u"R&D Sample Status (Available, In Process, Retained, Consumed)"),
            values=[_(u"Available"),_(u"In Process"),_(u"Retained"),_(u"Consumed")],
            required=False,
    )
    RandDFluidType=schema.Choice(
            title=_(u"R&D Fluid Type"),
            description=_(u"R&D Fluid Type"),
            values=[_(u"Serum"),_(u"Plasma"),_(u"CSF"),_(u"Tissue")],
            required=False,
    )
    RandDSampleReceived=schema.Date(
            title=_(u"Date R&D Sample was Received"),
            description=_(u"Date R&D Sample was Received"),
            required=True,
    )
    RandDSampleDateDisposed=schema.Date(
            title=_(u"Date R&D Sample was Disposed"),
            description=_(u"Date R&D Sample was Disposed"),
            required=True,
    )
    RandDSampleComment=schema.Text(
            title=_(u"Any Notes or Comments About the R&D Sample"),
            description=_(u"Any Notes or Comments About the R&D Sample"),
            required=False,
    )
