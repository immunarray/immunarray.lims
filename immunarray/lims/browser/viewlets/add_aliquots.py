import json

from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from immunarray.lims.interfaces.qcaliquot import IQCAliquot
from immunarray.lims.interfaces.randdaliquot import IRandDAliquot
from plone.api.content import find
from plone.app.layout.viewlets import ViewletBase


class AddAliquotsViewlet(ViewletBase):
    index = ViewPageTemplateFile("templates/add-aliquots.pt")

    def render(self):
        return self.index()

    def __call__(self):
        import pdb;
        pdb.set_trace();
        pass
        # loop and create.8
        # aliquot_type
        # msg = u'%s working aliquots created.' % len(created_ids)
        # self.context.plone_utils.addPortalMessage(msg)
        # self.request.response.redirect(bulk.absolute_url())


class AddAliquotsViewletAJAXHandler(BrowserView):
    """When any input in the add-aliquots viewlet is changed, this
    view returns feedback to the viewlet.
    """

    def __call__(self):

        result = {
            'success': False,
            'feedback': 'Error.',
        }

        # validate aliquot_volume
        try:
            aliquot_volume = self.request.form.get('aliquot_volume', '')
            aliquot_volume = int(aliquot_volume)
        except ValueError:
            result['feedback'] = 'Volume must be a whole number.'
            return json.dumps(result)
        if not aliquot_volume:
            result['feedback'] = 'Aliquot volume is required.'
            return json.dumps(result)

        # validate aliquot_count.  If no count is entered, calculate
        # from parent's remaining_volume / entered aliquot_volume.
        try:
            aliquot_count = self.request.form.get('aliquot_count', '')
            aliquot_count = int(aliquot_count)
        except ValueError:
            result['feedback'] = 'Aliquot count must be a whole number.'
            return json.dumps(result)
        if not aliquot_count:
            dm = divmod(self.context.remaining_volume, aliquot_volume)
            aliquot_count, remaining_volume = dm
            result['aliquot_count'] = aliquot_count
        else:
            required_volume = aliquot_count * aliquot_volume
            if required_volume > self.context.remaining_volume:
                result['feedback'] = \
                    "Remaining volume is not sufficient for requested aliquots."
                return json.dumps(result)
            remaining_volume = self.context.remaining_volume - required_volume

        # brains = find(object_provides=[IQCAliquot.__identifier__,
        #                                IRandDAliquot.__identifier__],
        #               veracis_id=self.context.veracis_id,
        #               sort_on='id',
        #               sort_order='reverse',
        #               limit=1)
        brains = find(object_provides=[IQCAliquot.__identifier__,
                                       IRandDAliquot.__identifier__],
                      path={'query': self.context.getPhysicalPath(),
                            'level': '1',
                            'depth': '1',})
        sequence_start = len(brains)
