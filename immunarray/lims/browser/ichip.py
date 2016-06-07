from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


from plone.dexterity.browser.view import DefaultView

class SessionView(DefaultView):
    pass

class IChipView(BrowserView):
    """"IChipView """
    template = ViewPageTemplateFile("templates/ichipview.pt")

    def __call__(self):
        return self.template()
