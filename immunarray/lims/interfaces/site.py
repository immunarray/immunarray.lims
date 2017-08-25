# -*- coding: utf-8 -*-
from zope import schema

from Products.CMFPlone.utils import safe_hasattr
from bika.lims.interfaces.organisation import IOrganisation
from immunarray.lims import messageFactory as _
from plone.app.content.interfaces import INameFromTitle
from plone.rfc822.interfaces import IPrimaryFieldInfo
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer


class ISite(IOrganisation):
    """ Commercial Site
    """
    title = schema.TextLine(
        title=_(u"Therapak ID"),
        description=_(u"Therapak ID"),
        required=False,
    )

    site_name = schema.TextLine(
        title=_(u"Site Name"),
        description=_(u"Site Name"),
        required=False,
    )

    sales_rep = schema.Bool(
        title=_(u"Sales Representative"),
        description=_(u"Site is a Sales Representative"),
        default=False,
        required=True,
    )

    setup_by = schema.TextLine(
        title=_(u"Setup By"),
        description=_(u"Setup By"),
        required=False,
    )

    primary_provider = schema.TextLine(
        title=_(u"Primary Provider"),
        description=_(u"Primary Provider"),
        required=False,
    )

    fax_number = schema.TextLine(
        title=_(u"Fax Number"),
        description=_(u"Fax Number"),
        required=False,
    )

    fax_confirmed = schema.Bool(
        title=_(u"Fax Number Confirmed"),
        description=_(u"Fax Number Confirmed"),
        required=False,
        default=False,
    )

    megapractice_id = schema.TextLine(
        title=_(u"Mega Practice ID"),
        description=_(u"Link multiple sites together"),
        required=False,
    )

    inbound_shipping_method = schema.Choice(
        title=_(u"Inbound Shipping Method"),
        description=_(u"Inbound Shipping Method"),
        values = [(u'FedEx'),(u'UPS')],
        required=False,
    )

    kits_on_site = schema.Int(
        title=_(u"Kits on Site"),
        description=_(u"Kits on Site"),
        default=0,
        required=False,
    )

    free_kits_left = schema.Int(
        title=_(u"Free Kits Left"),
        description=_(u"Free Kits Left"),
        default=0,
        required=False,
    )

    primary_contact = schema.TextLine(
        title=_(u"Primary Site Contact"),
        description=_(u"Primary Site Contact"),
        required=False,
    )

    primary_contact_phone = schema.TextLine(
        title=_(u"Primary Office Contact Phone Number"),
        description=_(u"Primary Office Contact Phone Number"),
        required=False,
    )

    site_notes = schema.Text(
        title=_(u"Site Notes"),
        description=_(u"Site Notes"),
        required=False,
    )


class INameFromFileName(Interface):
    """Marker interface to enable name from filename behavior"""


@implementer(INameFromTitle)
@adapter(INameFromFileName)
class NameFromFileName(object):

    def __new__(cls, context):
        info = IPrimaryFieldInfo(context, None)
        if info is None:
            return None
        filename = getattr(info.value, 'filename', None)
        if not isinstance(filename, basestring) or not filename:
            return None
        instance = super(NameFromFileName, cls).__new__(cls)
        instance.title = filename
        if safe_hasattr(context, 'title') and not context.title:
            context.title = filename
        return instance

    def __init__(self, context):
        pass
