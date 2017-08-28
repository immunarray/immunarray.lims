from zope import schema
from plone.supermodel import model
from immunarray.lims import messageFactory as _

class ISample(model.Schema):
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

