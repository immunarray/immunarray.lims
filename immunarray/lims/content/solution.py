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

    @property
    def batch_number(self):
        return getattr(self, "_batch_number", "")

    @batch_number.setter
    def batch_number(self, value):
        self._batch_number = value
        self.setTitle("{} ({})".format(self.Type(), value))
