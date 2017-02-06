# -*- coding: utf-8 -*-
from datetime import date
from plone.app.textfield import RichText
from zope import schema
from plone.supermodel import model
from immunarray.lims import messageFactory as _
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.utils import createContentInContainer
from plone.autoform import directives
from zope.interface import alsoProvides

class IiChipAssay(model.Schema):
    """ Interface that will allow for creation of new iChip Assays"""
    title = schema.TextLine(
        title=_(u"iChip Assay"),
        required=True,
    )

    description = schema.TextLine(
        title=_(u"Description"),
        description=_(u"Description"),
        required=False,
    )

    ichiptype = schema.TextLine(
        title=_(u"iChip Type"),
        description=_(u"iChip Type"),
        required=True,
    )

    number_of_unique_ichips_lots_needed = schema.Int(
        title=_(u"Number of Unique iChip Lots Needed"),
        description=_(u"Number of Unique iChip Lots Needed"),
        required=True,
        default=2,
    )

    number_of_same_lot_replication_needed_for_samples = schema.Int(
        title=_(u"Same Lot Replication Needed For Samples"),
        description=_(u"Same Lot Replication Needed For Samples"),
        required=True,
        default=2,
    )

    number_of_high_value_controls = schema.Int(
        title=_(u"Number of High/Positive Controls"),
        description=_(u"Number of High/Positive Controls"),
        required=True,
        default=2,
    )

    number_of_low_value_controls = schema.Int(
        title=_(u"Number of Low/Negative Controls"),
        description=_(u"Number of Low/Negative Controls"),
        required=True,
        default=1,
    )

    sample_qc_dilution_factor = schema.Int(
        title=_(u"Material Dilution Factor"),
        description=_(u"Material Dilution Factor"),
        required=True,
        default=75,
    )

    sample_qc_dilution_material = schema.TextLine(
        title=_(u"Sample QC Diluation Material"),
        description=_(u"Sample QC Diluiton Material"),
        required=True,
    )

    max_number_of_plates_per_test_run = schema.Int(
        title=_(u"Max Number of Plates per Test Run"),
        description=_(u"Max Number of Plates per Test Run"),
        required=True,
        default=8,
    )

    number_of_working_aliquots_needed = schema.Int(
        title=_(u"Number of Working Aliquots Needed"),
        description=_(u"Number of Working Aliquots Needed"),
        required=True,
        default=1,
    )

    desired_working_aliquot_volume = schema.Int(
        title=_(u"Desired Working Aliquot Volume (uL)"),
        description=_(u"Desired Working Aliquot Volume (uL)"),
        required=True,
        default=12,
    )

    status = schema.Choice(
        title=_(u"iChip Assay Status"),
        description=_(u"iChip Layout"),
        values=[_(u"Development"),
                _(u"Commercial"),
                _(u"Retired (No Longer Offered)")],
        required=True,
    )

    comments = RichText(
        title=_(u"Comments"),
        description=_(u"Comments"),
        required=False,
    )

