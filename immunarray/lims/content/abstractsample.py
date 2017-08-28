from immunarray.lims.interfaces.sample import ISample
from plone.dexterity.content import Container
from zope.interface import implements


class AbstractSample(Container):
    """This is a base class for all types of sample.
    """
    implements(ISample)

    def __init__(self, *args, **kwargs):
        super(AbstractSample, self).__init__(*args, **kwargs)

    def __setattr__(self, key, value):
        super(AbstractSample, self).__setattr__(key, value)
        if key == 'initial_volume':
            self.remaining_volume = value
