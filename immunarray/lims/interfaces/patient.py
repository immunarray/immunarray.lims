from zope import schema

from zope.interface import Interface

from immunarray.lims import messageFactory as _
from immunarray.lims.interfaces.person import IPerson


class IPatientFolder(Interface):
    """Folder to hold test requisitions
    """


class IPatient(IPerson):
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
    Address = schema.ASCIILine(
        title=_(u"Address"),
        description=_(u"Street Address"),
        required=False,
    )
    City = schema.ASCIILine(
        title=_(u"City"),
        description=_(u"City"),
        required=False,
    )
    State = schema.ASCIILine(
        title=_(u"State"),
        description=_(u"State"),
        required=False,
    )
    """Should/Could we do a format or XXXXX-XXXX"""
    ZipCode = schema.ASCIILine(
        title=_(u"Zip Code"),
        description=_(u"Zip Code"),
        required=False,
    )
    DOB = schema.Date(
        title=_(u"Date of Birth"),
        description=_(u"Date of Birth"),
        required=False,
    )
    MaritalStatus = schema.Choice(
        title=_(u"Marital Status"),
        description=_(u"Marital Status"),
        values=[_(u'Single'), _(u'Married'), _(u'Other')],
        required=False,
    )
    Gender = schema.Choice(
        title=_(u"Gender"),
        description=_(u"Gender"),
        values=[_(u'Male'), _(u'Female'), _(u'Other')],
        required=False,
    )
    SSN = schema.ASCIILine(
        title=_(u"Social Security Number"),
        description=_(u"Social Security Number"),
        required=False,
    )
    RelationToInsured = schema.Choice(
        title=_(u"Patient Relationship to Insured"),
        description=_(u"Patient relationship to Insured"),
        values=[_(u'Self'), _(u'Spouse'), _(u'Child')],
        required=False,
    )
    UniqueSampleNumber = schema.ASCIILine(
        title=_(u"Unique Sample Number"),
        description=_(u"Sample ID from the blood draw kit"),
        required=False,
    )
    ResearchConsent = schema.Bool(
        title=_(u"Patient Consent to Research"),
        description=_(u"Patient Gives consisent to research use"),
        required=False,
    )
