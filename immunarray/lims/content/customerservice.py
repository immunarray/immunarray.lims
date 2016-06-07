from zope import schema
from zope.interface import Interface

from immunarray.lims import _
from plone.supermodel import model



class ICustomerServiceFolder(Interface):
    """Marker interface for a folder which contains Customer Service Clients objects
    """

class ICustomerServiceClientFolder(model.Schema):
    """Object that holds customer service items
    """
    CustomerServiceClientFolderID = schema.ASCIILine(
            title =_(u"Customer Service Item ID"),
            description=_(u"Customer Service Item ID"),
            required=True,
    )

class ICustomerServiceItem(model.Schema):
    """
    Pull all techs and managers and put into a list, use that as the values list for MaterialReciviedBy and MaterialOpenedBy
    """
    CustomerServiceItemID = schema.ASCIILine(
            title =_(u"Customer Service Item ID"),
            description=_(u"Customer Service Item ID"),
            required=True,
    )
