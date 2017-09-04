# -*- coding: utf-8 -*-
from zope import schema

from immunarray.lims import messageFactory as _
from immunarray.lims.interfaces import BaseModel
from immunarray.lims.vocabularies.qc import InUseQCListVocabulary
from immunarray.lims.vocabularies.solution import \
    SolutionsForiChipAssayVocabulary
from plone.app.textfield import RichText
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from plone.autoform import directives as form


class IiChipAssay(BaseModel):
    """ Interface that will allow for creation of new iChip Assays"""
    name = schema.TextLine(
        title=_(u"iChip Assay"),
        required=True,
    )

    description = schema.TextLine(
        title=_(u"Description"),
        description=_(u"Description"),
        required=False,
    )

    framecount = schema.Int(
        title=_(u"Frame Layout"),
        description=_(u"No Well = 1, Eight Well = 8"),
        required=True,
    )

    number_of_unique_ichips_lots_needed = schema.Int(
        title=_(u"Number of Unique iChip Lots Needed"),
        description=_(u"Number of Unique iChip Lots Needed"),
        required=True,
        default=2,
    )

    number_of_same_lot_replication_needed = schema.Int(
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

    qc_high_choice = schema.Choice(
        title=_(u"Select High/Positive QC Veracis ID"),
        description=_(u"Select High/Positive QC Veracis ID"),
        source=InUseQCListVocabulary,
        required=False,
    )

    number_of_low_value_controls = schema.Int(
        title=_(u"Number of Low/Negative Controls"),
        description=_(u"Number of Low/Negative Controls"),
        required=True,
        default=1,
    )

    qc_low_choice = schema.Choice(
        title=_(u"Select Low/Negative QC Veracis ID"),
        description=_(u"Select Low/Negative QC Veracis ID"),
        source=InUseQCListVocabulary,
        required=False,
    )

    sample_qc_dilution_factor = schema.Int(
        title=_(u"Material Dilution Factor"),
        description=_(u"Material Dilution Factor"),
        required=True,
        default=75,
    )

    # THere's a vocab for this in vocabs/solutions.  XXX showing Types only.

    # solutions = schema.List(
    #     value_type=schema.Choice(
    #         title=
    #         source=, required=False)

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

    minimum_working_aliquot_volume = schema.Int(
        title=_(u"Minimum Working Aliquot Volume (uL)"),
        description=_(u"Minimum Working Aliquot Volume (uL)"),
        required=True,
        default=8,
    )

    desired_use = schema.Choice(
        title=_(u"iChip Assay Status"),
        description=_(u"iChip Layout"),
        values=[_(u"Development"),
                _(u"Commercial"), ],
        required=True,
    )
    form.widget(needed_solutions=CheckBoxFieldWidget)
    needed_solutions = schema.List(
        title=_(u"Solutions Needed for Assay"),
        description=_(u"Solutions Needed for Assay"),
        required=False,
        value_type=schema.Choice(source=SolutionsForiChipAssayVocabulary),
    )

    comments = RichText(
        title=_(u"Comments"),
        description=_(u"Comments"),
        required=False,
    )
