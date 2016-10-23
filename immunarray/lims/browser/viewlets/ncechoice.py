from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets import ViewletBase
from plone import api


class NCEChoiceViewlet(ViewletBase):
    index = ViewPageTemplateFile("templates/nce_choice.pt")

    def render(self):
        return self.index()
