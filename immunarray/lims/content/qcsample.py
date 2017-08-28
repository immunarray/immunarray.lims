from immunarray.lims.content.abstractsample import AbstractSample
from immunarray.lims.interfaces.sample import ISample
from zope.interface import implements


class QCSample(AbstractSample):
    implements(ISample)

    def __init__(self, *args, **kwargs):
        super(QCSample, self).__init__(*args, **kwargs)

    def set_source_id_one(self, value):
        title = self.veracis_id + " " + value
        self.setTitle(title)

    def set_veracis_id(self, value):
        title = value + " " + self.source_id_one
        self.setTitle(title)
