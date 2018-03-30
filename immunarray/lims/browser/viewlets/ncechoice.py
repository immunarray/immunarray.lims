from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets import ViewletBase


class NCEChoiceViewlet(ViewletBase):
    index = ViewPageTemplateFile("templates/nce_choice.pt")

    def render(self):
        # noinspection PyArgumentList
        return self.index()
