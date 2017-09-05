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

    result = Attribute(
        """results go here
        """
    )

    images = schema.Dict(
        key_type=schema.TextLine(title=_(u"Image Name"),
                                 description=_(u"Image Name"),
                                 required=False, ),
        value_type=NamedBlobImage(title=_(u"Image File"),
                                  description=_(u"Image File"),
                                  required=False, ),
        required=False,
    )
