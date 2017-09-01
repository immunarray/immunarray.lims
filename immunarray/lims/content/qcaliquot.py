# -*- coding: utf-8 -*-
from immunarray.lims.content.abstractaliquot import AbstractAliquot
from immunarray.lims.interfaces.sample import ISample


class QCAliquot(AbstractAliquot):
    def __init__(self, *args, **kwargs):
        super(QCAliquot, self).__init__(*args, **kwargs)

    def get_veracis_id(self):
        """Return the veracis_id of the sample this aliquot originated from.
        """
        parent = self.aq_parent
        while not ISample.providedBy(parent):
            parent = self.aq_parent
        return parent.veracis_id
