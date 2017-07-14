# -*- coding: utf-8 -*-
from plone import api
from plone.i18n.normalizer.interfaces import IIDNormalizer
from zope.component import queryUtility
from zope.interface import implementer
from zope.interface import implements
from zope.schema.interfaces import IVocabularyFactory, IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary

class IChipAssayList(object):
    """Produces full list of all Non Retired iChip Assays in LIMS
    """
    implements(IVocabularyFactory, IContextSourceBinder)
    def __call__(self, context):
        values = api.content.find(context=api.portal.get(), portal_type='iChipAssay')
        ichipassay = []
        ichipassay_ids = [v.UID for v in values]
        for i in ichipassay_ids:
            value = api.content.get(UID=i)
            #only get non retired assays
            if value.status=="Commercial" or value.status=="Development":
                ichipassay.append("-".join([value.title, value.status]))
        normalizer = queryUtility(IIDNormalizer)
        items = [(o, normalizer.normalize(o).upper()) for o in ichipassay]
        return SimpleVocabulary.fromItems(items)

IChipAssayListVocabulary = IChipAssayList()
