from datetime import date
from plone.app.textfield import RichText
from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model
from zope import schema

from immunarray.lims import messageFactory as _
from plone.dexterity.utils import createContentInContainer


class IiChip(model.Schema):
    """An iChip Lot that will be the container class object
    """

    ichip_lot_run_date = schema.Date(
        title=_(u"iChip Run Date"),
        description=_(u"Run Date of iChip"),
        required=False,
    )

    ichip_status = schema.Choice(
        title=_(u"iChip Status"),
        description=_(u"Status of iChip"),
        required=True,
        values=[_(u'Quarantined'), _(u'Released'), _(u'Retained'), _(u'Inprocess'), _(u'Used-QC-Passed'), _(u'Used-QC-Failed'), _(u'Residual')],
    )

    ichip_agilent_red = NamedBlobImage(
        title=_(u"iChip Agilent Red Image"),
        description=_(u"Agilent Red Image of iChip (.tiff)"),
        required=False,
    )

    ichip_agilent_green = NamedBlobImage(
        title=_(u"iChip Agilent Green Image"),
        description=_(u"Agilent Green Image of iChip (.tiff)"),
        required=False,
    )

    ichip_genepix_red = NamedBlobImage(
        title=_(u"iChip GenePix Red Feature Extraction"),
        description=_(u"GenePix Red Feature Extraction of iChip (.gpr)"),
        required=False,
    )

    ichip_genepix_green = NamedBlobImage(
        title=_(u"iChip GenePix Green Feature Extraction"),
        description=_(u"GenePix Green Feature Extraction of iChip (.gpr)"),
        required=False,
    )

    ichip_storage_location = schema.Choice(
        title=_(u"iChip Storage Location"),
        description=_(u"Storage Location of iChip"),
        values=[_('EQ-76'), _('EQ-Unknown')],
        required=False,
    )

    ichip_well_a = schema.TextLine(
        title=_(u"iChip Well A"),
        description=_(u"Aliquot ID of Sample Placed in iChip Well A"),
        required=False,
    )

    ichip_well_b = schema.TextLine(
        title=_(u"iChip Well B"),
        description=_(u"Aliquot ID of Sample Placed in iChip Well B"),
        required=False,
    )

    ichip_well_c = schema.TextLine(
        title=_(u"iChip Well C"),
        description=_(u"Aliquot ID of Sample Placed in iChip Well C"),
        required=False,
    )

    ichip_well_d = schema.TextLine(
        title=_(u"iChip Well D"),
        description=_(u"Aliquot ID of Sample Placed in iChip Well D"),
        required=False,
    )

    ichip_well_e = schema.TextLine(
        title=_(u"iChip Well E"),
        description=_(u"Aliquot ID of Sample Placed in iChip Well E"),
        required=False,
    )

    ichip_well_f = schema.TextLine(
        title=_(u"iChip Well F"),
        description=_(u"Aliquot ID of Sample Placed in iChip Well F"),
        required=False,
    )

    ichip_well_g = schema.TextLine(
        title=_(u"iChip Well G"),
        description=_(u"Aliquot ID of Sample Placed in iChip Well G"),
        required=False,
    )

    ichip_well_h = schema.TextLine(
        title=_(u"iChip Well H"),
        description=_(u"Aliquot ID of Sample Placed in iChip Well H"),
        required=False,
    )

    ichip_comment = RichText(
        title=_(u"iChip Comment"),
        description=_(u"Comments about iChip"),
        required=False,
    )

