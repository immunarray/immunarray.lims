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
import pdb

#broken code for dict


@implementer(IVocabularyFactory, IContextSourceBinder)
class IChipsAllBroken(object):
#want to not have v.status = 'Retired (No Longer Offered)'
    def __call__(self, context):
        pdb.set_trace()
        catalog = getToolByName(context, 'portal_catalog')
        values = catalog(portal_type='iChip')
        names = [([v.id]) for v in values]
        normalizer = queryUtility(IIDNormalizer)
        items = [(n, normalizer.normalize(n).upper()) for n in names]
        return SimpleVocabulary.fromItems(items)
IChipsAllBrokenVocabulary = IChipsAllBroken()
alsoProvides(IChipsAllBroken, IFormFieldProvider)


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
        items = [(i, normalizer.normalize(i).upper()) for i in ichips]
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
        items = [(i, normalizer.normalize(i).upper()) for i in ichips]
        return SimpleVocabulary.fromItems(items)
IThreeFrameChipsInUSVocabulary = IThreeFrameChipsInUS()

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
        items = [(i, normalizer.normalize(i).upper()) for i in ichips]
        return SimpleVocabulary.fromItems(items)
IEightFrameChipsInUSVocabulary = IEightFrameChipsInUS()

#Vocabs for Commercial Testable iChip well IDs in the US
class ICommercialNoFrameChips (object):
    """Produces full list of all iChip well options for no frame iChip
    does not require addition of
    """
    implements(IVocabularyFactory, IContextSourceBinder)
    def __call__(self, context):
        wells = []
        values = api.content.find(context=api.portal.get(), portal_type='iChip')
        ichips = [v.Title for v in values
                  if "released" in v.status.lower()]
        unique_ichip_wells=[]
        for o in ichips:
            for w in wells:
                well_location = o + w
                unique_ichip_wells.append(well_location)

        normalizer = queryUtility(IIDNormalizer)
        items = [(i, normalizer.normalize(i).upper()) for i in ichips]
        return SimpleVocabulary.fromItems(items)
ICommercialNoFrameChipsVocabulary = ICommercialNoFrameChips()

class ICommercialThreeFrameChipWells (object):
    """Produces full list of all iChip well options for three frame iChip
    """
    implements(IContextSourceBinder)

    #def __init__(self, ichip, frames):
    #   self.i = ichip
    #   self.f = frames

    def __call__(self, context):
        no_well = []
        three_well = ["-A","-B","-C"]
        eight_well = ["-A","-B","-C","-D","-E","-F","-G","-H"]
        values = api.content.find(context=api.portal.get(), portal_type='iChip')
        # filter __parent__ to get only 3 frame iChips
        import pdb;pdb.set_trace()
        ichips = []

        for v in values:
            a = v.getObject()
            if "released" in a.ichip_status.lower():
                ichips.append("-".join([a.title, str(a.ichip_status)]))
        unique_ichip_wells=[]
        for o in ichips:
            for w in three_well:
                well_location = o + w
                unique_ichip_wells.append(well_location)

        normalizer = queryUtility(IIDNormalizer)
        items = [(i, normalizer.normalize(i)) for i in unique_ichip_wells]
        return SimpleVocabulary.fromItems(items)
ICommercailThreeFrameChipWellsVocabulary = ICommercialThreeFrameChipWells()

class ICommercialEightFrameChipWells (object):
    """Produces full list of all iChip well options for eight frame iChip
    """
    implements(IVocabularyFactory, IContextSourceBinder)
    def __call__(self, context):
        wells = ["-A","-B","-C","-D","-E","-F","-H"]
        values = api.content.find(context=api.portal.get(), portal_type='iChip')
        ichips = [v.Title for v in values
                  if "released" in v.status.lower()]
        unique_ichip_wells=[]
        for o in ichips:
            for w in wells:
                well_location = o + w
                unique_ichip_wells.append(well_location)

        normalizer = queryUtility(IIDNormalizer)
        items = [(i, normalizer.normalize(i).upper()) for i in unique_ichip_wells]
        return SimpleVocabulary.fromItems(items)
ICommercailEightFrameChipWellsVocabulary = ICommercialEightFrameChipWells()

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
