from plone.dexterity.content import Container


class ClinicalSample(Container):
    def __init__(self, *args, **kwargs):
        super(ClinicalSample, self).__init__(*args, **kwargs)
