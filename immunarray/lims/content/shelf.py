from plone.dexterity.content import Container


class Shelf(Container):
    def __init__(self, *args, **kwargs):
        super(Shelf, self).__init__(*args, **kwargs)
