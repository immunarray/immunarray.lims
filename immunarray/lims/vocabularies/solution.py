# -*- coding: utf-8 -*-
from immunarray.lims.interfaces.solution import ISolution
from zope.interface import implements
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary


class Solutions(object):
    """Context source binder to provide a vocabulary of available lots of
    different solution types.
    """

    implements(IContextSourceBinder)

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def __call__(self, context):
        catalog = context.portal_catalog
        brains = catalog(
            object_provides=ISolution.__identifier__,
            sort_on='sortable_title',
        )
        return SimpleVocabulary.fromValues([brain.title for brain in brains])

class SolutionTypes(object):
    """Context source binder to provide a vocabulary of available lots of
    different solution types.
    """

    implements(IContextSourceBinder)

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def __call__(self, context):
        # portal_types walker XXX for ichipassay definitions
        return SimpleVocabulary.fromValues(
            [brain.title for brain in brains])
