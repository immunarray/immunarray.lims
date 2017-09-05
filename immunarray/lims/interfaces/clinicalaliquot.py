# -*- coding: utf-8 -*-
from datetime import date

from immunarray.lims import messageFactory as _
from immunarray.lims.interfaces.aliquot import IAliquot
from immunarray.lims.vocabularies.ichipassay import IChipAssayListVocabulary
from plone.namedfile.field import NamedBlobImage
from zope import schema

from zope.interface import Attribute


class IClinicalAliquot(IAliquot):
    title = schema.TextLine(
        title=_(u"Aliquot Name"),
        description=_(u"Aliquot Name/ID"),
        required=False,
    )

    sample_id = schema.TextLine(
        title=_(u"Parent ID"),
        description=_(u"Parent ID"),
        required=False,
    )

    aliquot_type = schema.Choice(
        title=_(u"Aliquot Type"),
        description=_(u"Aliquot Type"),
        required=True,
        values=[_(u'Bulk'),
                _(u'Working')],
    )

    pour_date = schema.Date(
        title=_(u"Aliquot Pour Date"),
        description=_(u"Aliquot Pour Date"),
        required=False,
        default=date.today(),
    )

    consume_date = schema.Date(
        title=_(u"Aliquot Consume Date"),
        description=_(u"Aliquot Consume Date"),
        required=False,
    )

    numeric_result = schema.Float(
        title=_(u"Numeric Result"),
        description=_(u"SLE_key_Score"),
        required=False,
    )

    text_result = schema.TextLine(
        title=_(u"Text Result"),
        description=_(u"SLE_key_Classification"),
        required=False,
    )
