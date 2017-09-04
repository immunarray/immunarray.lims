# -*- coding: utf-8 -*-
from immunarray.lims.interfaces.billingprogram import IBillingProgram
from plone.api.content import find
from zope.interface import implements
from zope.schema.interfaces import IContextSourceBinder, IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary


class BillingPrograms(object):
    """Produces full list of all Non Retired iChip Assays in LIMS
    """
    implements(IVocabularyFactory, IContextSourceBinder)

    def __call__(self, context):
        brains = find(object_provides=IBillingProgram.__identifier__,
                      reivew_state='activated')
        titles = [''] + [brain.Title for brain in brains]
        return SimpleVocabulary.fromValues(titles)


BillingProgramsVocabulary = BillingPrograms()
