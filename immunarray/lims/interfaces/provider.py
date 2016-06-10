from zope import schema

from zope.interface import Interface

from immunarray.lims import messageFactory as _
from immunarray.lims.interfaces.person import IPerson


class IProviderFolder(Interface):
    """Folder to hold test requisitions
    """


class IProvider(IPerson):
    """
    Firstname = schema.ASCIILine(
        title=_(u"Firstname"),
        description=_(u""),
        required=False,
    )
    Lastname = schema.ASCIILine(
        title=_(u"Lastname"),
        description=_(u""),
        required=False,
    )
    EmailAddress = schema.ASCIILine(
        title=_(u"EmailAddress"),
        description=_(u""),
        required=False,
    )
    Phone = schema.ASCIILine(
        title=_(u"Phone number"),
        description=_(u""),
        required=False,
    )
    """
    NPI = schema.ASCIILine(
        title=_(u"NPI"),
        description=_(u"NPI (unique to each provider)"),
        required=True,
    )
    Credentials = schema.ASCIILine(
        title=_(u"Provider Credentials"),
        description=_(u"Provider credentials (M.D.  D.O.)"),
        required=False,
    )
    TaxID = schema.ASCIILine(
        title=_(u"Tax ID"),
        description=_(u"Tax ID"),
        required=False,
    )
    PIN = schema.ASCIILine(
        title=_(u"PIN"),
        description=_(u"PIN"),
        required=False,
    )
    UPIN = schema.ASCIILine(
        title=_(u"UPIN"),
        description=_(u"UPIN"),
        required=False,
    )
    Fax = schema.ASCIILine(
        title=_(u"Fax Number"),
        description=_(u"Fax number for result delivery"),
        required=True,
    )
    PublishingPrefernce = schema.Choice(
        title =_(u"Publishing Preference"),
        description=_(u"Providers desired publincation of resutls"),
        values=[_(u'Fax'), _(u'Mail'), _(u'EMR')],
        required=True,
    )
