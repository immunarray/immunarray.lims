from . import BaseContainer


class iChipLot(BaseContainer):
    def __init__(self, *args, **kwargs):
        super(iChipLot, self).__init__(*args, **kwargs)

    @property
    def lot_id(self):
        return getattr(self, "_lot_id", "")

    @lot_id.setter
    def lot_id(self, value):
        self._lot_id = value
        self.setTitle(value)
