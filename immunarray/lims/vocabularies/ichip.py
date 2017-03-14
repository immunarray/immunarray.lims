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
from zope.interface import alsoProvides
from plone.autoform.interfaces import IFormFieldProvider
from plone.directives import form


class IChipsInUS (object):
    implements(IVocabularyFactory, IContextSourceBinder)
    def __call__(self, context):
        wells = ["A","B","C","D","E","F","G","H"]
        values = api.content.find(context=api.portal.get(), portal_type='iChip')
        ichips = [v.Title for v in values]
        unique_ichips=[]
        for u in ichips:
            if u not in unique_ichips:
                unique_ichips.append(u)
        normalizer = queryUtility(IIDNormalizer)
        items = [(i, normalizer.normalize(i).upper()) for i in unique_ichips]
        return SimpleVocabulary.fromItems(items)
IChipsInUSVocabulary = IChipsInUS()


@implementer(IVocabularyFactory)
class IChipsForCommercialTesting (object):
    implements(IVocabularyFactory, IContextSourceBinder)
    def __call__(self, context):
        values = api.content.find(context=api.portal.get(), portal_type='IChip')
        ichips = [(v.id) for v in values
                  if 'released' in v.status.lower()]
        normalizer = queryUtility(IIDNormalizer)
        items = [(i, normalizer.normalize(i).upper()) for i in ichips]
        return SimpleVocabulary.fromItems(items)
IChipsForCommercialTestingVocabulary = IChipsForCommercialTesting()


@implementer(IVocabularyFactory, IContextSourceBinder)
class IChipsAll(object):

    #want to not have v.status = 'Retired (No Longer Offered)'
    def __call__(self, context):
        catalog = getToolByName(context, 'portal_catalog')
        values = catalog(portal_type='iChip')
        names = [([v.id]) for v in values]
        normalizer = queryUtility(IIDNormalizer)
        items = [(n, normalizer.normalize(n).upper()) for n in names]
        return SimpleVocabulary.fromItems(items)
IChipsAllVocabulary = IChipsAll()
alsoProvides(IChipsAll, IFormFieldProvider)


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
