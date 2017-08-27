from immunarray.lims.interfaces import ISample
from plone.dexterity.content import Container
from zope.interface import implements


class ClinicalSample(Container):
    implements(ISample)

    def __init__(self, *args, **kwargs):
        super(ClinicalSample, self).__init__(*args, **kwargs)
