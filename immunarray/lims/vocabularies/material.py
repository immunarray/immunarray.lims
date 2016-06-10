from zope.interface import implements

from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm


class Materials(object):
    """Context source binder to provide a vocabulary of available lots of
    different material types.
    """

    implements(IContextSourceBinder)

    def __init__(self, material_type):
        self.material_type = material_type

    def __call__(self, context):
        catalog = context.portal_catalog
        proxies = catalog({
            'object_provides': 'immunarray.lims.interfaces.material.IMaterial',
            'sort_on': 'sortable_title',
        })
        terms = [SimpleTerm(proxy.id, title=proxy.Title)
                 for proxy in proxies]
        return SimpleVocabulary(terms)

