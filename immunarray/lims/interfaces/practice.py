from bika.lims.interfaces.organisation import IOrganisation
from immunarray.lims import messageFactory as _
from zope import schema


class IPractice(IOrganisation):
    """Base fields for all organisation types
    """
    FirstName = schema.TextLine(
        title=_(u"First name of primary pratice contact"),
        description=_(u"First name of primary pratice contact"),
        required=False,
    )
    LastName = schema.TextLine(
        title=_(u"Last name of primay practice contact"),
        description=_(u"Last name of primay practice contact"),
        required=False,
    )
    Fax = schema.TextLine(
        title=_(u"Fax number"),
        description=_(u"Fax number of practice"),
        required=False,
    )
    Address = schema.TextLine(
        title=_(u"Address"),
        description=_(u"Address of practice"),
        required=False,
    )
    Suite = schema.TextLine(
        title=_(u"Suite"),
        description=_(u"Suite of practice"),
        required=False,
    )
    City = schema.TextLine(
        title=_(u"City"),
        description=_(u"City"),
        required=False,
    )
    State = schema.TextLine(
        title=_(u"State"),
        description=_(u"State"),
        required=False,
    )
    """Should/Could we do a format or XXXXX-XXXX"""
    ZipCode = schema.TextLine(
        title=_(u"Zip Code"),
        description=_(u"Zip Code"),
        required=False,
    )
    TherapakID = schema.Int(
        title = _(u"ThearaPak Site ID"),
        description=_(u"ThearaPak Site ID"),
        required=True,
    )
    MegaPracticeID = schema.Int(
        title = _(u"Mega Pratice ID"),
        description=_(u"ID used to link multiple practices as one entity"),
        required=True,
    )
