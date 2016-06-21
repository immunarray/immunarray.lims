from datetime import date
from plone.app.textfield import RichText
from plone.namedfile import field as namedfile
from plone.supermodel import model
from zope import schema

from immunarray.lims import messageFactory as _
from plone.dexterity.utils import createContentInContainer


class IiChip(model.Schema):
    """An iChip Lot that will be the container class object
    """

    # iChipLotCode = schema.TextLine(
    #        title=_(u"iChip Lot Code"),
    #        description=_(u"Code that could be use for external database longterm"),
    #        constraint=iChipLotCodeIsValid,
    #        )

    """iChipID = schema.TextLine(
        title=_(u"iChip ID"),
        description=_(u"ID of iChip"),
        required=True,
    )"""
    iChipLotRunDate = schema.Date(
        title=_(u"iChip Run Date"),
        description=_(u"Run Date of iChip"),
        required=False,
    )
    iChipStatus = schema.Choice(
        title=_(u"iChip Status"),
        description=_(u"Status of iChip"),
        required=True,
        values=[_(u'Quarantined'), _(u'Released'), _(u'Used'), _(u'Retained')],
    )
    iChipAgilentRed = namedfile.NamedBlobImage(
        title=_(u"iChip Agilent Red Image"),
        description=_(u"Agilent Red Image of iChip (.tiff)"),
        required=False,
    )
    iChipAgilentGreen = namedfile.NamedBlobImage(
        title=_(u"iChip Agilent Green Image"),
        description=_(u"Agilent Green Image of iChip (.tiff)"),
        required=False,
    )
    iChipGenePixRed = namedfile.NamedBlobImage(
        title=_(u"iChip GenePix Red Feature Extraction"),
        description=_(u"GenePix Red Feature Extraction of iChip (.gpr)"),
        required=False,
    )
    iChipGenePixGreen = namedfile.NamedBlobImage(
        title=_(u"iChip GenePix Green Feature Extraction"),
        description=_(u"GenePix Green Feature Extraction of iChip (.gpr)"),
        required=False,
    )
    iChipStorageLocation = schema.Choice(
        title=_(u"iChip Storage Location"),
        description=_(u"Storage Location of iChip"),
        values=[_('EQ-76'), _('EQ-Unknown')],
        required=False,
    )
    iChipWellA = schema.TextLine(
        title=_(u"iChip Well A"),
        description=_(u"Aliquot ID of Sample Placed in iChip Well A"),
        required=False,
    )
    iChipWellB = schema.TextLine(
        title=_(u"iChip Well B"),
        description=_(u"Aliquot ID of Sample Placed in iChip Well B"),
        required=False,
    )
    iChipWellC = schema.TextLine(
        title=_(u"iChip Well C"),
        description=_(u"Aliquot ID of Sample Placed in iChip Well C"),
        required=False,
    )
    iChipWellD = schema.TextLine(
        title=_(u"iChip Well D"),
        description=_(u"Aliquot ID of Sample Placed in iChip Well D"),
        required=False,
    )
    iChipWellE = schema.TextLine(
        title=_(u"iChip Well E"),
        description=_(u"Aliquot ID of Sample Placed in iChip Well E"),
        required=False,
    )
    iChipWellF = schema.TextLine(
        title=_(u"iChip Well F"),
        description=_(u"Aliquot ID of Sample Placed in iChip Well F"),
        required=False,
    )
    iChipWellG = schema.TextLine(
        title=_(u"iChip Well G"),
        description=_(u"Aliquot ID of Sample Placed in iChip Well G"),
        required=False,
    )
    iChipWellH = schema.TextLine(
        title=_(u"iChip Well H"),
        description=_(u"Aliquot ID of Sample Placed in iChip Well H"),
        required=False,
    )
    iChipComment = RichText(
        title=_(u"iChip Comment"),
        description=_(u"Comments about iChip"),
        required=False,
    )

