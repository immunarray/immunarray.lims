# -*- coding: utf-8 -*-
from immunarray.lims import normalize
from plone.api.portal import get_registry_record
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary


@implementer(IVocabularyFactory)
class PrimaryNCE(object):
    def __call__(self, context):
        values = get_registry_record('immunarray.category_primary')
        items = [(i, normalize(i)) for i in values]
        return SimpleVocabulary.fromItems(items)


PrimaryNCEVocabulary = PrimaryNCE()


@implementer(IVocabularyFactory)
class SecondaryNCE(object):
    def __call__(self, context):
        values = get_registry_record('immunarray.category_secondary')
        items = [(i, normalize(i)) for i in values]
        return SimpleVocabulary.fromItems(items)


SecondaryNCEVocabulary = SecondaryNCE()


@implementer(IVocabularyFactory)
class TertiaryNCE(object):
    def __call__(self, context):
        values = get_registry_record('immunarray.category_tertiary')
        items = [(i, normalize(i)) for i in values]
        return SimpleVocabulary.fromItems(items)


TertiaryNCEVocabulary = TertiaryNCE()
