# -*- coding: utf-8 -*-
from immunarray.lims.content.abstractsample import AbstractSample
from immunarray.lims.interfaces.sample import ISample
from zope.interface import implements


class ClinicalSample(AbstractSample):
    implements(ISample)

    def __init__(self, *args, **kwargs):
        super(ClinicalSample, self).__init__(*args, **kwargs)

    @property
    def usn(self):
        return getattr(self, "_usn", "")

    @usn.setter
    def usn(self, value):
        self._usn = value
        self.setTitle(value)
