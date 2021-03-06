# -*- coding: utf-8 -*-
"""Interface for Customer Service Incident
"""

from immunarray.lims import messageFactory as _
from immunarray.lims.interfaces import BaseModel
from zope import schema


class ICustomerServiceCall(BaseModel):
    """Interface for Customer Service Call objects CSC
    """
    csc_client = schema.Choice(
        title=_(u"Client"),
        description=_(u"Client"),
        required=True,
        values=[_(u'Quarantined'), _(u'Released')],
    )
    csc_instance = schema.Choice(
        title=_(u"Instance Type"),
        description=_(u"Instance Type"),
        required=True,
        values=[_(u'Quarantined'), _(u'Released')],
    )
    csc_datetime = schema.Datetime(
        title=_(u"Date and Time of Instance"),
        description=_(u"Date and Time of Instance"),
        required=False,
    )
    csc_follow_up_needed = schema.Bool(
        title=_(u"Is Follow Up Needed"),
        description=_(u"Is Follow Up Needed"),
        required=False,
    )
    csc_status = schema.Choice(
        title=_(u"Status of CSI"),
        description=_(u"Status of CSI"),
        required=True,
        values=[_(u'Open'), _(u'Closed'), _(u'Held')],
    )
    csc_details = schema.Text(
        title=_(u"Details of CSI"),
        description=_(u"Details of CSI"),
        required=False,
    )
