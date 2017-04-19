from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class AddInsuranceView(BrowserView):

    template = ViewPageTemplateFile("templates/billing/insurance.pt")

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.errors = []

    def __call__(self):
        request = self.request

        if "submitted" not in request:
            return self.template()


