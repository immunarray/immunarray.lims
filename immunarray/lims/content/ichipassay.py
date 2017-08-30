from . import BaseContainer


class iChipAssay(BaseContainer):
    def __init__(self, *args, **kwargs):
        super(iChipAssay, self).__init__(*args, **kwargs)

    @property
    def name(self):
        return getattr(self, "_name", "")

    @name.setter
    def name(self, value):
        self._name = value
        temp = getattr(self, "_desired_use", "")
        self.setTitle(value + " - " + temp)
        self.id = '{}-{}'.format(value, temp)

    @property
    def desired_use(self):
        return getattr(self, "_desired_use", "")

    @desired_use.setter
    def desired_use(self, value):
        self._desired_use = value
        temp = getattr(self, "_name", "")
        self.setTitle(temp + " - " + value)
        self.id = '{}-{}'.format(temp, value)
