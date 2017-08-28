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


class IQCSample(Interface):
    """Marker interface to denote QC Sample
    """

class IRandDSample(Interface):
    """Marker interface to denote RandD Sample
    """
