from plone.dexterity.content import Container


class Freezer(Container):
    def __init__(self, *args, **kwargs):
        super(Freezer, self).__init__(*args, **kwargs)
