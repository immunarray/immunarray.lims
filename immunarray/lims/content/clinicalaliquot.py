# -*- coding: utf-8 -*-
from immunarray.lims.content.abstractaliquot import AbstractAliquot


class ClinicalAliquot(AbstractAliquot):
    def __init__(self, *args, **kwargs):
        super(ClinicalAliquot, self).__init__(*args, **kwargs)
