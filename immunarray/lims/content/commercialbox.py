from plone.dexterity.content import Container


class CommercialBox(Container):
    def __init__(self, *args, **kwargs):
        super(CommercialBox, self).__init__(*args, **kwargs)
