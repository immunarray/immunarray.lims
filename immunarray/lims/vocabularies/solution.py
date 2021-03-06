# -*- coding: utf-8 -*-
from datetime import datetime

from plone.api.portal import get_tool
from zope.interface import implements
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary


class Solutions(object):
    """Context source binder to provide a vocabulary of available lots of
    different solution types.
    """

    implements(IContextSourceBinder)

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def __call__(self, context):
        catalog = context.portal_catalog
        from immunarray.lims.interfaces.solution import ISolution
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


class SolutionsForiChipAssay(object):
    """Context source binder to provide vocabulary of availabe soluiton types
    that can be used iChip Assays
    """
    implements(IContextSourceBinder)

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def __call__(self, context):
        # This is a local import
        from immunarray.lims.interfaces.solution import ISolution
        tt = get_tool('portal_types')
        all_portal_types = tt.objectValues()
        temp = []
        for pt in all_portal_types:
            if hasattr(pt, 'behaviors'):
                if ISolution.__identifier__ in pt.behaviors:
                    temp.append(pt.Title())
        return SimpleVocabulary.fromValues(temp)


SolutionsForiChipAssayVocabulary = SolutionsForiChipAssay()


class SolutionBatchesForTestRuns(object):
    """Context source binder to provide vocabulary of availabe soluiton batches
    that can be used in test runs
    """
    implements(IContextSourceBinder)

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def __call__(self, context):
        # This is a local import
        from immunarray.lims.interfaces.solution import ISolution
        catalog = get_tool('portal_catalog')
        brains = catalog(
            object_provides=ISolution.__identifier__,
            expiration_date={'query': datetime.today().date(), 'range': 'min'},
            sort_on='sortable_title',
            **self.kwargs
        )

        return SimpleVocabulary.fromValues(
            [brain.Title for brain in brains])


SolutionBatchesForTestRunsVocabulary = SolutionBatchesForTestRuns()
