# -*- coding: utf-8 -*-
from immunarray.lims.content.abstractsample import AbstractSample
from immunarray.lims.interfaces.sample import ISample
from zope.interface import implements


class RandDSample(AbstractSample):
    implements(ISample)

    def __init__(self, *args, **kwargs):
        super(RandDSample, self).__init__(*args, **kwargs)

    @property
    def veracis_id(self):
        return getattr(self, "_veracis_id", "")

    @veracis_id.setter
    def veracis_id(self, value):
        self._veracis_id = value
        self.setTitle(value + " - " + self.source_id_one)
        self.id = '{}-{}'.format(value, self.source_id_one)

    @property
    def source_id_one(self):
        return getattr(self, "_source_id_one", "")

    @source_id_one.setter
    def source_id_one(self, value):
        self._source_id_one = value
        self.setTitle(self.veracis_id + " - " + value)
        self.id = '{}-{}'.format(self.veracis_id, value)
