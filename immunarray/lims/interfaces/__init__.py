from zope.interface import Interface


class IImmunarrayLayer(Interface):
    """Marker interface for the Browserlayer
    """


class IWorkingAliquot(Interface):
    """Marker interface to denote Working Aliquots
    """


class IBulkAliquot(Interface):
    """Marker interface to denote Bulk Aliquots
    """
