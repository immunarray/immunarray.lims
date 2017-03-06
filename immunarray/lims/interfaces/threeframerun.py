from datetime import date
from immunarray.lims.interfaces.veracisrunbase import IVeracisRunBase
from immunarray.lims import messageFactory as _
from plone.app.textfield import RichText
from plone.supermodel import model
from zope import schema
from immunarray.lims.vocabularies.ichip import IChipsInUSVocabulary
from immunarray.lims.vocabularies.ichip import IChipsForCommercialTestingVocabulary
from immunarray.lims.vocabularies import ichip
from immunarray.lims.vocabularies.ichipassay import IChipAssayListVocabulary
from immunarray.lims.vocabularies import ichipassay
from immunarray.lims.vocabularies.provider import ProvidersVocabulary


class IThreeFrameRun(IVeracisRunBase):
    aliquot_to_well = schema.Dict(
        key_type=schema.TextLine(title=u"Aliquot ID"),
        value_type=schema.Choice(vocabulary='immunarray.lims.vocabularies.ichip.IChipsInUSVocabulary')
    )
