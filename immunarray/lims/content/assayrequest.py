from . import BaseContainer


class AssayRequest(BaseContainer):
    def __init__(self, *args, **kwargs):
        super(AssayRequest, self).__init__(*args, **kwargs)

    @property
    def assay_name(self):
        return getattr(self, "_assay_name", "")

    @assay_name.setter
    def assay_name(self, value):
        self._assay_name = value
        self.setTitle(value)
