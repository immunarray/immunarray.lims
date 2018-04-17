# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
from immunarray.lims import normalize
from plone.api.content import find, get_state
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides
from zope.interface import implementer
from zope.interface import implements
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary


@implementer(IVocabularyFactory, IContextSourceBinder)
class IChipsAllBroken(object):
    """ Produces all iChips that have been decared as broken
    """

    def __call__(self, context):
        catalog = getToolByName(context, 'portal_catalog')
        values = catalog(portal_type='iChip')
        names = [([v.id]) for v in values]
        items = [(n, normalize(n)) for n in names]
        return SimpleVocabulary.fromItems(items)


IChipsAllBrokenVocabulary = IChipsAllBroken()
alsoProvides(IChipsAllBroken, IFormFieldProvider)


class IEightFrameChipsInUS(object):
    """Produces full list of all iChips
    """
    # get all iChipLots where iChipLot.frames = 8 Frame iChips
    implements(IVocabularyFactory, IContextSourceBinder)

    def __call__(self, context):
        wells = []
        values = find(portal_type='iChip')
        ichips = [v.Title for v in values]
        unique_ichip_wells = []
        for o in ichips:
            for w in wells:
                well_location = o + w
                unique_ichip_wells.append(well_location)

        items = [(i, normalize(i)) for i in ichips]
        return SimpleVocabulary.fromItems(items)


IEightFrameChipsInUSVocabulary = IEightFrameChipsInUS()


# Vocabs for Commercial Testable iChip well IDs in the US

class IEightFrameChipWellsAll(object):
    """Produces full list of all iChip well options for eight frame iChip
    """
    implements(IVocabularyFactory, IContextSourceBinder)

    def __call__(self, context):
        wells = ["-A", "-B", "-C", "-D", "-E", "-F", "-H"]
        values = find(portal_type='iChip')
        ichips = [v.Title for v in values]
        unique_ichip_wells = []
        for o in ichips:
            for w in wells:
                well_location = o + w
                unique_ichip_wells.append(well_location)

        items = [(i, normalize(i)) for i in unique_ichip_wells]
        return SimpleVocabulary.fromItems(items)


IEightFrameChipWellsAllVocabulary = IEightFrameChipWellsAll()
