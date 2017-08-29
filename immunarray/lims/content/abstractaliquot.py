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

    @property
    def id(self):
        return getattr(self, '_id')

    @id.setter
    def id(self, value):
        """The title is set the same as the ID, but has spaces in it.
        """
        self._id = value
        self.setTitle(' - '.join(value.split('-')))
