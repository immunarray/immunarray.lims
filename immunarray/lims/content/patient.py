from . import BaseContainer


class Patient(BaseContainer):
    def __init__(self, *args, **kwargs):
        super(Patient, self).__init__(*args, **kwargs)

    def set_last_name(self, value):
        fullname = self.first_name + " " + value
        self.setTitle(fullname)

    def set_first_name(self, value):
        fullname = value + " " + self.last_name
        self.setTitle(fullname)
