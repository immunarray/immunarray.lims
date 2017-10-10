# -*- coding: utf-8 -*-
from immunarray.lims.interfaces.storage import IRandDBox
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer

from . import BaseContainer


@implementer(IRandDBox)
@adapter(Interface)
class RandDBox(BaseContainer):
    def __init__(self, *args, **kwargs):
        super(RandDBox, self).__init__(*args, **kwargs)
