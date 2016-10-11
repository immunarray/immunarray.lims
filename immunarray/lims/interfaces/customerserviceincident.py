"""Interface for Customer Service Incident
"""
import datetime

from immunarray.lims import messageFactory as _
from plone.autoform import directives
from plone.supermodel import model
from zope import schema

class ICustomerServiceIncident (model.Schema);
    """Interface for Customer Service Incident CSI
    """
    csi_client = schema.Choice(
        title=_(u"Client"),
        description=_(u"Client"),
        required=True,
        values=[_(u'Quarantined'), _(u'Released')],
    )
    csi_instance =  schema.Choice(
        title=_(u"Instance Type"),
        description=_(u"Instance Type"),
        required=True,
        values=[_(u'Quarantined'), _(u'Released')],
    )
    csi_datetime = schema.Datetime(
        title=_(u"Date and Time of Instance"),
        description=_(u"Date and Time of Instance"),
        required=False,
    )
    csi_follow_up_needed = schema.Bool(
        title=_(u"Is Follow Up Needed"),
        description=_(u"Is Follow Up Needed"),
        required=False,
    )
    csi_status = schema.Choice(
        title=_(u"Status of CSI"),
        description=_(u"Status of CSI"),
        required=True,
        values=[_(u'Open'), _(u'Closed'), _(u'Held')],
    )
    csi_details = schema.Text(
        title =_(u"Details of CSI"),
        description=_(u"Details of CSI"),
        required=False,
    )
