from zope import schema
from zope.interface import Interface
from immunarray.lims import messageFactory as _
from bika.lims.interfaces.organisation import IOrganisation


class ISite(IOrganisation):
    """Care provider
    """
    pass