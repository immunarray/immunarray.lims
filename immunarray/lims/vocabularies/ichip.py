# -*- coding: utf-8 -*-
from plone import api
from plone.i18n.normalizer.interfaces import IIDNormalizer
from zope.component import queryUtility
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary

@implementer(IVocabularyFactory)
class IChipsInUS (object):
    def __call__(self, context):
        values = context.ichip.objectValues()
        ichips = [v.title for v in values
                  if 'released' in v.status.lower()
                  or 'retained-us' in v.status.lower()
                  or 'quarantined' in v.status.lower()
                  or 'retained-us' in v.status.lower()]
        normalizer = queryUtility(IIDNormalizer)
        items = [(i, normalizer.normalize(i)) for i in ichips]
IChipsInUSVocabulary = IChipsInUS()

class IChipsForCommercialTesting (object):
    def __call__(self, context):
        values = context.ichip.objectValues()
        ichips = [v.title for v in values
                  if 'released' in v.status.lower()]
        normalizer = queryUtility(IIDNormalizer)
        items = [(i, normalizer.normalize(i)) for i in ichips]
IChipsForCommercialTestingVocabulary = IChipsForCommercialTesting()

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
    """
