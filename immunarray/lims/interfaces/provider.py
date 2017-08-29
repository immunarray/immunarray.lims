# -*- coding: utf-8 -*-
from bika.lims.interfaces.person import IPerson
from immunarray.lims import messageFactory as _
from zope import schema


class IProvider(IPerson):
    """Care provider
    """

    site_ID = schema.Int(
        title=_(u"Site ID"),
        description=_(u"Site ID"),
        required=False,
    )

    npi = schema.TextLine(
        title=_(u"NPI"),
        description=_(u"NPI (unique to each provider)"),
        required=True,
    )

    credentials = schema.Choice(
        title=_(u"Provider Credentials"),
        description=_(u"Provider credentials (M.D.  D.O.)"),
        values=[_(u'MD'), _(u'DO'), _(u'PA-C'), _(u'MD/PhD'), _(u'PhD')],
        required=False,
    )

    tax_id = schema.TextLine(
        title=_(u"Tax ID"),
        description=_(u"Tax ID"),
        required=False,
    )

    pin = schema.TextLine(
        title=_(u"PIN"),
        description=_(u"PIN"),
        required=False,
    )

    upin = schema.TextLine(
        title=_(u"UPIN"),
        description=_(u"UPIN"),
        required=False,
    )

    publishing_preference = schema.Choice(
        title=_(u"Publishing Preference"),
        description=_(u"Providers desired publincation of resutls"),
        values=[_(u'Fax'), _(u'Mail'), _(u'EMR')],
        required=True,
    )

    test_report_preference = schema.Choice(
        title=_(u"Labortory Report Preference"),
        description=_(u"Labortory Report Preference"),
        values=[_(u'Standard'), _(u'Extended')],
        required=True,
    )
