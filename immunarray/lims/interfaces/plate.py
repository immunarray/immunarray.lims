from zope import schema
from zope.interface import Interface

from immunarray.lims import messageFactory as _
from plone.supermodel import model


class IPlateFolder(Interface):
    """Marker interface for a folder which contains Plate objects
    """


class IPlate96WellItem(model.Schema):
    """
    A 96 Well plate object
    """
    CustomerServiceItemID = schema.ASCIILine(
        title=_(u"Customer Service Item ID"),
        description=_(u"Customer Service Item ID"),
        required=True,
    )
