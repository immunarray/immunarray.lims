from bika.lims.interfaces.organisation import IOrganisation
from immunarray.lims import messageFactory as _
from zope import schema


class IPractice(IOrganisation):
    """Base fields for all organisation types
    """
    contact_first_name = schema.TextLine(
        title=_(u"First name of primary pratice contact"),
        description=_(u"First name of primary pratice contact"),
        required=False,
    )
    contact_last_name = schema.TextLine(
        title=_(u"Last name of primay practice contact"),
        description=_(u"Last name of primay practice contact"),
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
