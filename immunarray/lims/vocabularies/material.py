from plone.api.content import find
from zope.interface import implements
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary


class Materials(object):
    """Context source binder to provide a vocabulary of available lots of
    different material types.
    """

    implements(IContextSourceBinder)

    def __call__(self, context):
        brains = find(
            object_provides='immunarray.lims.interfaces.material.IMaterial',
            review_state='in_use',
            remaining_amount={'query': 1, 'range': 'min'},
            sort_on='sortable_title')
        return SimpleVocabulary.fromValues([brain.Title for brain in brains])


MaterialsVocabulary = Materials()
