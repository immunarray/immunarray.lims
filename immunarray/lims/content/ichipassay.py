# -*- coding: utf-8 -*-
from . import BaseContainer


class iChipAssay(BaseContainer):
    def __init__(self, *args, **kwargs):
        super(iChipAssay, self).__init__(*args, **kwargs)

    @property
    def name(self):
        return getattr(self, "_name", "")

    @name.setter
    def name(self, value):
        self._name = value
        self.setTitle(value + " - " + self.desired_use)
        self.id = '{}-{}'.format(value, self.desired_use)

    @property
    def desired_use(self):
        return getattr(self, "_desired_use", "")

    @desired_use.setter
    def desired_use(self, value):
        self._desired_use = value
        self.setTitle(self.name + " - " + value)
        self.id = '{}-{}'.format(self.name, value)
