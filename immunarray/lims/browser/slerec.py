from Products.Five.browser import BrowserView
from plone import api
from immunarray.lims.interfaces.clinicalsample import IClinicalSample

class RecView(BrowserView):
    """ View that pulls data from multiple content objects
    """

    def usn(self):
        results = []
        brains = api.content.find(context=self.context, portal_type="title")
        for brain in brains
            title = brain.getObject()
            results.append().
