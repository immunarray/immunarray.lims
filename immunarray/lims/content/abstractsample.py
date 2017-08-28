from immunarray.lims.interfaces.sample import ISample
from . import BaseContainer
from zope.interface import implements


class AbstractSample(BaseContainer):
    """This is a base class for all types of sample.
    """
    implements(ISample)

    def __init__(self, *args, **kwargs):
        super(AbstractSample, self).__init__(*args, **kwargs)

    def set_initial_volume(self, value):
        self.remaining_volume = value
