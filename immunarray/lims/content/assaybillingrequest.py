# -*- coding: utf-8 -*-
from . import BaseContainer


class AssayBillingRequest(BaseContainer):
    def __init__(self, *args, **kwargs):
        super(AssayBillingRequest, self).__init__(*args, **kwargs)

    @property
    def assay_name(self):
        return getattr(self, "_assay_name", "")

    @assay_name.setter
    def assay_name(self, value):
        self._assay_name = value
        self.setTitle(value + " - " + self.sample_id)

    @property
    def sample_id(self):
        return getattr(self, "_sample_id", "")

    @sample_id.setter
    def sample_id(self, value):
        self._sample_id = value
        self.setTitle(self.assay_name + " - " + value)
