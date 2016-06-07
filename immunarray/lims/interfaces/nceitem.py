"""To add custome slide content to immunarray.lims
"""
import datetime

from immunarray.lims import messageFactory as _
from immunarray.lims.interfaces.solution import *


def currentTime():
    return datetime.datetime.now()

class INCEItem(model.Schema):
    """General NCE Item to be used to track non conformance events in the lab"""
    NCETrackingNumber=schema.ASCIILine(
            title=_(u"NCE Tracking Number"),
            description=_(u"NCE Tracking Number"),
            required=True,
    )
    NCECurrentDateTime=schema.Datetime(
            title=_(u"Datetime of NCE"),
            description=_(u"Datetime of NCE"),
            defaultFactory=currentTime,
            required=True,
    )
    NCEReporter=schema.Choice(
            title=_(u"Operator that is Reporting NCE"),
            description=_(u"Operator that is Reporting NCE"),
            vocabulary=u"plone.principalsource.Users",
            required=False,
    )
