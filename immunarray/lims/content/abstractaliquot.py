from immunarray.lims.interfaces import IWorkingAliquot, IBulkAliquot
from plone.dexterity.content import Container
from zope.interface import alsoProvides


class AbstractAliquot(Container):
    def __init__(self, *args, **kwargs):
        super(AbstractAliquot, self).__init__(*args, **kwargs)

    def __setattr__(self, key, value):
        if key == 'aliquot_type':
            if value == 'Bulk':
                alsoProvides(self, IBulkAliquot)
            else:
                alsoProvides(self, IWorkingAliquot)
