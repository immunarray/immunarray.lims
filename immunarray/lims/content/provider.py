from . import BaseContainer


class Provider(BaseContainer):
    def __init__(self, *args, **kwargs):
        super(Provider, self).__init__(*args, **kwargs)

    def set_last_name(self, value):
        fullname = self.first_name + " " + value
        self.setTitle(fullname)

    def set_first_name(self, value):
        fullname = value + " " + self.last_name
        self.setTitle(fullname)

