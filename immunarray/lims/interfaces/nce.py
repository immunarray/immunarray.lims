"""To add custome slide content to immunarray.lims
"""
import datetime

from immunarray.lims import messageFactory as _
from immunarray.lims.interfaces.solution import *


def currentTime():
    return datetime.datetime.now()


class INCE(model.Schema):
    """General NCE Item to be used to track non conformance events in the lab
    """

    current_date_time = schema.Datetime(
        title=_(u"Datetime of NCE"),
        description=_(u"Datetime of NCE"),
        defaultFactory=currentTime,
        required=True,
    )

    reporter = schema.Choice(
        title=_(u"Operator that is Reporting NCE"),
        description=_(u"Operator that is Reporting NCE"),
        vocabulary=u"plone.principalsource.Users",
        required=False,
    )
