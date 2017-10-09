# -*- coding: utf-8 -*-
from immunarray.lims.interfaces.storage import IRandDBox
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer

from . import BaseContainer


@implementer(IRandDBox)
@adapter(Interface)
class RandDBox(BaseContainer):
    def __init__(self, *args, **kwargs):
        super(RandDBox, self).__init__(*args, **kwargs)

    # @property
    # def box_number(self):
    #     return getattr(self, "_box_number", "")
    #
    # @box_number.setter
    # def box_number(self, value):
    #     self._box_number = value
    #     self.setTitle(value + " - " + self.box_type)
    #
    # @property
    # def box_type(self):
    #     return getattr(self, "_box_type", "")
    #
    # @box_type.setter
    # def box_type(self, value):
    #     self._box_type = value
    #     self.setTitle(self.box_number + " - " + value)
