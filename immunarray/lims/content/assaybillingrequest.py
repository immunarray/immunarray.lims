from . import BaseContainer


class AssayBillingRequest(BaseContainer):
    def __init__(self, *args, **kwargs):
        super(AssayBillingRequest, self).__init__(*args, **kwargs)

    @property
    def assay_name(self):
        return getattr(self, "_assay_name", "")

    @assay_name.setter
    def assay_name(self, value):
        self._assay_name = value
        temp = getattr(self, "_program_name", "")
        self.setTitle(value + " - " + temp)

    @property
    def program_name(self):
        return getattr(self, "_program_name", "")

    @program_name.setter
    def program_name(self, value):
        self._assay_name = value
        temp = getattr(self, "_assay_name", "")
        self.setTitle(temp + " - " + value)
