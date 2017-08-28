from plone.dexterity.content import Container


class BaseContainer(Container):
    def __getattr__(self, key):
        """Allows to define get_XYZ, to be used automatically when getting 
        the XYZ attribute on subclasses of this base container.
        """
        if hasattr(self, 'get_' + key) and not key.startswith('get_'):
            return getattr(self, 'get_' + key)()
        return super(BaseContainer, self).__getattr__(key)

    def __setattr__(self, key, value):
        """Allows to define set_XYZ, to be used automatically when setting 
        the XYZ attribute on subclasses of this base container.
        """
        super(BaseContainer, self).__setattr__(key, value)
        try:
            getattr(self, 'set_' + key)(value)
        except AttributeError:
            pass
