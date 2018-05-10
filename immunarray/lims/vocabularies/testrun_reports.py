# -*- coding: utf-8 -*-
import os
from os.path import exists, join

from pkg_resources import resource_filename
from zope.interface import implements
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary


class TestRunReports(object):
    """Context source binder to provide vocabulary of availabe soluiton types
    that can be used iChip Assays
    """
    implements(IContextSourceBinder)

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def __call__(self, context):
        path = resource_filename('immunarray.lims', 'reports')
        items = [x for x in os.listdir(path)
                 if exists(join(path, x, 'report.pt'))]
        return SimpleVocabulary.fromValues(items)


TestRunReportsVocabulary = TestRunReports()
