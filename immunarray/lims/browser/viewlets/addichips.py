from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets import ViewletBase
from plone import api


class AddMultipleiChipsViewlet(ViewletBase):
    index = ViewPageTemplateFile("templates/addichips_viewlet.pt")

    def render(self):
        return self.index()


class AddMultipleiChipsHandler(BrowserView):

    def __call__(self):
        ichiplot = self.context

        try:
            start = int(self.request.form.get('sequence_start', ''))
            end = int(self.request.form.get('sequence_end', ''))
        except ValueError:
            msg = u'Start and End must both be integers'
            self.context.plone_utils.addPortalMessage(msg)
            self.request.response.redirect(ichiplot.absolute_url())
            return

        if not start < end:
            msg = u'End must be higher than Start.'
            self.context.plone_utils.addPortalMessage(msg)
            self.request.response.redirect(ichiplot.absolute_url())
            return

        title = ichiplot.ichiplotID

        for x in range(start, end+1):
            objectname = "{0}_{1}".format(title, x)
            api.content.create(
                type='iChip',
                title=objectname,
                container=ichiplot)
        self.request.response.redirect(ichiplot.absolute_url())
