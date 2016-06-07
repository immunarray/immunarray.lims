from zope import schema
from zope.interface import Interface
from immunarray.lims.content.organisation import IOrganisation
from immunarray.lims import _

class IPractice(IOrganisation):
    """Base fields for all organisation types
    """
    Firstname = schema.ASCIILine(
        title=_(u"Name"),
        description=_(u""),
        required=False,
    )
    EmailAddress = schema.ASCIILine(
        title=_(u"EmailAddress"),
        description=_(u""),
        required=False,
    )
    Phone = schema.ASCIILine(
        title=_(u"Phone number"),
        description=_(u""),
        required=False,
    )
