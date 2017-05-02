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

    medical_record_number = schema.TextLine(
        title=_(u"Medical Record Number"),
        description=_(u"Medical Record Number"),
        required=False,
    )

    research_consent = schema.Choice(
        title=_(u"Patient Consent to Research"),
        description=_(u"Patient Gives consisent to research use"),
        values=[_(u'No'), _(u'Yes')],
        required=True,
    )

    race = schema.Choice(
        title=_(u"Patient Race"),
        description=_(u"Patient Race"),
        values=[_(u'African American or Black'), _(u'Asian Indian Middle Eastern'), _(u'Caucasian'), _(u'Hispanic or Latino'), _(u'Other')],
        required=False,
    )

    # append to this list to track the sample run on a particular patient

    tested_unique_sample_ids = schema.List(
        title=_(u"List of Unique Sample Numbers"),
        description =_(u"List of Unique Sample Numbers"),
        required=False,
        value_type=schema.TextLine()
    )
