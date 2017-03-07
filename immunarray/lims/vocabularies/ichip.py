# -*- coding: utf-8 -*-
from plone import api
from plone.i18n.normalizer.interfaces import IIDNormalizer
from zope.component import queryUtility
from zope.interface import implements
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.interfaces import IContextSourceBinder
from Products.CMFCore.interfaces import IContentish
from Products.CMFCore.utils import getToolByName


class IChipsInUS (object):
    implements(IVocabularyFactory, IContextSourceBinder)
    def __call__(self, context):
        catalog = getToolByName(context, 'portal_catalog')
        values = catalog.searchResults(portal_type='crap')
        ichips = [v.title for v in values]
        normalizer = queryUtility(IIDNormalizer)
        items = [(i, normalizer.normalize(i)) for i in ichips]
        return SimpleVocabulary.fromItems(items)

IChipsInUSVocabulary = IChipsInUS()


class IChipsForCommercialTesting (object):
    implements(IVocabularyFactory, IContextSourceBinder)
    def __call__(self, context):
        values = api.content.find(context=api.portal.get(), portal_type='IChip')
        ichips = [str(v.id) for v in values
                  if 'released' in v.status.lower()]
        normalizer = queryUtility(IIDNormalizer)
        items = [(i, normalizer.normalize(i)) for i in ichips]
        return SimpleVocabulary.fromItems(items)
IChipsForCommercialTestingVocabulary = IChipsForCommercialTesting()

class IChipsAll(object):

    implements(IVocabularyFactory, IContextSourceBinder)
    #want to not have v.status = 'Retired (No Longer Offered)'
    def __call__(self, context):
        values = api.content.find(context=api.portal.get(), portal_type='IChip')
        names = [" ".join([v.title, v.status]) for v in values
             if 'retired' not in v.status.lower()]
        normalizer = queryUtility(IIDNormalizer)
        items = [(n, normalizer.normalize(n).upper()) for n in names]
        return SimpleVocabulary.fromItems(items)

IChipsAllVocabulary = IChipsAll()

"""class Providers(object):
    def __call__(self, context):
        values = context.providers.objectValues()
        names = [" ".join([str(v.site_ID), v.first_name, v.last_name]) for v in values]
        normalizer = queryUtility(IIDNormalizer)
        items = [(n, normalizer.normalize(n)) for n in names]
        return SimpleVocabulary.fromItems(items)

ProvidersVocabulary = Providers()

values=[_(u'Quarantined'),
                _(u'Released'),
                _(u'Retained-US'),
                _(u'Retained-IA'),
                _(u'Inprocess'),
                _(u'Used-QC-Passed'),
                _(u'Used-QC-Failed'),
                _(u'Residual'),
                _(u'Broken'),
                _(u'Used-Training'),
                _(u'Used-Validaiton')],
    )


                  if 'released' in v.status.lower()
                  or 'retained-us' in v.status.lower()
                  or 'quarantined' in v.status.lower()
                  or 'retained-us' in v.status.lower()
    """
