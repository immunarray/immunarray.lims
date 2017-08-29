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
        readonly=True,
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


class ISamples(Interface):
    """Marker interface for navigation-root folder
    """


class ISites(Interface):
    """Marker interface for navigation-root folder
    """


class IMaterials(Interface):
    """Marker interface for navigation-root folder
    """


class ISolutions(Interface):
    """Marker interface for navigation-root folder
    """


class IiChipLots(Interface):
    """Marker interface for navigation-root folder
    """


class ITestRuns(Interface):
    """Marker interface for navigation-root folder
    """


class INonConformanceEvents(Interface):
    """Marker interface for navigation-root folder
    """


class IInventory(Interface):
    """Marker interface for navigation-root folder
    """


class IPatients(Interface):
    """Marker interface for navigation-root folder
    """


class IProviders(Interface):
    """Marker interface for navigation-root folder
    """


class IiChipAssays(Interface):
    """Marker interface for navigation-root folder
    """


class IConfiguration(Interface):
    """Marker interface for navigation-root folder
    """
