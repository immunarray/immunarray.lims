# -*- coding: utf-8 -*-
from . import BaseContainer


class iChip(BaseContainer):
    def __init__(self, *args, **kwargs):
        super(iChip, self).__init__(*args, **kwargs)

    @property
    def ichip_id(self):
        return getattr(self, "_ichip_id", "")

    @ichip_id.setter
    def ichip_id(self, value):
        self._ichip_id = value
        self.setTitle(value)
