from immunarray.lims.interfaces import IWorkingAliquot, IBulkAliquot
from zope.interface import alsoProvides

from . import BaseContainer


class AbstractAliquot(BaseContainer):
    def __init__(self, *args, **kwargs):
        super(AbstractAliquot, self).__init__(*args, **kwargs)

    @property
    def aliquot_type(self):
        return getattr(self, "_aliquot_type", "")

    @aliquot_type.setter
    def aliquot_type(self, value):
        self._aliquot_type = value
        if value == 'Bulk':
            alsoProvides(self, IBulkAliquot)
        else:
            alsoProvides(self, IWorkingAliquot)
