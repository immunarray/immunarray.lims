from immunarray.lims.content.abstractsample import AbstractSample
from immunarray.lims.interfaces.sample import ISample
from zope.interface import implements


class QCSample(AbstractSample):
    implements(ISample)

    def __init__(self, *args, **kwargs):
        super(QCSample, self).__init__(*args, **kwargs)
