# -*- coding: utf-8 -*-
from immunarray.lims.interfaces.storage import IQCBox
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer

from . import BaseContainer


@implementer(IQCBox)
@adapter(Interface)
class QCBox(BaseContainer):
    def __init__(self, *args, **kwargs):
        super(QCBox, self).__init__(*args, **kwargs)

