# -*- coding: utf-8 -*-
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets import ViewletBase
from plone.autoform.view import WidgetsView
from plone.dexterity.interfaces import IDexterityFTI
from plone.dexterity.utils import getAdditionalSchemata
from zope.component import getUtility


class WidgetValuesViewlet(ViewletBase):
    """Use this to insert tabular field/value pairs in a viewlet.
    This means we can use views like the default dexterity folder_listing
    view as the base view of an object, but still include the widget values.
    """

    def render(self):
        return WidgetValuesView(self.context, self.request)()


class WidgetValuesView(WidgetsView):
    template = ViewPageTemplateFile("./templates/widgetvalues.pt")

    @property
    def schema(self):
        fti = getUtility(IDexterityFTI, name=self.context.portal_type)
        return fti.lookupSchema()

    @property
    def additionalSchemata(self):
        return getAdditionalSchemata(context=self.context)

    def render(self):
        # noinspection PyArgumentList
        return self.template()
