# -*- coding: utf-8 -*-
from immunarray.lims import normalize
from immunarray.lims.interfaces.provider import IProvider
from plone.api.content import find
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary
from pkg_resources import resource_listdir, resource_filename

@implementer(IVocabularyFactory)
class TestRunReports(object):
    def __call__(self, context):

        path = resource_filename('immunarray.lims', ''
            )



        brains = find(.__identifer__)
        values = [b.getObject() for b in brains]
        names = [" ".join([str(v.site_ID), v.first_name, v.last_name])
                 for v in values]
        items = [(n, normalize(n)) for n in names]
        return SimpleVocabulary.fromItems(items)


ProvidersVocabulary = Providers()
