from immunarray.lims.interfaces.sample import ISample
from . import BaseContainer
from zope.interface import implements


class AbstractSample(BaseContainer):
    """This is a base class for all types of sample.
    """
    implements(ISample)

    def __init__(self, *args, **kwargs):
        super(AbstractSample, self).__init__(*args, **kwargs)
        self._initial_volume = 0

    @property
    def initial_volume(self):
        return getattr(self, "_initial_volume", 0)

    @initial_volume.setter
    def initial_volume(self, value):
        # if there's already an _initial_volume, do NOT update remaining_volume.
        already_set = self._initial_volume
        self._initial_volume = value
        if not already_set:
            self.remaining_volume = value
