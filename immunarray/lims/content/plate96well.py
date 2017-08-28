from . import BaseContainer


class Plate96Well(BaseContainer):
    def __init__(self, *args, **kwargs):
        super(Plate96Well, self).__init__(*args, **kwargs)
