# -*- coding: utf-8 -*-
from plone import api
from plone.i18n.normalizer.interfaces import IIDNormalizer
from zope.component import queryUtility
from zope.interface import implements
from zope.schema.interfaces import IVocabularyFactory, IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary

class QCList (object):
    """Returns a vocab of qc samples that will be used by iChipAssay to assign high and low qc samples to be used in testing
    """
    implements(IVocabularyFactory, IContextSourceBinder)
    def __call__(self, context):
        values = api.content.find(context=api.portal.get(), portal_type='QCSample')
        qcsample_ids = [v.UID for v in values]
        items = []
        for i in qcsample_ids:
            a = api.content.get(UID=i)
            items.append(SimpleVocabulary.createTerm(a.veracis_id))
        return SimpleVocabulary(items)

QCListVocabulary = QCList()
