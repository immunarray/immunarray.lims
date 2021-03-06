import json

from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from immunarray.lims.interfaces.qcaliquot import IQCAliquot
from immunarray.lims.interfaces.qcsample import IQCSample
from immunarray.lims.interfaces.randdaliquot import IRandDAliquot
from immunarray.lims.interfaces.sample import ISample
from plone.api.content import create, find, get_state
from plone.app.layout.viewlets import ViewletBase


class AddAliquotsViewlet(ViewletBase):
    index = ViewPageTemplateFile("templates/add-aliquots.pt")

    def render(self):
        if get_state(self.context, 'cancelled'):
            return ''
        else:
            # noinspection PyArgumentList
            return self.index()


class AddAliquotsViewletSubmit(BrowserView):
    def __init__(self, context, request):
        super(AddAliquotsViewletSubmit, self).__init__(context, request)
        self.context = context
        self.request = request

    def __call__(self):
        form = self.request.form

        aliquot_type = form.get('aliquot_type', False)
        if not aliquot_type:
            msg = u'You must select the type of aliquot to be created.'
            self.context.plone_utils.addPortalMessage(msg)
            self.request.response.redirect(self.context.absolute_url())

        aliquot_volume = form.get('aliquot_volume', False)
        aliquot_count = form.get('aliquot_count', False)
        if not all([aliquot_type, aliquot_volume, aliquot_count]):
            msg = u'One of Aliquot type, volume or count was not defined!'
            self.context.plone_utils.addPortalMessage(msg)
            self.request.response.redirect(self.context.absolute_url())

        try:
            aliquot_volume = int(aliquot_volume)
            aliquot_count = int(aliquot_count)
        except (ValueError, TypeError):
            msg = u'Aliquot volume and count must both be whole numbers!'
            self.context.plone_utils.addPortalMessage(msg)
            self.request.response.redirect(self.context.absolute_url())

        sequence_start = get_sequence_start(self.context.veracis_id)

        # Discover if it's RandD or QC aliquots that we will be creating.
        sample = _get_parent_sample(self.context)
        if IQCSample.providedBy(sample):
            aliquot_portal_type = 'QCAliquot'
        else:
            aliquot_portal_type = 'RandDAliquot'

        # Create aliquots
        for seq in range(sequence_start, sequence_start + aliquot_count):
            _id = "{self.context.veracis_id}-{seq:03d}".format(**locals())
            _title = "{self.context.veracis_id} - {seq:03d}".format(**locals())
            aliquot = create(self.context,
                             aliquot_portal_type,
                             _id,
                             initial_volume=aliquot_volume,
                             aliquot_type=aliquot_type)
            aliquot.setTitle(_title)

        self.context.remaining_volume -= aliquot_volume * aliquot_count
        self.context.reindexObject(idxs=['remaining_volume'])

        msg = '{} {} aliquots created. Remaining volume on "{}" is {} uL' \
            .format(aliquot_count,
                    aliquot_type.lower(),
                    self.context.title,
                    self.context.remaining_volume)
        self.context.plone_utils.addPortalMessage(msg)
        self.request.response.redirect(self.context.absolute_url())


class AddAliquotsViewletAJAXFeedback(BrowserView):
    """When any input in the add-aliquots viewlet is changed, this
    view returns feedback to the viewlet.
    """

    def __call__(self):
        result = {'success': False, 'feedback': 'Error.'}

        form = self.request.form

        # validate aliquot_type
        aliquot_type = form.get('aliquot_type', False)
        if not aliquot_type:
            result['feedback'] = \
                u'You must select the type of aliquot to be created.'
            return json.dumps(result)

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
        sequence_start = get_sequence_start(veracis_id)

        # some variables for the feedback
        aliquot_type = form['aliquot_type']
        s = "s" if aliquot_count > 1 else ""

        result['feedback'] = \
            """{aliquot_count} {aliquot_type} aliquot{s} will be created,
            using {required_volume} uL and leaving {remaining_volume} uL
            unallocated. The first aliquot ID will be
            {veracis_id}-{sequence_start:03d}""".format(**locals())
        result['aliquot_count'] = aliquot_count
        result['success'] = True
        return json.dumps(result)


def get_sequence_start(veracis_id):
    """Discover the next available aliquot number for the sample with
    the provided veracis_id.
    """
    brains = find(object_provides=[IQCAliquot.__identifier__,
                                   IRandDAliquot.__identifier__],
                  veracis_id=veracis_id)
    return len(brains) + 1


def _get_parent_sample(context):
    """Get the sample associated with the current context.
    """
    parent = context
    while not ISample.providedBy(parent):
        parent = parent.aq_parent
    return parent
