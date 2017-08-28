from . import BaseContainer


class Provider(BaseContainer):
    def __init__(self, *args, **kwargs):
        super(Provider, self).__init__(*args, **kwargs)
