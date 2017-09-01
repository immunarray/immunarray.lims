from . import BaseContainer


class Provider(BaseContainer):
    def __init__(self, *args, **kwargs):
        super(Provider, self).__init__(*args, **kwargs)

    @property
    def first_name(self):
        return getattr(self, "_first_name", "")

    @first_name.setter
    def first_name(self, value):
        self._first_name = value
        self.setTitle(value + " " + self.last_name)

    @property
    def last_name(self):
        return getattr(self, "_last_name", "")

    @last_name.setter
    def last_name(self, value):
        self._last_name = value
        self.setTitle(self.first_name + " " + value)
