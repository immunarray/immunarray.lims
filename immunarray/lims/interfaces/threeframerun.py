# -*- coding: utf-8 -*-
from immunarray.lims import messageFactory as _
from immunarray.lims.interfaces.veracisrunbase import IVeracisRunBase
from immunarray.lims.vocabularies.ichip import *
from zope import schema
from zope.interface import alsoProvides


class IThreeFrameRun(IVeracisRunBase):
    # aliquot_to_well = schema.Dict(
    #    key_type=schema.TextLine(title=u"Aliquot ID", required=False),
    #    value_type=schema.Choice(
    # source=ICommercailThreeFrameChipWellsVocabulary, required=False)

    # )

    # make solutions dict, just easier to grow
    ten_x_pbs = schema.TextLine(
        title=_(u"10X PBS Lot Used"),
        description=_(u"10X PBS Lot Used"),
        required=False,
    )

    one_x_pbs = schema.TextLine(
        title=_(u"1X PBS Lot Used"),
        description=_(u"1X PBS Lot Used"),
        required=False,
    )

    one_x_pbs_22_tween20 = schema.TextLine(
        title=_(u"1X PBS - 22% Tween 20 Lot Used"),
        description=_(u"1X PBS - 22% Tween 20 Lot Used"),
        required=False,
    )


alsoProvides(IThreeFrameRun, IFormFieldProvider)
