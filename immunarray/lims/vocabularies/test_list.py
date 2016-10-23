# -*- coding: utf-8 -*-
from plone import api
from plone.i18n.normalizer.interfaces import IIDNormalizer
from zope.component import queryUtility
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary

@implementer(IVocabularyFactory)
class TestList(object):
    pass
    def __call__(self, context):
        values = api.portal.get_registry_record('immunarray.category_primary')
        normalizer = queryUtility(IIDNormalizer)
        items = [(i, normalizer.normalize(i)) for i in values]
        return SimpleVocabulary.fromItems(items)

TestListVocabulary = TestList()
