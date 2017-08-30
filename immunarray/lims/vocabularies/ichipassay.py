# -*- coding: utf-8 -*-
from plone import api
from zope.interface import implements
from zope.schema.interfaces import IVocabularyFactory, IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary


class IChipAssayList(object):
    """Produces full list of all Non Retired iChip Assays in LIMS
    """
    implements(IVocabularyFactory, IContextSourceBinder)

    def __call__(self, context):
        brains = api.content.find(portal_type='iChipAssay',
                                  reivew_state='activated')
        ichip_assay_titles = [brain.title for brain in brains]
        return SimpleVocabulary.fromItems(ichip_assay_titles)

IChipAssayListVocabulary = IChipAssayList()
