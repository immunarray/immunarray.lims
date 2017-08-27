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
        # After this block, aliquot_volume WILL be defined.
        try:
            aliquot_volume = form.get('aliquot_volume', '')
            aliquot_volume = int(aliquot_volume)
        except ValueError:
            result['feedback'] = 'Volume must be a whole number.'
            return json.dumps(result)
        if not aliquot_volume:
            result['feedback'] = 'Aliquot volume is required.'
            return json.dumps(result)

        # validate aliquot_count.  If no count is entered, calculate
        # from parent's remaining_volume / entered aliquot_volume.
        # after this block, aliquot_count and remaining_volume WILL be defined.
        parent_volume = self.context.remaining_volume
        try:
            aliquot_count = form.get('aliquot_count', 0)
            aliquot_count = int(aliquot_count)
        except ValueError:
            result['feedback'] = 'Aliquot count must be a whole number.'
            return json.dumps(result)
        if not aliquot_count:
            dm = divmod(parent_volume, aliquot_volume)
            aliquot_count = dm[0]
            # this aliquot_count will be set in the viewlet's input element.
            result['aliquot_count'] = aliquot_count
            required_volume = aliquot_count * aliquot_volume
            remaining_volume = dm[1]
        else:
            required_volume = aliquot_count * aliquot_volume
            if required_volume > parent_volume:
                result['feedback'] = \
                    "Remaining volume is not sufficient for requested aliquots."
                return json.dumps(result)
            remaining_volume = parent_volume - required_volume

        # Get the sequence start for the new aliquots which will be created.
        brains = find(object_provides=[IQCAliquot.__identifier__,
                                       IRandDAliquot.__identifier__],
                      veracis_id=self.context.veracis_id)
        sequence_start = len(brains)

        aliquot_type = form['aliquot_type']
        result['feedback'] = """{aliquot_count} {aliquot_type} aliquots will 
        be created, using {required_volume} uL of {parent_volume} uL 
        remaining on {self.context.id}, and leavning {remaining_volume} 
        unallocated.""".format(**locals())
        result['success'] = True
        return json.dumps(result)
