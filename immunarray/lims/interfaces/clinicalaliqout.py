from bika.lims.interfaces.aliquot import IAliquot
from datetime import datetime
from plone.supermodel import model
from zope import schema
from immunarray.lims.vocabularies.ichipassay import IChipAssayListVocabulary

class IClinicalAliquot(IAliquot):
    result = schema.Dict(
        key_type=schema.Choice(source=IChipAssayListVocabulary, required=False),
        value_type=schema.TextLine,
    )
