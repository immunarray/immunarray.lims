# -*- coding: utf-8 -*-
from zope import schema
from zope.interface import Interface
from immunarray.lims import messageFactory as _
from bika.lims.interfaces.organisation import IOrganisation


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
        required=False,
    )

    free_kits_left = schema.Int(
        title=_(u"Free Kits Left"),
        description=_(u"Free Kits Left"),
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
