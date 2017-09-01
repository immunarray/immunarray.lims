# -*- coding: utf-8 -*-
from immunarray.lims.interfaces.solution import ISolution
from zope.component import adapter
from zope.interface import Interface, implementer

from . import BaseContainer


@implementer(ISolution)
@adapter(Interface)
class Solution(BaseContainer):
    def __init__(self, *args, **kwargs):
        super(Solution, self).__init__(*args, **kwargs)

    @property
    def solution_name(self):
        return getattr(self, "_solution_name", "")

    @solution_name.setter
    def solution_name(self, value):
        self._solution_name = value
        self.setTitle(value + " - " + self.batch_number)

    @property
    def batch_number(self):
        return getattr(self, "_batch_number", "")

    @batch_number.setter
    def batch_number(self, value):
        self._batch_number = value
        self.setTitle(self.solution_name + " - " + value)

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
