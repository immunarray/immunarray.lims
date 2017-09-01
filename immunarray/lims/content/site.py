from . import BaseContainer


class Site(BaseContainer):
    def __init__(self, *args, **kwargs):
        super(Site, self).__init__(*args, **kwargs)

    @property
    def therapak_id(self):
        return getattr(self, "_therapak_id", "")

    @therapak_id.setter
    def therapak_id(self, value):
        self._therapak_id = value
        temp = getattr(self, "_site_name", "")
        self.setTitle(value + " - " + temp)
        self.id = '{}-{}'.format(value, temp)

    @property
    def site_name(self):
        return getattr(self, "_site_name", "")

    @site_name.setter
    def site_name(self, value):
        self._site_name = value
        temp = getattr(self, "_therapak_id", "")
        self.setTitle(temp + " - " + value)
        self.id = '{}-{}'.format(temp, value)
