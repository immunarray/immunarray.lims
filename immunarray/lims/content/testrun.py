# -*- coding: utf-8 -*-
from plone.api.content import find

from . import BaseContainer


class TestRun(BaseContainer):
    def __init__(self, *args, **kwargs):
        super(TestRun, self).__init__(*args, **kwargs)

    @property
    def framecount(self):
        """Return the framecount from the assigned ichip-assay
        """
        try:
            ia = find(UID=self.assay_uid)[0].getObject()
        except IndexError:
            msg = "Shouldn't happen, Can't resolve ichip assay for testrun."
            raise RuntimeError(msg)
        return ia.framecount if ia.framecount else 5

    @property
    def import_log(self):
        if hasattr(self, '_import_log'):
            return self._import_log
        else:
            return []

    @import_log.setter
    def import_log(self, value):
        self._import_log = value
