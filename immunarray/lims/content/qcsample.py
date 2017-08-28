from immunarray.lims.content.abstractsample import AbstractSample
from immunarray.lims.interfaces.sample import ISample
from zope.interface import implements


class QCSample(AbstractSample):
    implements(ISample)

    def __init__(self, *args, **kwargs):
        super(QCSample, self).__init__(*args, **kwargs)

    # def set_source_id_one(self, value):
    #     title = self.veracis_id + " " + value
    #     self.setTitle(title)
    #
    # def set_veracis_id(self, value):
    #     title = value + " " + self.source_id_one
    #     self.setTitle(title)
    @property
    def veracis_id(self):
        return getattr(self, "_veracis_id", "")

    @veracis_id.setter
    def veracis_id(self, value):
        self._veracis_id = value
        temp = getattr(self, "_source_id_one", "")
        self.setTitle(value + " - " + temp)

    @property
    def source_id_one(self):
        return getattr(self, "_source_id_one", "")

    @source_id_one.setter
    def source_id_one(self, value):
        self._source_id_one = value
        temp = getattr(self, "_veracis_id", "")
        self.setTitle(temp + " - " + value)
