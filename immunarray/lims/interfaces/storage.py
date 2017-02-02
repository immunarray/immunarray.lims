from immunarray.lims import messageFactory as _
from plone.app.textfield import RichText
from plone.supermodel import model
from zope import schema


class IFreezer(model.Schema):
    """Not desired for ImmunArray"""
    pass

class IShelf(model.Schema):
    """Not desired for ImmunArray"""
    pass

class IRack(model.Schema):
    """Letters of the alphabet singel letter to double letter to tripple
    letter, have two types of racks and that determines the number of boxes
    it will hold.  (5x4=20 boxes, or 4x4=16 boxes)
    """

    title = schema.Choice(
        title=_(u"Rack ID"),
        description=_(u"Rack ID"),
        required=True,
        values=[_(u'A'),
                _(u'B'),
                _(u'C'),
                _(u'D'),
                _(u'E'),
                _(u'F'),
                _(u'G'),
                _(u'H')],
    )

    size = schema.Int(
        title = _(u'Rack Size'),
        description= _(u'Number of boxes rack can hold'),
    )


class ICommercialBox(model.Schema):
    """Boxes can hold either 100 sampels or 81 samples"""
    title = schema.TextLine(
        title = _(u''),
        description = _(u''),
        required=True,
    )

    max_samples = schema.Int(
        title=_(u'Max Number of Samples'),
        description=_(u'Max Number of Samples'),
        default=81,
    )

class IRandDBox(model.Schema):
    """Boxes can hold either 100 sampels or 81 samples"""
    title = schema.TextLine(
        title = _(u''),
        description = _(u''),
        required=True,
    )

    max_samples = schema.Int(
        title=_(u'Max Number of Samples'),
        description=_(u'Max Number of Samples'),
        default=81,
    )

class IAcidStorage(model.Schema):
    """Container that will hold all acidic items for the lab"""
    pass

class IBaseStorage(model.Schema):
    """Container that will hold all basic items for the lab"""
    pass

class INonHazardusStorage(model.Schema):
    """Container that will hold all non hazardus items for the lab
        Things like lab consumables gloves, tips ect
    """
    pass

class IPowerderStorage(model.Schema):
    """Container that will hold all chemical powders
    """
    pass

def make100samplebox(self):
    pass


def make90samplebox(self):
    pass



