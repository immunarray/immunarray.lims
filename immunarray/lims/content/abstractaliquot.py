from immunarray.lims.interfaces import IWorkingAliquot, IBulkAliquot
from . import BaseContainer
from zope.interface import alsoProvides


class AbstractAliquot(BaseContainer):
    def __init__(self, *args, **kwargs):
        super(AbstractAliquot, self).__init__(*args, **kwargs)

    def set_aliquot_type(self, value):
        if value == 'Bulk':
            alsoProvides(self, IBulkAliquot)
        else:
            alsoProvides(self, IWorkingAliquot)
