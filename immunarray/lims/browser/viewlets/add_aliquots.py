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
        import pdb
        pdb.set_trace()
        pass
        # loop and create.8
        # aliquot_type
        # msg = u'%s working aliquots created.' % len(created_ids)
        # self.context.plone_utils.addPortalMessage(msg)
        # self.request.response.redirect(bulk.absolute_url())


class AddAliquotsViewletAJAXFeedback(BrowserView):
    """When any input in the add-aliquots viewlet is changed, this
    view returns feedback to the viewlet.
    """

    def __call__(self):

        result = {'success': False, 'feedback': 'Error.'}

        form = self.request.form

        # validate aliquot_volume.
        aliquot_volume = form.get('aliquot_volume', '')
        try:
            aliquot_volume = int(aliquot_volume)
        except ValueError:
            result['feedback'] = 'Volume must be a whole number.'
            return json.dumps(result)
        if not aliquot_volume:
            result['feedback'] = 'Aliquot volume is required.'
            return json.dumps(result)

        # validate aliquot_count
        available_volume = self.context.remaining_volume
        aliquot_count = form.get('aliquot_count', False)
        try:
            if aliquot_count:
                aliquot_count = int(aliquot_count)
        except ValueError:
            result['feedback'] = 'Aliquot count must be a whole number.'
            return json.dumps(result)

        # possibly calculate aliquot_count
        if not aliquot_count:
            dm = divmod(available_volume, aliquot_volume)
            aliquot_count = dm[0]
            remaining_volume = dm[1]

        # Re-calculate aliquot_count, if remaining_volume is insufficient.
        required_volume = aliquot_count * aliquot_volume
        if required_volume > available_volume:
            dm = divmod(available_volume, aliquot_volume)
            aliquot_count = dm[0]
            required_volume = aliquot_count * aliquot_volume
        remaining_volume = available_volume - required_volume

        # Get the sequence start for the new aliquots which will be created.
        veracis_id = self.context.veracis_id
        brains = find(object_provides=[IQCAliquot.__identifier__,
                                       IRandDAliquot.__identifier__],
                      veracis_id=veracis_id)
        sequence_start = len(brains) + 1

        # some variables for the feedback
        aliquot_type = form['aliquot_type']
        s = "s" if aliquot_count > 1 else ""

        result['feedback'] = """{aliquot_count} {aliquot_type} aliquot{s} to be 
        created, using {required_volume} uL of the remaining {available_volume}
        uL and leaving {remaining_volume} uL unallocated. The first aliquot 
        ID will be {veracis_id}-{sequence_start:03d}""".format(**locals())
        result['aliquot_count'] = aliquot_count
        result['success'] = True
        return json.dumps(result)
