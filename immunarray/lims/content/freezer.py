# -*- coding: utf-8 -*-
from . import BaseContainer


class Freezer(BaseContainer):
    def __init__(self, *args, **kwargs):
        super(Freezer, self).__init__(*args, **kwargs)
