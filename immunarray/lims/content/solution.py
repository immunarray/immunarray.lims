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
        self.setTitle(value + " - " + self.lot_number)

    @property
    def lot_number(self):
        return getattr(self, "_lot_number", "")

    @lot_number.setter
    def lot_number(self, value):
        self._lot_number = value
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
