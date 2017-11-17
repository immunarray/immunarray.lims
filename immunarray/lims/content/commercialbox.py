# -*- coding: utf-8 -*-
from zope import schema
from immunarray.lims.interfaces.storage import ICommercialBox, assignBoxNumber
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer
from immunarray.lims import messageFactory as _

from . import BaseContainer


@implementer(ICommercialBox)
@adapter(Interface)
class CommercialBox(BaseContainer):
    def __init__(self, *args, **kwargs):
        super(CommercialBox, self).__init__(*args, **kwargs)
