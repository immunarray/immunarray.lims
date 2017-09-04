# -*- coding: utf-8 -*-
from immunarray.lims.interfaces.patient import IPatient
from zope.interface import implements
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary


class Patients(object):
    """Context source binder to provide a vocabulary of existing patients
    """

    implements(IContextSourceBinder)

    def __call__(self, context):
        catalog = context.portal_catalog
        proxies = catalog({
            'object_provides': IPatient.__identifier__,
            'sort_on': 'sortable_title',
        })
        terms = [SimpleTerm(proxy.id, title=proxy.Title)
                 for proxy in proxies]
        return SimpleVocabulary(terms)
