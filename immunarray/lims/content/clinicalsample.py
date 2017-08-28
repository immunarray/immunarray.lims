from immunarray.lims.content.abstractsample import AbstractSample
from immunarray.lims.interfaces import ISample
from zope.interface import implements


class ClinicalSample(AbstractSample):
    implements(ISample)

    def __init__(self, *args, **kwargs):
        super(ClinicalSample, self).__init__(*args, **kwargs)
