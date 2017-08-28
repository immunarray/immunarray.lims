from . import BaseContainer


class Material(BaseContainer):
    def __init__(self, *args, **kwargs):
        super(Material, self).__init__(*args, **kwargs)

    @property
    def product_name(self):
        return getattr(self, "_product_name", "")

    @product_name.setter
    def product_name(self, value):
        self._product_name = value
        temp = getattr(self, "_lot_number", "")
        self.setTitle(value + " - " + temp)

    @property
    def lot_number(self):
        return getattr(self, "_lot_number", "")

    @lot_number.setter
    def lot_number(self, value):
        self._lot_number = value
        temp = getattr(self, "_product_name", "")
        self.setTitle(temp + " - " + value)
