# -*- coding: utf-8 -*-
from datetime import date
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.z3cform import layout
from zope import schema
from zope.interface import Interface


class IImmunArrayControlPanel(Interface):

    category_primary = schema.Tuple(
        title=u'NCE Parimary Category',
        default=(u'Process Management', u'Purchasing and Inventory',
                 u'Equipment'),
        missing_value=None,
        required=False,
        value_type=schema.TextLine()
    )

    category_secondary = schema.Tuple(
        title=u'NCE Secondary Category',
        default=(u'Scanning', u'Accessioning', u'Test Preparation',
                 u'Blocking', u'Testing', u'Data Analysis'),
        missing_value=None,
        required=False,
        value_type=schema.TextLine()
    )

    category_tertiary = schema.Tuple(
        title=u'NCE Tertiary Category',
        default=(u'Scanning', u'Accessioning', u'Test Preparation',
                 u'Blocking', u'Testing', u'Data Analysis'),
        missing_value=None,
        required=False,
        value_type=schema.TextLine()
    )


class ImmunArrayControlPanelForm(RegistryEditForm):
    schema = IImmunArrayControlPanel
    schema_prefix = "immunarray"
    label = u'ImmunArray Control Panel Settings'


ImmunArrayControlPanelView = layout.wrap_form(
    ImmunArrayControlPanelForm, ControlPanelFormWrapper)

