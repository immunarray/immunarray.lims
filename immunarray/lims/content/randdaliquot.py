from immunarray.lims.content.abstractaliquot import AbstractAliquot


class RandDAliquot(AbstractAliquot):
    def __init__(self, *args, **kwargs):
        super(RandDAliquot, self).__init__(*args, **kwargs)

    @property
    def veracis_id(self):
        """Return the veracis_id of the sample this aliquot originated from.
        """
        parent = self.aq_parent
        while not ISample.providedBy(parent):
            parent = self.aq_parent
        return parent.veracis_id
