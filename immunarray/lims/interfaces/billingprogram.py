# -*- coding: utf-8 -*-
from zope import schema

from immunarray.lims import messageFactory as _
from immunarray.lims.interfaces import BaseModel
from immunarray.lims.vocabularies.ichipassay import IChipAssayListVocabulary
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides


class IBillingProgram(BaseModel):
    """Object that will be billing programs that can be added to the system,
    will be what is used to determin if a billing message needs to be generated,
    cost to patient, and message structure to be sent to third party.
    """
    program_name = schema.TextLine(
        title=_(u"Name of Billing Program"),
        description=_(u"Name of Billing Program"),
        required=False,
    )

    assay_name = schema.Choice(
        title=_(u"Assay to be Billed"),
        description=_(u"Assay to be Billed"),
        source=IChipAssayListVocabulary,
        required=True
    )

    cost_of_assay = schema.Float(
        title=_(u"Full Cost of Assay"),
        description=_(u"Full Cost of Assay"),
        required=True,
    )

    max_cost_to_patient = schema.Float(
        title=_(u"Max Cost to Patient"),
        description=_(u"Max Cost to Patient"),
        required=True,
    )

    discount_to_patient = schema.Float(
        title=_(u"Discout to Patient"),
        description=_(u"Discout to Patient"),
        default=0.0,
        required=True,
    )

    allow_balance_bill = schema.Bool(
        title=_(u"Allow Balance Billing"),
        description=_(u"Allow Balance Billing")
    )


alsoProvides(IBillingProgram, IFormFieldProvider)
