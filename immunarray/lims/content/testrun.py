# -*- coding: utf-8 -*-
from plone.api.content import find

from . import BaseContainer


class TestRun(BaseContainer):
    def __init__(self, *args, **kwargs):
        super(TestRun, self).__init__(*args, **kwargs)

    def framecount(self):
        """Return the framecount from the assigned ichip-assay
        """
        try:
            ia = find(UID=self.assay_uid)[0]
        except IndexError:
            msg = "Can't resolve the iChipAssay for this TestRun!"
            raise RuntimeError(msg)
        return ia.framecount
