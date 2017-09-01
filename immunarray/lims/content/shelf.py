# -*- coding: utf-8 -*-
from . import BaseContainer


class Shelf(BaseContainer):
    def __init__(self, *args, **kwargs):
        super(Shelf, self).__init__(*args, **kwargs)
