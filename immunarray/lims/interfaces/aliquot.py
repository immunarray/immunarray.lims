from zope import schema

from zope.interface import Interface

from immunarray.lims import messageFactory as _
from plone.supermodel import model


class IAliquotFolder(Interface):
    """Folder to hold aliquot
    """


class IAliquot(model.Schema):
    """Object that can hold other aliquots, or be an aliquot
    """
    PourDate = schema.Date(
        title=_(u"Date of Aliquot Pour"),
        description=_(u"Date of Aliquot Pour"),
        required=True,
    )
    FluidType = schema.Choice(
        title=_(u"Fluid Type"),
        description=_(u"Fluid Type"),
        values=[_(u"Serum"),
                _(u"Plasma"),
                _(u"CSF"),
                _(u"Whole Blood")],
        default=u"Serum",
        required=True,
    )
    Use = schema.Choice(
        title=_(u"Use of Aliquot"),
        description=_(u"Use of Aliquot Bulk or Working"),
        values=[_(u"Bulk"),
                _(u"Working"),
                _(u"Quality Control"),
                _(u"Other")],
        default=u"Bulk",
        required=True,
    )
    Department = schema.Choice(
        title=_(u"Department"),
        description=_(u"Department Expected to use Aliquot"),
        values=[_(u"Clinical"),
                _(u"R&D"),
                _(u"Other")],
        default=u"Clinical",
        required=True,
    )
    StorageLocation = schema.ASCIILine(
        title=_(u"Storage Location of Aliquot"),
        description=_(u"Storage Location of Aliquot"),
        required=False,
    )
    Volume = schema.Float(
        title=_(u"Volume of Material in uL"),
        description=_(u"volume of Material in uL"),
        required=True,
    )
    Status = schema.Choice(
        title=_(u"Aliquot Status"),
        description=_(u"Aliquot Status Available/Consumed"),
        values=[_(u"Available"),
                _(u"Consumed")],
        default=u"Available",
        required=True,
    )
