from . import BaseContainer


class Box(BaseContainer):
    def __init__(self, *args, **kwargs):
        super(Box, self).__init__(*args, **kwargs)


    @property
    def max_samples(self):
        return getattr(self, "_max_samples", 0)

    @max_samples.setter
    def max_samples(self, value):
        # if there's already an _max_samples, do NOT update remaining_volume.
        already_set = getattr(self, '_max_samples', False)
        self._max_samples = value
        if not already_set:
            self.remaining_volume = value
