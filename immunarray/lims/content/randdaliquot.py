from immunarray.lims.content.abstractaliquot import AbstractAliquot


class RandDAliquot(AbstractAliquot):
    def __init__(self, *args, **kwargs):
        super(RandDAliquot, self).__init__(*args, **kwargs)
