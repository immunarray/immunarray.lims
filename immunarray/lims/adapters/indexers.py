from immunarray.lims.interfaces.aliquot import IAliquot
from immunarray.lims.interfaces.ichipassay import IiChipAssay
from immunarray.lims.interfaces.ichiplot import IiChipLot
from plone.indexer import indexer
import datetime as dt


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

@indexer(IiChipLot)
def ichiplot_expires(instance):
    """iChipLot ichip_lot_expiration_date populates 'expires' index
    """
    return dt.datetime.combine(instance.ichip_lot_expiration_date, dt.time.min)
