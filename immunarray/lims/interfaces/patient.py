from bika.lims.interfaces.person import IPerson
from immunarray.lims import messageFactory as _
from zope import schema
from zope.interface import Interface


class IPatient(IPerson):
    """

    Firstname = schema.TextLine(
        title=_(u"Firstname"),
        description=_(u""),
        required=False,
    )
    Lastname = schema.TextLine(
        title=_(u"Lastname"),
        description=_(u""),
        required=False,
    )
    EmailAddress = schema.TextLine(
        title=_(u"EmailAddress"),
        description=_(u""),
        required=False,
    )
    Phone = schema.TextLine(
        title=_(u"Phone number"),
        description=_(u""),
        required=False,
    )
    """
    Address = schema.TextLine(
        title=_(u"Address"),
        description=_(u"Street Address"),
        required=False,
    )
    City = schema.TextLine(
        title=_(u"City"),
        description=_(u"City"),
        required=False,
    )
    State = schema.TextLine(
        title=_(u"State"),
        description=_(u"State"),
        required=False,
    )
    """Should/Could we do a format or XXXXX-XXXX"""
    ZipCode = schema.TextLine(
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
    SSN = schema.TextLine(
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
    UniqueSampleNumber = schema.TextLine(
        title=_(u"Unique Sample Number"),
        description=_(u"Sample ID from the blood draw kit"),
        required=False,
    )
    ResearchConsent = schema.Bool(
        title=_(u"Patient Consent to Research"),
        description=_(u"Patient Gives consisent to research use"),
        required=False,
    )
