# -*- coding: utf-8 -*-
from plone import api
from plone.i18n.normalizer.interfaces import IIDNormalizer
from zope.component import queryUtility
from zope.interface import implementer
from zope.interface import implements
from zope.schema.interfaces import IVocabularyFactory, IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary

@implementer(IVocabularyFactory)
class IChipAssay (object):
    pass
    def __call__(self, context):
        values = api.portal.get_registry_record('immunarray.category_primary')
        normalizer = queryUtility(IIDNormalizer)
        items = [(i, normalizer.normalize(i)) for i in values]
        return SimpleVocabulary.fromItems(items)

IChipAssayVocabulary = IChipAssay()

class IChipAssayList(object):

    implements(IVocabularyFactory, IContextSourceBinder)

    def __call__(self, context):
        values = context.ichipassay.objectValues()
        names = [" ".join([v.title, v.status]) for v in values]
        normalizer = queryUtility(IIDNormalizer)
        items = [(n, normalizer.normalize(n)) for n in names]
        return SimpleVocabulary.fromItems(items)

IChipAssayListVocabulary = IChipAssayList()
