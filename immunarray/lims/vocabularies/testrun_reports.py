# -*- coding: utf-8 -*-
import os

from immunarray.lims import normalize
from os.path import exists, join
from pkg_resources import resource_filename
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary


@implementer(IVocabularyFactory)
class TestRunReports(object):
    def __call__(self, context):
        path = resource_filename('immunarray.lims', 'reports')
        reports = [x for x in os.listdir(path) if exists(join(x, 'report.pt'))]
        items = [(t, normalize(t)) for t in sorted(reports)]
        return SimpleVocabulary.fromItems(items)


TestRunReportsVocabulary = TestRunReports()
