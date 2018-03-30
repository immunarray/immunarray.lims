from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.api.content import get_state
from plone.app.layout.viewlets import ViewletBase


class CancelledViewlet(ViewletBase):
    """Show a warning if the currently being viewed object is cancelled
    """
    index = ViewPageTemplateFile("templates/cancelled-viewlet.pt")

    def render(self):
        if get_state(self.context) == 'cancelled':
            # noinspection PyArgumentList
            return self.index()
        return ''
