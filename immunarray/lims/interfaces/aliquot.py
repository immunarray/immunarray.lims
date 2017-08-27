from zope import schema
from plone.supermodel import model


class IAliquot(model.Schema):
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
        readonly=True,
    )

