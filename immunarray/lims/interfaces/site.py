from zope import schema
from zope.interface import Interface
from immunarray.lims import messageFactory as _
from bika.lims.interfaces.organisation import IOrganisation


class ISite(IOrganisation):
    """ Commercial Site
    """
    title = schema.TextLine(
        title=_(u"Site ID"),
        description=_(u"Site ID"),
        required=False,
    )
