from immunarray.lims import logger
from plone.api.content import find
from plone.dexterity.content import Container
from zope.interface import implements
from zope.schema._bootstrapinterfaces import IContextAwareDefaultFactory


class BaseContainer(Container):
    """
    """

class AssignBottleNumber():
    """make bottle number for new materials
    """
    implements(IContextAwareDefaultFactory)

    def __init__(self):
        pass

    def __call__(self, context):
        """Pull all Veracis IDs for R&D and QC samples and get the next one.
        """
        brains = find(portal_type=context.REQUEST.URL.split('++')[-1])
        if not brains:
            return 1
        return max([b.getObject().bottle_number for b in brains]) + 1


