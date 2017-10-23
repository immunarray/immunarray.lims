# -*- coding: utf-8 -*-
from immunarray.lims.interfaces.storage import ICommercialBox
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer

from . import BaseContainer


@implementer(ICommercialBox)
@adapter(Interface)
class CommercialBox(BaseContainer):
    def __init__(self, *args, **kwargs):
        super(CommercialBox, self).__init__(*args, **kwargs)

    box_number = schema.TextLine(
        title=_(u'Box Number'),
        description=_(u'Box Number'),
        defaultFactory=assignBoxNumber(),
        required=True,
    )
