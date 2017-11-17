# -*- coding: utf-8 -*-

from zope import schema

from immunarray.lims import logger
from immunarray.lims import messageFactory as _
from immunarray.lims.interfaces import BaseModel
from plone.api.content import find
from zope.interface import implements
from zope.schema import List
from zope.schema.interfaces import IContextAwareDefaultFactory


class assignBoxNumber():
    """All boxes use this as the default value of their
    box_number fields, allows for a consistent number system.
    """
    implements(IContextAwareDefaultFactory)

    def __init__(self):
        pass

    def __call__(self, context):
        """Pull all box numbers and get the next one.
        """
        brains = find(portal_type=['CommercialBox', 'RandDBox', 'QCBox'],
                      sort_on='box_number',
                      sort_order='reverse', limit=1)
        if brains:
            _id = str(int(brains[0].box_number) + 1)
            return unicode(_id)
        logger.info("assignBoxNumber: No Boxes Exist: using ID '1'")
        return u"1"

class IFreezer(BaseModel):
    """Not desired for ImmunArray"""
    pass


class IShelf(BaseModel):
    """Not desired for ImmunArray"""
    pass


class IRack(BaseModel):
    """Letters of the alphabet single letter to double letter to triple
    letter, have two types of racks and that determines the number of boxes
    it will hold.  (5x4=20 boxes, or 4x4=16 boxes)
    """

    rack_name = schema.TextLine(
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

    remaining_volume = schema.Int(
        title=_(u"Remaining Rack Spaces"),
        description=_(u"Remaining Rack Spaces"),
        required=True,
    )


class ICommercialBox(BaseModel):
    """Boxes can hold either 100 sampels or 81 samples"""
    #tmp_box_number = assignBoxNumber()

    box_number = schema.TextLine(
        title=_(u'R&D Box Number'),
        description=_(u'R&D Box Number'),
        defaultFactory=assignBoxNumber(),
        #default=assignBoxNumber(),
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

    remaining_volume = schema.Int(
        title=_(u"Remaining Aliquot Spaces"),
        description=_(u"Remaining Aliquot Spaces"),
        required=True,
    )

    aliquot_dic = schema.Dict(
        title=_(u'Box Count to Aliquot ID'),
        required=False,
        key_type=schema.TextLine(
            title=_(u"Box Count"),
            description=_(u"Box Count"),
            required=False,
        ),
        value_type=List(
            title=_(u"Aliquot ID, UID"),
            description=_(u"Aliquot ID, UID"),
            required=False,
        )
    )


class IRandDBox(BaseModel):
    """Boxes can hold either 100 sampels or 81 samples"""
    box_number = schema.TextLine(
        title=_(u'R&D Box Number'),
        description=_(u'R&D Box Number'),
        defaultFactory=assignBoxNumber(),
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

    remaining_volume = schema.Int(
        title=_(u"Remaining Aliquot Spaces"),
        description=_(u"Remaining Aliquot Spaces"),
        required=True,
    )

    aliquot_dic = schema.Dict(
        title=_(u'Box Count to Aliquot ID'),
        required=False,
        key_type=schema.TextLine(
            title=_(u"Box Count"),
            description=_(u"Box Count"),
            required=False,
        ),
        value_type=List(
            title=_(u"Aliquot ID, UID"),
            description=_(u"Aliquot ID, UID"),
            required=False,
        )
    )


class IQCBox(BaseModel):
    """Boxes can hold either 100 sampels or 81 samples"""
    box_number = schema.TextLine(
        title=_(u'QC Box Number'),
        description=_(u'QC Box Number'),
        defaultFactory=assignBoxNumber(),
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

    remaining_volume = schema.Int(
        title=_(u"Remaining Aliquot Spaces"),
        description=_(u"Remaining Aliquot Spaces"),
        required=True,
    )

    aliquot_dic = schema.Dict(
        title=_(u'Box Count to Aliquot ID'),
        required=False,
        key_type=schema.TextLine(
            title=_(u"Box Count"),
            description=_(u"Box Count"),
            required=False,
        ),
        value_type=List(
            title=_(u"Aliquot ID, UID"),
            description=_(u"Aliquot ID, UID"),
            required=False,
        )
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


