from zope import schema
from zope.interface import Interface
from immunarray.lims import messageFactory as _
from bika.lims.interfaces.person import IPerson


class IProvider(IPerson):
    """Care provider
    """
