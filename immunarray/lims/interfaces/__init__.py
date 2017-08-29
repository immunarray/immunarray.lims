from immunarray.lims import messageFactory as _
from plone.supermodel import model
from zope import schema
from zope.interface import Interface


class BaseModel(model.Schema):
    """This is a base for all schema interfaces presented here. It contains 
    fields that we know will be present on all objects.
    """
    title = schema.TextLine(
        title=_(u"Title"),
        required=False,
    )


class IImmunarrayLayer(Interface):
    """Marker interface for the Browserlayer
    """


class IWorkingAliquot(Interface):
    """Marker interface to denote Working Aliquots
    """


class IBulkAliquot(Interface):
    """Marker interface to denote Bulk Aliquots
    """
