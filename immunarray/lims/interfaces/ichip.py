from datetime import date
from plone.app.textfield import RichText
from plone.namedfile import field as namedfile
from plone.supermodel import model
from zope import schema

from immunarray.lims import messageFactory as _
from plone.dexterity.utils import createContentInContainer


class IIChip(model.Schema):
    """An IChip Lot that will be the container class object
    """

    # IChipLotCode = schema.TextLine(
    #        title=_(u"IChip Lot Code"),
    #        description=_(u"Code that could be use for external database longterm"),
    #        constraint=IChipLotCodeIsValid,
    #        )

    """IChipID = schema.TextLine(
        title=_(u"IChip ID"),
        description=_(u"ID of IChip"),
        required=True,
    )"""
    IChipLotRunDate = schema.Date(
        title=_(u"IChip Run Date"),
        description=_(u"Run Date of IChip"),
        required=False,
    )
    IChipStatus = schema.Choice(
        title=_(u"IChip Status"),
        description=_(u"Status of IChip"),
        required=True,
        values=[_(u'Quarantined'), _(u'Released'), _(u'Used'), _(u'Retained')],
    )
    IChipAgilentRed = namedfile.NamedBlobImage(
        title=_(u"IChip Agilent Red Image"),
        description=_(u"Agilent Red Image of IChip (.tiff)"),
        required=False,
    )
    IChipAgilentGreen = namedfile.NamedBlobImage(
        title=_(u"IChip Agilent Green Image"),
        description=_(u"Agilent Green Image of IChip (.tiff)"),
        required=False,
    )
    IChipGenePixRed = namedfile.NamedBlobImage(
        title=_(u"IChip GenePix Red Feature Extraction"),
        description=_(u"GenePix Red Feature Extraction of IChip (.gpr)"),
        required=False,
    )
    IChipGenePixGreen = namedfile.NamedBlobImage(
        title=_(u"IChip GenePix Green Feature Extraction"),
        description=_(u"GenePix Green Feature Extraction of IChip (.gpr)"),
        required=False,
    )
    IChipStorageLocation = schema.Choice(
        title=_(u"IChip Storage Location"),
        description=_(u"Storage Location of IChip"),
        values=[_('EQ-76'), _('EQ-Unknown')],
        required=False,
    )
    IChipWellA = schema.TextLine(
        title=_(u"iChip Well A"),
        description=_(u"Aliquot ID of Sample Placed in iChip Well A"),
        required=False,
    )
    IChipWellB = schema.TextLine(
        title=_(u"iChip Well B"),
        description=_(u"Aliquot ID of Sample Placed in iChip Well B"),
        required=False,
    )
    IChipWellC = schema.TextLine(
        title=_(u"iChip Well C"),
        description=_(u"Aliquot ID of Sample Placed in iChip Well C"),
        required=False,
    )
    IChipWellD = schema.TextLine(
        title=_(u"iChip Well D"),
        description=_(u"Aliquot ID of Sample Placed in iChip Well D"),
        required=False,
    )
    IChipWellE = schema.TextLine(
        title=_(u"iChip Well E"),
        description=_(u"Aliquot ID of Sample Placed in iChip Well E"),
        required=False,
    )
    IChipWellF = schema.TextLine(
        title=_(u"iChip Well F"),
        description=_(u"Aliquot ID of Sample Placed in iChip Well F"),
        required=False,
    )
    IChipWellG = schema.TextLine(
        title=_(u"iChip Well G"),
        description=_(u"Aliquot ID of Sample Placed in iChip Well G"),
        required=False,
    )
    IChipWellH = schema.TextLine(
        title=_(u"iChip Well H"),
        description=_(u"Aliquot ID of Sample Placed in iChip Well H"),
        required=False,
    )
    IChipComment = RichText(
        title=_(u"IChip Comment"),
        description=_(u"Comments about IChip"),
        required=False,
    )

