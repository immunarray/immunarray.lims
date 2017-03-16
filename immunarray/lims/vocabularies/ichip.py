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

#updated jp 3-16-17
#Vocabs for iChips
class INoFrameChipsInUS (object):
    """Produces full list of all iChip well options for no frame iChip
    does not require addition of
    """
    implements(IVocabularyFactory, IContextSourceBinder)
    def __call__(self, context):
        wells = []
        values = api.content.find(context=api.portal.get(), portal_type='iChip')
        ichips = [v.Title for v in values]
        unique_ichip_wells=[]
        for o in ichips:
            for w in wells:
                well_location = o + w
                unique_ichip_wells.append(well_location)

        normalizer = queryUtility(IIDNormalizer)
        items = [(i, normalizer.normalize(i).upper()) for i in unique_ichip_wells]
        return SimpleVocabulary.fromItems(items)
INoFrameChipsInUSVocabulary = INoFrameChipsInUS()

class IThreeFrameChipsInUS (object):
    """Produces full list of all iChips
    """
    implements(IVocabularyFactory, IContextSourceBinder)
    def __call__(self, context):
        wells = []
        values = api.content.find(context=api.portal.get(), portal_type='iChip')
        ichips = [v.Title for v in values]
        unique_ichip_wells=[]
        for o in ichips:
            for w in wells:
                well_location = o + w
                unique_ichip_wells.append(well_location)

        normalizer = queryUtility(IIDNormalizer)
        items = [(i, normalizer.normalize(i).upper()) for i in unique_ichip_wells]
        return SimpleVocabulary.fromItems(items)
IThreeFrameChipsVocabulary = IThreeFrameChipsInUS()

class IEightFrameChipsInUS (object):
    """Produces full list of all iChips
    """
    implements(IVocabularyFactory, IContextSourceBinder)
    def __call__(self, context):
        wells = []
        values = api.content.find(context=api.portal.get(), portal_type='iChip')
        ichips = [v.Title for v in values]
        unique_ichip_wells=[]
        for o in ichips:
            for w in wells:
                well_location = o + w
                unique_ichip_wells.append(well_location)

        normalizer = queryUtility(IIDNormalizer)
        items = [(i, normalizer.normalize(i).upper()) for i in unique_ichip_wells]
        return SimpleVocabulary.fromItems(items)
IEightFrameChipsInUSVocabulary = IEightFrameChipsInUS()

#Vocabs for Commercial Testable iChip well IDs in the US
class IThreeFrameChipWellsInUS (object):
    """Produces full list of all iChip well options for three frame iChip
    """
    implements(IVocabularyFactory, IContextSourceBinder)
    def __call__(self, context):
        wells = ["-A","-B","-C"]
        values = api.content.find(context=api.portal.get(), portal_type='iChip')
        ichips = [v.Title for v in values]
        unique_ichip_wells=[]
        for o in ichips:
            for w in wells:
                well_location = o + w
                unique_ichip_wells.append(well_location)

        normalizer = queryUtility(IIDNormalizer)
        items = [(i, normalizer.normalize(i).upper()) for i in unique_ichip_wells]
        return SimpleVocabulary.fromItems(items)
IThreeFrameChipWellsInUSVocabulary = IThreeFrameChipWellsInUS()

class IEightFrameChipWellsInUS (object):
    """Produces full list of all iChip well options for eight frame iChip
    does not require addition of
    """
    implements(IVocabularyFactory, IContextSourceBinder)
    def __call__(self, context):
        wells = ["-A","-B","-C","-D","-E","-F","-H"]
        values = api.content.find(context=api.portal.get(), portal_type='iChip')
        ichips = [v.Title for v in values]
        unique_ichip_wells=[]
        for o in ichips:
            for w in wells:
                well_location = o + w
                unique_ichip_wells.append(well_location)

        normalizer = queryUtility(IIDNormalizer)
        items = [(i, normalizer.normalize(i).upper()) for i in unique_ichip_wells]
        return SimpleVocabulary.fromItems(items)
IEightFrameChipWellsInUSVocabulary = IEightFrameChipWellsInUS()


#Vocabs for ALL iChip well ID in the US (R&D use)
class IThreeFrameChipWellsAll (object):
    """Produces full list of all iChip well options for three frame iChip
    """
    implements(IVocabularyFactory, IContextSourceBinder)
    def __call__(self, context):
        wells = ["-A","-B","-C"]
        values = api.content.find(context=api.portal.get(), portal_type='iChip')
        ichips = [v.Title for v in values]
        unique_ichip_wells=[]
        for o in ichips:
            for w in wells:
                well_location = o + w
                unique_ichip_wells.append(well_location)

        normalizer = queryUtility(IIDNormalizer)
        items = [(i, normalizer.normalize(i).upper()) for i in unique_ichip_wells]
        return SimpleVocabulary.fromItems(items)
IThreeFrameChipWellsAllVocabulary = IThreeFrameChipWellsAll()

class IEightFrameChipWellsAll (object):
    """Produces full list of all iChip well options for eight frame iChip
    does not require addition of
    """
    implements(IVocabularyFactory, IContextSourceBinder)
    def __call__(self, context):
        wells = ["-A","-B","-C","-D","-E","-F","-H"]
        values = api.content.find(context=api.portal.get(), portal_type='iChip')
        ichips = [v.Title for v in values]
        unique_ichip_wells=[]
        for o in ichips:
            for w in wells:
                well_location = o + w
                unique_ichip_wells.append(well_location)

        normalizer = queryUtility(IIDNormalizer)
        items = [(i, normalizer.normalize(i).upper()) for i in unique_ichip_wells]
        return SimpleVocabulary.fromItems(items)
IEightFrameChipWellsAllVocabulary = IEightFrameChipWellsAll()



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
