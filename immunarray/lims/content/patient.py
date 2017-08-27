from plone.dexterity.content import Container


class Patient(Container):
    def __init__(self, *args, **kwargs):
        super(Patient, self).__init__(*args, **kwargs)
