# -*- coding: utf-8 -*-
from . import BaseContainer


class NoFrameRun(BaseContainer):
    def __init__(self, *args, **kwargs):
        super(NoFrameRun, self).__init__(*args, **kwargs)
