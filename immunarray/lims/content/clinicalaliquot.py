from plone.dexterity.content import Container


class ClinicalAliquot(Container):
    def __init__(self, *args, **kwargs):
        super(ClinicalAliquot, self).__init__(*args, **kwargs)
