# -*- coding: utf-8 -*-
from immunarray.lims import messageFactory as _
from immunarray.lims.fields.amount import Amount
from immunarray.lims.interfaces import BaseModel
from immunarray.lims.vocabularies.material import MaterialsVocabulary
from plone.autoform.interfaces import IFormFieldProvider
from zope import schema
from zope.interface import alsoProvides


class ISolution(BaseModel):
    """Base Solution schema fields
    """
    batch_number = schema.TextLine(
        title=_(u"Batch Number"),
        description=_(u""),
        required=True,
    )

    make_date = schema.Date(
        title=_(u"Date Made"),
        description=_(u""),
        required=True,
    )

    expiration_date = schema.Date(
        title=_(u"Expiration Date"),
        description=_(u""),
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
        readonly=True,
    )

    unit = schema.TextLine(
        title=_(u"Unit"),
        description=_("Enter the unit in which the amounts are measured"),
        required=True,
    )

    materials_used = schema.Dict(
        title=_(u"Materials used"),
        key_type=schema.Choice(title=_(u"Material"),
                               source=MaterialsVocabulary,
                               required=False),
        value_type=Amount(title=u"Amount used",
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


alsoProvides(ISolution, IFormFieldProvider)
