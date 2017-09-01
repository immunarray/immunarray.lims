# -*- coding: utf-8 -*-
from immunarray.lims import messageFactory as _
from immunarray.lims.interfaces import BaseModel
from zope import schema


class ISample(BaseModel):
    """Common schema fields for all types of Samples
    """

    initial_volume = schema.Int(
        title=_(u"Initial Volume"),
        description=_(u"Volume of sample in micro liters (uL)"),
        required=True,
    )

    remaining_volume = schema.Int(
        title=_(u"Remaining Volume"),
        description=_(u"Remaining sample volume in micro liters (uL)"),
        required=True,
        readonly=True,
    )
