from immunarray.lims.content.abstractaliquot import AbstractAliquot


class QCAliquot(AbstractAliquot):
    def __init__(self, *args, **kwargs):
        super(QCAliquot, self).__init__(*args, **kwargs)
