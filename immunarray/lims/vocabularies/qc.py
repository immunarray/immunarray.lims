# -*- coding: utf-8 -*-
from immunarray.lims.interfaces.qcsample import IQCSample
from plone.api.content import find, get
from zope.interface import implements
from zope.schema.interfaces import IContextSourceBinder, IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary


class QCList(object):
    """Returns a vocab of qc samples that will be used by iChipAssay to 
    assign high and low qc samples to be used in testing
    """
    implements(IVocabularyFactory, IContextSourceBinder)

    def __call__(self, context):
        values = find(object_provides=IQCSample.__identifier__)
        qcsample_ids = [v.UID for v in values]
        items = []
        for uid in qcsample_ids:
            a = get(UID=uid)
            items.append(SimpleVocabulary.createTerm(a.veracis_id))
        return SimpleVocabulary(items)


QCListVocabulary = QCList()


class InUseQCList(object):
    """Returns a vocab of qc samples that will be used by iChipAssay to 
    assign high and low qc samples to be used in testing
    """
    implements(IVocabularyFactory, IContextSourceBinder)

    def __call__(self, context):
        brains = find(object_provides=IQCSample.__identifier__,
                      review_state='in_use')
        items = []
        for b in brains:
            items.append(SimpleVocabulary.createTerm(b.veracis_id))
        return SimpleVocabulary(items)


InUseQCListVocabulary = InUseQCList()
