# -*- coding: utf-8 -*-
from plone import api
from plone.i18n.normalizer.interfaces import IIDNormalizer
from zope.component import queryUtility
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary

@implementer(IVocabularyFactory)
class Providers(object):

    def __call__(self, context):
        values = context.providers.objectValues()
        names = [" ".join([v.first_name, v.last_name]) for v in values]
        normalizer = queryUtility(IIDNormalizer)
        items = [(n, normalizer.normalize(n)) for n in names]
        return SimpleVocabulary.fromItems(items)

ProvidersVocabulary = Providers()
