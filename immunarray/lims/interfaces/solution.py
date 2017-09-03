# -*- coding: utf-8 -*-
from zope import schema

from immunarray.lims import messageFactory as _
from immunarray.lims.fields.amount import Amount
from immunarray.lims.interfaces import BaseModel
from immunarray.lims.vocabularies.material import Materials
from immunarray.lims.vocabularies.solution import \
    SolutionBatchesForTestRunsVocabulary
from immunarray.lims.vocabularies.users import UserVocabulary
from plone.autoform.interfaces import IFormFieldProvider
from plone.namedfile import NamedFile
from plone.namedfile.field import NamedFile
from zope.interface import alsoProvides

MaterialsVocabulary = Materials(review_state='in_use')


class ISolution(BaseModel):
    """Base Solution schema fields
    """
    solution_name = schema.TextLine(
        title=_(u"Solution Name"),
        description=_(u"Solution Name"),
        required=True,
    )

    batch_number = schema.TextLine(
        title=_(u"Batch Number"),
        description=_(u"Batch Number"),
        required=True,
    )

    make_date = schema.Date(
        title=_(u"Date Made"),
        description=_(u"Date Made"),
        required=True,
    )

    expiration_date = schema.Date(
        title=_(u"Expiration Date"),
        description=_(u"Expiration Date"),
        required=True,
    )

    initial_amount = Amount(
        title=_(u"Initial amount made"),
        description=_(u"Enter a decimal number"),
        required=True,
    )

    remaining_amount = Amount(
        title=_(u"Amount remaining"),
        description=_(u"You should not need to edit this value"),
    )

    unit = schema.TextLine(
        title=_(u"Unit"),
        description=_("Enter the unit in which the amounts are measured"),
        required=True,
    )

    made_by = schema.Choice(
        title=_(u"Made By"),
        description=_(u"The operator created the material lot"),
        source=UserVocabulary,
        required=True
    )

    materials_used = schema.Dict(
        title=_(u"Materials Used"),
        key_type=schema.Choice(title=_(u"Material"),
                               source=MaterialsVocabulary,
                               required=False),
        value_type=Amount(title=u"Amount Used",
                          required=False),
        required=False
    )

    solution_used = schema.Dict(
        title=_(u"Solution(s) Used"),
        key_type=schema.Choice(
            title=_(u"Solution"),
            source=SolutionBatchesForTestRunsVocabulary,
            required=False),
        value_type=Amount(
            title=u"Amount Used",
            required=False),
        required=False
    )

    viability = schema.Int(
        title=_(u"Solution Viability"),
        description=_(
            u"Viability of solution in hours. "
            u"Leave blank if solution does not expire."),
        required=False,
    )

    completed_solution_prep_form = NamedFile(
        title=_(u"Completed Solution Preperation Form"),
        required=False,
    )

    ####comments =

alsoProvides(ISolution, IFormFieldProvider)
