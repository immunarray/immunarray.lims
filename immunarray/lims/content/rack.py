from plone.dexterity.content import Container


class Rack(Container):
    def __init__(self, *args, **kwargs):
        super(Rack, self).__init__(*args, **kwargs)
