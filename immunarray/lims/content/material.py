from plone.dexterity.content import Container


class Material(Container):
    def __init__(self, *args, **kwargs):
        super(Material, self).__init__(*args, **kwargs)
