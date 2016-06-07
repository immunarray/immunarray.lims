from zope import schema

from zope.interface import Interface

from immunarray.lims import messageFactory as _
from immunarray.lims.interfaces.person import IPerson


class IDoctorFolder(Interface):
    """Folder to hold test requisitions
    """


class IDoctor(IPerson):
    """
    """
    Firstname = schema.ASCIILine(
        title=_(u"Firstname"),
        description=_(u""),
        required=False,
    )
    Lastname = schema.ASCIILine(
        title=_(u"Lastname"),
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
