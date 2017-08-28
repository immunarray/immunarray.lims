from immunarray.lims.content.abstractsample import AbstractSample
from immunarray.lims.interfaces.sample import ISample
from zope.interface import implements


class RandDSample(AbstractSample):
    implements(ISample)

    def __init__(self, *args, **kwargs):
        super(RandDSample, self).__init__(*args, **kwargs)
