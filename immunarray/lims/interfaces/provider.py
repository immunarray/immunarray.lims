from zope import schema

from zope.interface import Interface

from immunarray.lims import messageFactory as _
from bika.lims.interfaces.person import IPerson


class IProvider(IPerson):
    """Care provider
    """

    npi = schema.TextLine(
        title=_(u"NPI"),
        description=_(u"NPI (unique to each provider)"),
        required=True,
    )

    credentials = schema.TextLine(
        title=_(u"Provider Credentials"),
        description=_(u"Provider credentials (M.D.  D.O.)"),
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

    publishing_prefernce = schema.Choice(
        title =_(u"Publishing Preference"),
        description=_(u"Providers desired publincation of resutls"),
        values=[_(u'Fax'), _(u'Mail'), _(u'EMR')],
        required=True,
    )
