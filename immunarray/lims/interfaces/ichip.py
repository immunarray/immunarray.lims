# -*- coding: utf-8 -*-
from immunarray.lims import messageFactory as _
from plone.app.textfield import RichText
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.supermodel import model
from zope import schema


class IiChip(model.Schema):
    """An iChip Lot that will be the container class object
    """

    title = schema.TextLine(
        title=_(u"iChip ID"),
        required=True,
    )

    ichip_run_date = schema.TextLine(
        title=_(u"iChip Run Date"),
        description=_(u"Run Date of iChip (Read only)"),
        readonly=True,
        required=False,
    )

    ichip_status = schema.Choice(
        title=_(u"iChip Status"),
        description=_(u"Status of iChip"),
        required=True,
        values=[_(u'Quarantined'),
                _(u'Released'),
                _(u'Retained-US'),
                _(u'Retained-IA'),
                _(u'In-Process'),
                _(u'Used-QC-Passed'),
                _(u'Used-QC-Failed'),
                _(u'Residual'),
                _(u'Broken'),
                _(u'Used-Training'),
                _(u'Used-Validation')],
        default=_(u'Quarantined'),
    )

    # Image name to actual image (zip image file before upload)
    image = schema.Dict(
        key_value=schema.TextLine(
            title=_(u"Image Title (ie Agilent Red)"),
            descrition=_(u"Image Title (ie Agilent Red)"),
            required=False,
        ),
        value_type=NamedBlobImage(
            title=_(u"iChip Agilent Image"),
            description=_(u"Agilent Image of iChip (.tiff)"),
            required=False),
    )

    # Image extraction name to extraction
    image_extractions = schema.Dict(
        key_value=schema.TextLine(
            title=_(u"Image Extraction Title (ie Agilent Red)"),
            descrition=_(u"Image Extraction Title (ie Agilent Red)"),
            required=False,
        ),
        value_type=NamedBlobFile(
            title=_(u"iChip Agilent Image Extraction"),
            description=_(u"Agilent Image Extraction of iChip (.tiff)"),
            required=False),
    )

    # update to have vocabulary tied to choices
    storage_location = schema.Choice(
        title=_(u"iChip Storage Location"),
        description=_(u"Storage Location of iChip"),
        values=[_('EQ-76'), _('EQ-Unknown')],
        required=False,
    )

    # well to aliquot ID tested on it
    well_to_aliquot = schema.Dict(
        key_value=schema.TextLine(
            title=_(u"Well ID"),
            descrition=_(u"Well ID"),
            required=False,
        ),
        value_type=schema.TextLine(
            title=_(u"Aliquot ID"),
            descrition=_(u"Aliquot ID"),
            required=False,
        ),
    )

    comment = RichText(
        title=_(u"iChip Comment"),
        description=_(u"Comments about iChip"),
        required=False,
    )
