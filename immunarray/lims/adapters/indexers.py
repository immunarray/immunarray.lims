from immunarray.lims.interfaces.aliquot import IAliquot
from immunarray.lims.interfaces.ichipassay import IiChipAssay
from immunarray.lims.interfaces.ichiplot import IiChipLot
from immunarray.lims.interfaces.material import IMaterial
from immunarray.lims.interfaces.solution import ISolution
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

@indexer(IMaterial)
def material_remaining_volume(instance):
    """populate "remaining_volume" index with "remaining_amount" field value
    """
    return instance.remaining_amount

@indexer(ISolution)
def solution_remaining_volume(instance):
    """populate "remaining_volume" index with "remaining_amount" field value
    """
    return instance.remaining_amount
