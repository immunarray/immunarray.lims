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
        self.setTitle(value + " - " + self.lot_number)

    @property
    def lot_number(self):
        return getattr(self, "_lot_number", "")

    @lot_number.setter
    def lot_number(self, value):
        self._lot_number = value
        self.setTitle(self.product_name + " - " + value)

    @property
    def initial_amount(self):
        # no default value, because we do not want to guess the unit.
        return getattr(self, "_initial_amount", "")

    @initial_amount.setter
    def initial_amount(self, value):
        # if there's already an _initial_amount, do NOT update remaining_amount.
        already_set = getattr(self, '_initial_amount', False)
        self._initial_amount = value
        if not already_set:
            self.remaining_amount = value
