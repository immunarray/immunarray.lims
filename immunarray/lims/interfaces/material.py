"""To add custome slide content to immunarray.lims
"""

from zope import schema

from immunarray.lims import messageFactory as _
from plone.indexer import indexer
from plone.namedfile import field as namedfile
from plone.supermodel import model
class IMaterialsFolder(Interface):
    """Marker interface for a folder which contains Materials
    (raw materials) objects
    """

class IMaterial(model.Schema):
    """Base schema fields common to all Material types.
    """
    # subverting Plone's default 'Type' index, which is normally
    # derived from the Title of the FTI.
    Type = schema.ASCIILine(
        title=_(u"Type"),
        description=_(u"Type of material"),
        required=True,
    )
    LotNumber = schema.ASCIILine(
        title=_(u"Lot"),
        description=_(u"The identifier Lot of Casein Salt"),
        required=True,
    )
    Vendor = schema.ASCIILine(
        title=_(u"Vendor"),
        description=_(u"The vendor that supplied the lot"),
        required=True,
    )
    CatalogNumber = schema.ASCIILine(
        title=_(u"Catalog Number"),
        description=_(u"The lot's catalog number"),
        required=True,
    )
    ArrivalDate = schema.Date(
        title=_(u"Arrival Date"),
        description=_(u"The date on which the lot arrived"),
        required=True,
    )
    ExpirationDate = schema.Date(
        title=_(u"Expiration Date"),
        description=_(
            u"The date on which the lot expires and becomes unusable"),
        required=True,
    )
    COA = namedfile.NamedBlobImage(
        title=_(u"Certificate of Analysis"),
        description=_(u"Certificate of Analysis"),
        required=True,
    )
    ArrivalAmount = schema.ASCIILine(
        title=_(u"Amount of material at time of arrival"),
        description=_(u"Specify with SI units, eg: 1cm/2, 1', 20g, or 1kg."),
        required=False,
    )
    CurrentAmount = schema.ASCIILine(
        title=_(u"Amount of material currently remaining"),
        description=_(u"Specify with SI units, eg: 1cm/2, 1', 20g, or 1kg."),
        required=False,
    )
    ReceivedBy = schema.Choice(
        title=_(u"Received by"),
        description=_(u"The operator that received the material lot"),
        vocabulary=u"plone.principalsource.Users",
        required=False,  # value will be completed by workflow transition
    )
    OpenedBy = schema.Choice(
        title=_(u"Opened by"),
        description=_(u"The operator that Opened the material lot"),
        vocabulary=u"plone.principalsource.Users",
        required=False,  # value will be completed by workflow transition
    )
