# -*- coding: utf-8 -*-
from datetime import date
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.z3cform import layout
from zope import schema
from zope.interface import Interface


class IImmunArrayControlPanel(Interface):

    category_primary = schema.Tuple(
        title=u"NCE Parimary Category",
        description=u"NCE Parimary Category",
        required=False,
        value_type=schema.TextLine()
    )

    category_secondary = schema.Tuple(
        title=u"NCE Secondary Category",
        description=u"NCE Secondary Category",
        required=False,
        value_type=schema.TextLine()
    )

    category_tertiary = schema.Tuple(
        title=u'NCE Tertiary Category',
        description=u'NCE Tertiary Category',
        required=False,
        value_type=schema.TextLine()
    )

    diagnostic_codes = schema.Tuple(
        title=u'Diagnostic/Billing Codes',
        description=u'Diagnostic/Billing Codes',
        required=False,
        value_type=schema.TextLine()
    )


class ImmunArrayControlPanelForm(RegistryEditForm):
    schema = IImmunArrayControlPanel
    schema_prefix = "immunarray"
    label = u'ImmunArray Control Panel Settings'


ImmunArrayControlPanelView = layout.wrap_form(
    ImmunArrayControlPanelForm, ControlPanelFormWrapper)

