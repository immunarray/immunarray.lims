from . import BaseContainer


class Material(BaseContainer):
    def __init__(self, *args, **kwargs):
        super(Material, self).__init__(*args, **kwargs)

    def set_product_name(self, value):
        import pdb;pdb.set_trace()
        title = value + " - " + self.lot_number
        self.setTitle(title)

    def set_lot_number(self, value):
        title = self.product_name + " - " + value
        self.setTitle(title)
