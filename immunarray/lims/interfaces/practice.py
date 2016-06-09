from zope import schema
from zope.interface import Interface
from immunarray.lims.interfaces.organisation import IOrganisation
from immunarray.lims import messageFactory as _

class IPractice(IOrganisation):
    """Base fields for all organisation types
    Name = schema.ASCIILine(
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
    """
    FirstName = schema.ASCIILine(
        title=_(u"First name of primary pratice contact"),
        description=_(u"First name of primary pratice contact"),
        required=False,
    )
    LastName = schema.ASCIILine(
        title=_(u"Last name of primay practice contact"),
        description=_(u"Last name of primay practice contact"),
        required=False,
    )
    Fax = schema.ASCIILine(
        title=_(u"Fax number"),
        description=_(u"Fax number of practice"),
        required=False,
    )
    Address = schema.ASCIILine(
        title=_(u"Address"),
        description=_(u"Address of practice"),
        required=False,
    )
    Suite = schema.ASCIILine(
        title=_(u"Suite"),
        description=_(u"Suite of practice"),
        required=False,
    )
    City = schema.ASCIILine(
        title=_(u"City"),
        description=_(u"City"),
        required=False,
    )
    State = schema.ASCIILine(
        title=_(u"State"),
        description=_(u"State"),
        required=False,
    )
    """Should/Could we do a format or XXXXX-XXXX"""
    ZipCode = schema.ASCIILine(
        title=_(u"Zip Code"),
        description=_(u"Zip Code"),
        required=False,
    )
    ThearapakID = schema.Int(
        title = _(u"ThearaPak Site ID"),
        description=_(u"ThearaPak Site ID"),
        required=True,
    )
    MegaPraticeID = schema.Int(
        title = _(u"Mega Pratice ID"),
        description=_(u"ID used to link multiple practices as one entity"),
        required=True,
    )
