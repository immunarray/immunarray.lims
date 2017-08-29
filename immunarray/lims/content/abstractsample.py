from immunarray.lims import logger
from immunarray.lims.interfaces.sample import ISample
from zope.interface import implements
from zope.schema.interfaces import IContextAwareDefaultFactory
from plone.api.content import find

from . import BaseContainer


class assignVeracisId():
    """QC and RandD samples use this as the default value of their 
    veracis_id fields.
    """
    implements(IContextAwareDefaultFactory)

    def __init__(self):
        pass

    def __call__(self, context):
        """Pull all Veracis IDs for R&D and QC samples and get the next one.
        """
        brains = find(portal_type=['QCSample', 'RandDSample'],
                      sort_on='veracis_id',
                      sort_order='reverse', limit=1)
        if brains:
            _id = str(int(brains[0].veracis_id) + 1)
            return unicode(_id)
        logger.info("assignVeracisId: No QC or RandD samples: using ID '1000'")
        return u"1000"


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
