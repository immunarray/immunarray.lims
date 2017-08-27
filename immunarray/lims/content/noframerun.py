from plone.dexterity.content import Container


class NoFrameRun(Container):
    def __init__(self, *args, **kwargs):
        super(NoFrameRun, self).__init__(*args, **kwargs)
