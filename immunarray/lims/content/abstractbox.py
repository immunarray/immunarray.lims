# -*- coding: utf-8 -*-
from immunarray.lims import logger
from zope.interface import implements
from zope.schema.interfaces import IContextAwareDefaultFactory
from plone.api.content import find


class assignBoxNumber():
    """All boxes use this as the default value of their
    box_number fields, allows for a consistent number system.
    """
    implements(IContextAwareDefaultFactory)

    def __init__(self):
        pass

    def __call__(self, context):
        """Pull all box numbers and get the next one.
        """
        brains = find(portal_type=['CommercialBox', 'RandDBox', 'QCBox'],
                      sort_on='box_number',
                      sort_order='reverse', limit=1)
        if brains:
            _id = str(int(brains[0].box_number) + 1)
            return unicode(_id)
        logger.info("assignBoxNumber: No Boxes Exist: using ID '1'")
        return u"1"
