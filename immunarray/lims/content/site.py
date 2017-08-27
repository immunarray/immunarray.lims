from plone.dexterity.content import Container


class Site(Container):
    def __init__(self, *args, **kwargs):
        super(Site, self).__init__(*args, **kwargs)
