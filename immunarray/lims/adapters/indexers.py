from immunarray.lims.interfaces.aliquot import IAliquot
from immunarray.lims.interfaces.ichipassay import IiChipAssay
from plone.indexer import indexer


@indexer(IAliquot)
def aliquot_Type(instance):
    """Append (aliquot_type) to IAliquot Type index values.
    """
    return "{} ({})".format(instance.Type(), instance.aliquot_type)

@indexer(IiChipAssay)
def ichipassay_Type(instance):
    """Append the ichip-assay (status) to the Type for iChipAssays.
    """
    return "{} ({})".format(instance.Type(), instance.status)
