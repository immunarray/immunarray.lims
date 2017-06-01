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

    name = schema.TextLine(
        title=_(u"Site Name"),
        description=_(u"Site Name"),
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

    megapractice_id = schema.TextLine(
        title=_(u"Mega Practice ID"),
        description=_(u"Link multiple sites together"),
        required=False,
    )

    inbound_shipping_method = schema.Choice(
        title=_(u"Inbound Shipping Method"),
        description=_(u"Inbound Shipping Method"),
        values = [(u'FedEX'),(u'UPS')],
        required=False,
    )

    kits_on_site = schema.Int(
        title=_(u"Kits on Site"),
        description=_(u"Kits on Site"),
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
