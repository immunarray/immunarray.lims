# -*- coding: utf-8 -*-
from plone.api.content import find
from zope.interface import implements
from zope.schema.interfaces import IContextSourceBinder, IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary


class IChipAssayList(object):
    """Produces full list of all Non Retired iChip Assays in LIMS
    """
    implements(IVocabularyFactory, IContextSourceBinder)

    def __call__(self, context):
        brains = find(portal_type='iChipAssay', review_state='activated')
        ichip_assay_titles = [brain.Title for brain in brains]
        return SimpleVocabulary.fromValues(ichip_assay_titles)


IChipAssayListVocabulary = IChipAssayList()
