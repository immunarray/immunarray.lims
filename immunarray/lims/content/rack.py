# -*- coding: utf-8 -*-
from zope.interface import Interface
from immunarray.lims.interfaces.storage import IRack
from zope.component import adapter
from zope.interface import implementer

from . import BaseContainer

@implementer(IRack)
@adapter(Interface)
class Rack(BaseContainer):
    def __init__(self, *args, **kwargs):
        super(Rack, self).__init__(*args, **kwargs)

    @property
    def rack_name(self):
        return getattr(self, "_rack_name", "")

    @rack_name.setter
    def rack_name(self, value):
        self._rack_name = value
        self.setTitle(value)
