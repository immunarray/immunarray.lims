from . import BaseContainer


class Patient(BaseContainer):
    def __init__(self, *args, **kwargs):
        super(Patient, self).__init__(*args, **kwargs)
