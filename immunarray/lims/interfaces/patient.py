from bika.lims.interfaces.person import IPerson
from immunarray.lims import messageFactory as _
from zope import schema
from zope.interface import Interface


class IPatient(IPerson):
    """Patient record
    """

    dob = schema.Date(
        title=_(u"Date of Birth"),
        description=_(u"Date of Birth"),
        required=False,
    )

    marital_status = schema.Choice(
        title=_(u"Marital Status"),
        description=_(u"Marital Status"),
        values=[_(u'Single'), _(u'Married'), _(u'Other')],
        required=False,
    )

    gender = schema.Choice(
        title=_(u"Gender"),
        description=_(u"Gender"),
        values=[_(u'Male'), _(u'Female'), _(u'Other')],
        required=False,
    )

    ssn = schema.TextLine(
        title=_(u"Social Security Number"),
        description=_(u"Social Security Number"),
        required=False,
    )

    relation_to_insured = schema.Choice(
        title=_(u"Patient Relationship to Insured"),
        description=_(u"Patient relationship to Insured"),
        values=[_(u'Self'), _(u'Spouse'), _(u'Child')],
        required=False,
    )

    unique_sample_number = schema.TextLine(
        title=_(u"Unique Sample Number"),
        description=_(u"Sample ID from the blood draw kit"),
        required=False,
    )

    research_consent = schema.Bool(
        title=_(u"Patient Consent to Research"),
        description=_(u"Patient Gives consisent to research use"),
        required=False,
    )
