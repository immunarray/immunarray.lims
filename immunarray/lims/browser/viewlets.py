from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets import ViewletBase
from plone import api

from immunarray.lims.interfaces.aliquot import IAliquot


class AddMultipleIChipsViewlet(ViewletBase):
    index = ViewPageTemplateFile("templates/addichips_viewlet.pt")

    def render(self):
        return self.index()


class AddMultipleIChipsHandler(BrowserView):

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

        title = ichiplot.IChipLotID

        for x in range(start, end+1):
            objectname = "{0}_{1}".format(title, x)
            api.content.create(
                type='ichip',
                title=objectname,
                container=ichiplot)
        self.request.response.redirect(ichiplot.absolute_url())

class AddWorkingAliquotFromBulkViewlet(ViewletBase):
    index = ViewPageTemplateFile(
        "templates/addworkingaliquotfrombulk_viewlet.pt")

    def render(self):
        return self.index()


class AddWorkingAliquotFromBulkHandler(BrowserView):

    def __call__(self):

        bulk = self.context

        try:
            count = int(self.request.form.get('count', ''))
            volume = self.request.form.get('volume', '').lower()
            if 'ul' in volume:
                volume = volume.replace('ul', '').strip()
            volume = int(volume)
        except ValueError:
            msg = u'Count and Volume must both be integers'
            self.context.plone_utils.addPortalMessage(msg)
            self.request.response.redirect(bulk.absolute_url())
            return
        if not (count or volume):
            msg = u'Count and Volume must both be greater than 0'
            self.context.plone_utils.addPortalMessage(msg)
            self.request.response.redirect(bulk.absolute_url())
            return

        # the bulk aliquot at XXX-A01 creates working aliquots A02, A03...
        # we want to extend this series.
        basename = self.context.id[:-2]  # XXX-A

        for x in range(2, 100):
            tmp_id = "%s%02d"%(basename, x)
            proxies = api.content.find(object_provides=IAliquot, id=tmp_id)
            if not proxies:
                break
        else:
            msg = u"Cannot find ID for new working aliquots (shouldn't happen)."
            self.context.plone_utils.addPortalMessage(msg)
            self.request.response.redirect(bulk.absolute_url())
            return

        bulk_volume = self.context.Volume
        req_volume = volume * count
        if req_volume > bulk_volume:
            msg = u'Not enough bulk material (%s required, %s available).' % \
                  (req_volume, bulk_volume)
            self.context.plone_utils.addPortalMessage(msg)
            self.request.response.redirect(bulk.absolute_url())
            return

        created_ids = []
        for x in range(x, x + count):
            new_id = "%s%02d"%(basename, x)
            new_aliquot = api.content.create(
                type='aliquot',
                title=new_id,
                container=bulk)
            self.context.Volume -= volume
            new_aliquot.Volume = volume
            new_aliquot.Use = "Working"
            new_aliquot.Status = "Available"
            new_aliquot.FluidType = self.context.FluidType
            new_aliquot.Department = self.context.Department
            created_ids.append(new_id)

        msg = u'%s working aliquots created.' % len(created_ids)
        self.context.plone_utils.addPortalMessage(msg)
        self.request.response.redirect(bulk.absolute_url())
