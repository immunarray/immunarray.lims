from bika.lims.interfaces.aliquot import IAliquot
from datetime import datetime
from immunarray.lims import messageFactory as _
from plone.supermodel import model
from zope import schema
from immunarray.lims.vocabularies.ichipassay import IChipAssayListVocabulary

class IClinicalAliquot(model.Schema):

    title = schema.TextLine(
        title=_(u"Aliquot Name"),
        description=_(u"Aliquot Name/ID"),
        required=False,
    )

    result = schema.Dict(
        key_type=schema.Choice(source=IChipAssayListVocabulary, required=False),
        value_type=schema.TextLine,
    )

    sample_id = schema.TextLine(
        title=_(u"Parent ID"),
        description=_(u"Parent ID"),
        required=False,
    )
