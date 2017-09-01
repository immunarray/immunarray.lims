# -*- coding: utf-8 -*-
from zope.interface import implements

from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm


class Patients(object):
    """Context source binder to provide a vocabulary of existing patients
    """

    implements(IContextSourceBinder)

    def __call__(self, context):
        catalog = context.portal_catalog
        proxies = catalog({
            'object_provides': 'immunarray.lims.interfaces.patient.IPatient',
            'sort_on': 'sortable_title',
        })
        terms = [SimpleTerm(proxy.id, title=proxy.Title)
                 for proxy in proxies]
        return SimpleVocabulary(terms)
