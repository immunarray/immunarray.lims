from . import BaseContainer


class Patient(BaseContainer):
    def __init__(self, *args, **kwargs):
        super(Patient, self).__init__(*args, **kwargs)

    @property
    def first_name(self):
        return getattr(self, "_first_name", "")

    @first_name.setter
    def first_name(self, value):
        self._first_name = value
        lastname = getattr(self, "_last_name", "")
        self.setTitle(value + " " + lastname)

    @property
    def last_name(self):
        return getattr(self, "_last_name", "")

    @last_name.setter
    def last_name(self, value):
        self._last_name = value
        firstname = getattr(self, "_first_name", "")
        self.setTitle(firstname + " " + value)
