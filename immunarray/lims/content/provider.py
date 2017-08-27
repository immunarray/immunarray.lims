from plone.dexterity.content import Container


class Provider(Container):
    def __init__(self, *args, **kwargs):
        super(Provider, self).__init__(*args, **kwargs)
