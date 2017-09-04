# -*- coding: utf-8 -*-
from zope import schema

from immunarray.lims import messageFactory as _
from immunarray.lims.interfaces import BaseModel


class IFreezer(BaseModel):
    """Not desired for ImmunArray"""
    pass


class IShelf(BaseModel):
    """Not desired for ImmunArray"""
    pass


class IRack(BaseModel):
    """Letters of the alphabet singel letter to double letter to tripple
    letter, have two types of racks and that determines the number of boxes
    it will hold.  (5x4=20 boxes, or 4x4=16 boxes)
    """

    title = schema.TextLine(
        title=_(u"Rack ID"),
        description=_(u"Rack ID"),
        required=True,
    )

    size = schema.Int(
        title=_(u'Rack Size'),
        description=_(u'Number of boxes rack can hold'),
    )

    freezer = schema.TextLine(
        title=_(u"Freezer"),
        description=_(u"Freezer where rack is stored"),
        required=True,
    )


class ICommercialBox(BaseModel):
    """Boxes can hold either 100 sampels or 81 samples"""
    box_number = schema.TextLine(
        title=_(u'Box Number'),
        description=_(u'Box Number'),
        required=True,
    )

    box_type = schema.Choice(
        title=_(u"Sample Type"),
        description=_(u"Sample Type"),
        values=[_(u"Bulk"), _(u"Working")],
        required=True,
    )

    max_samples = schema.Int(
        title=_(u'Max Number of Samples'),
        description=_(u'Max Number of Samples'),
        default=81,
    )


class IRandDBox(BaseModel):
    """Boxes can hold either 100 sampels or 81 samples"""
    box_number = schema.TextLine(
        title=_(u'R&D Box Number'),
        description=_(u'R&D Box Number'),
        required=True,
    )

    max_samples = schema.Int(
        title=_(u'Max Number of Samples'),
        description=_(u'Max Number of Samples'),
        default=81,
    )


class IAcidStorage(BaseModel):
    """Container that will hold all acidic items for the lab"""
    pass


class IBaseStorage(BaseModel):
    """Container that will hold all basic items for the lab"""
    pass


class INonHazardusStorage(BaseModel):
    """Container that will hold all non hazardus items for the lab
        Things like lab consumables gloves, tips ect
    """
    pass


class IPowerderStorage(BaseModel):
    """Container that will hold all chemical powders
    """
    pass


def make100samplebox(self):
    pass


def make90samplebox(self):
    pass
