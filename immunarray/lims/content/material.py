# -*- coding: utf-8 -*-
from immunarray.lims.interfaces.material import IMaterial
from zope.component import adapter
from zope.interface import Interface, implementer

from . import BaseContainer


@implementer(IMaterial)
@adapter(Interface)
class Material(BaseContainer):
    def __init__(self, *args, **kwargs):
        super(Material, self).__init__(*args, **kwargs)

    @property
    def product_name(self):
        return getattr(self, "_product_name", "")

    @product_name.setter
    def product_name(self, value):
        self._product_name = value
        self.setTitle(value + " - " +
                      self.lot_number + " - " +
                      self.bottle_number)

    @property
    def lot_number(self):
        return getattr(self, "_lot_number", "")

    @lot_number.setter
    def lot_number(self, value):
        self._lot_number = value
        self.setTitle(self.product_name + " - " +
                      value + " - " +
                      self.bottle_number)

    @property
    def bottle_number(self):
        return getattr(self, "_bottle_number", "")

    @bottle_number.setter
    def bottle_number(self, value):
        self._bottle_number = value
        self.setTitle(self.product_name + " - " +
                      self.lot_number + " - " +
                      str(value))
