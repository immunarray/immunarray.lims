from bika.lims.interfaces.organisation import IOrganisation
from immunarray.lims import messageFactory as _
from zope import schema


class IPractice(IOrganisation):
    """Base fields for all organisation types
    """
    contact_name = schema.TextLine(
        title=_(u"First name of primary pratice contact"),
        description=_(u"First name of primary pratice contact"),
        required=False,
    )
    therapak_id = schema.Int(
        title = _(u"ThearaPak Site ID"),
        description=_(u"ThearaPak Site ID"),
        required=True,
    )
    megapractice_id = schema.Int(
        title = _(u"Mega Pratice ID"),
        description=_(u"ID used to link multiple practices as one entity"),
        required=True,
    )
    fax_number = schema.TextLine(
        title=_(u"Fax Number"),
        required=False,
    )
    inbound_shipping_method = schema.Choice(
        title=_(u"Inbound Shipping Method"),
        description=_(u"Inbound Shipping Method"),
        required="True",
        values=[_(u"Fed-Ex"), _(u"UPS")],
    )
    kits_on_site = schema.Int(
        title=_(u"Kits on Site"),
        description=_(u"Kits on Site"),
        required="True",
    )
