class PrimaryNCE(object):
    """Context source binder to provide a vocabulary of existing primaryNCE topics
    """

    implements(IContextSourceBinder)

    def __call__(self, context):
        catalog = context.portal_catalog
        proxies = catalog({
            'object_provides': 'immunarray.lims.interfaces.nce.INCE',
            'sort_on': 'sortable_title',
        })
        terms = [SimpleTerm(proxy.id, title=proxy.Title)
                 for proxy in proxies]
        return SimpleVocabulary(terms)
