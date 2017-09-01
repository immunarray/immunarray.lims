# -*- coding: utf-8 -*-
from immunarray.lims import messageFactory as _
from immunarray.lims.interfaces import BaseModel
from zope import schema


class IAliquot(BaseModel):
    """Common schema fields for all types of Aliquots
    """

    initial_volume = schema.Int(
        title=_(u"Initial Volume"),
        description=_(u"Volume of aliquot in micro liters (uL)"),
        required=True,
    )

    remaining_volume = schema.Int(
        title=_(u"Remaining Volume"),
        description=_(u"Remaining aliquot volume in micro liters (uL)"),
        required=True,
    )
