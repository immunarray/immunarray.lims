# -*- coding: utf-8 -*-
from immunarray.lims import messageFactory as _
from immunarray.lims.interfaces import BaseModel
from plone.app.textfield import RichText
from plone.namedfile.field import NamedBlobFile, NamedBlobImage
from zope import schema


class IiChip(BaseModel):
    """An iChip Lot that will be the container class object
    """

    ichip_id = schema.TextLine(
        title=_(u"iChip ID"),
        required=True,
    )

    ichip_run_date = schema.TextLine(
        title=_(u"iChip Run Date"),
        description=_(u"Run Date of iChip (Read only)"),
        readonly=True,
        required=False,
    )

    # Image name to actual image (zip image file before upload)
    image = schema.Dict(
        key_type=schema.TextLine(
            title=_(u"Image Title (ie Agilent Red)"),
            description=_(u"Image Title (ie Agilent Red)"),
            required=False,
        ),
        value_type=NamedBlobImage(
            title=_(u"iChip Agilent Image"),
            description=_(u"Agilent Image of iChip (.tiff)"),
            required=False),
    )

    # Image extraction name to extraction
    image_extractions = schema.Dict(
        key_type=schema.TextLine(
            title=_(u"Image Extraction Title (ie Agilent Red)"),
            description=_(u"Image Extraction Title (ie Agilent Red)"),
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
        key_type=schema.TextLine(
            title=_(u"Well ID"),
            description=_(u"Well ID"),
            required=False,
        ),
        value_type=schema.TextLine(
            title=_(u"Aliquot ID"),
            description=_(u"Aliquot ID"),
            required=False,
        ),
    )

    comment = RichText(
        title=_(u"iChip Comment"),
        description=_(u"Comments about iChip"),
        required=False,
    )
