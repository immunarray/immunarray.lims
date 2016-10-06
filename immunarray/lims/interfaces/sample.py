from datetime import date
from plone.app.textfield import RichText
from zope import schema
from immunarray.lims import messageFactory as _
from plone.dexterity.utils import createContentInContainer
from bika.lims.interfaces.sample import ISample

class ISample(ISample):
    """Sample that will contain all the billing info and high levle information
        that is applicalbe to all aliqouts made from this material
    """
    unique_sample_number = schema.TextLine(
        title=_(u"Unique Sample Number"),
        description=_(u"Sample ID from the blood draw kit"),
        required=False,
    )

    sample_primary_insurance_name = schema.TextLine(
        title=_(u"Primary Insurance Name"),
        description =_(u"Primary Insurance Name"),
        required=False,
    )

    sample_primary_insurance_payerID = schema.TextLine(
        title=_(u"Primary Insurance Payer ID"),
        description =_(u"Primary Insurance Payer ID"),
        required=False,
    )

    sample_primary_insurance_policy_number = schema.TextLine(
        title=_(u"Primary Insurance Policy Number"),
        description =_(u"Primary Insurance Policy Number"),
        required=False,
    )

    sample_primary_insurance_plan_number = schema.TextLine(
        title=_(u"Primary Insurance Plan Number"),
        description =_(u"Primary Insurance Plan Number"),
        required=False,
    )

    sample_primary_insurance_authorization_precertificate = schema.TextLine(
        title=_(u"Primary Insurance Authorization"),
        description =_(u"Primary Insurance Authorization"),
        required=False,
    )

    sample_primary_insurance_subscriber_name = schema.TextLine(
        title=_(u"Primary Insurance Subscriber Name"),
        description =_(u"Primary Insurance Subscriber Name"),
        required=False,
    )

    sample_primary_insurance_relation_to_insured = schema.Choice(
        title=_(u"Primary Insurance Relation to Insured"),
        description =_(u"Primary Insurance Relation to Insured"),
        values=[_(u"Self"), _("Spouse"), _("Child"),_("Other")],
        required=False,
    )

    sample_primary_insurance_subscriber_DOB = schema.Date(
        title=_(u"Primary Insurance Subscriber DOB"),
        description =_(u"Primary Insurance Subscriber DOB"),
        required=False,
    )

    sample_primary_insurance_effective_date = schema.Date(
        title=_(u"Primary Insurance Effective Date"),
        description =_(u"Primary Insurance Effective Date"),
        required=False,
    )

    sample_primary_insurance_address = schema.TextLine(
        title=_(u"Primary Insurance Address"),
        description =_(u"Primary Insurance Address"),
        required=False,
    )

    sample_primary_city = schema.TextLine(
        title=_(u"Primary Insurance City"),
        description =_(u"Primary Insurance City"),
        required=False,
    )

    sample_primary_state = schema.TextLine(
        title=_(u"Primary Insurance State"),
        description =_(u"Primary Insurance State"),
        required=False,
    )

    sample_primary_insurance_zip_code = schema.TextLine(
        title=_(u"Primary Insurance Zip Code"),
        description =_(u"Primary Insurance Zip Code"),
        required=False,
    )

sample_secondary_insurance_name = schema.TextLine(
    title=_(u"Secondary Insurance Name"),
    description =_(u"Secondary Insurance Name"),
    required=False,
)

sample_secondary_insurance_payerID = schema.TextLine(
    title=_(u"Secondary Insurance Payer ID"),
    description =_(u"Secondary Insurance Payer ID"),
    required=False,
)

sample_secondary_insurance_policy_number = schema.TextLine(
    title=_(u"Secondary Insurance Policy Number"),
    description =_(u"Secondary Insurance Policy Number"),
    required=False,
)

sample_secondary_insurance_plan_number = schema.TextLine(
    title=_(u"Secondary Insurance Plan Number"),
    description =_(u"Secondary Insurance Plan Number"),
    required=False,
)

sample_secondary_insurance_authorization_precertificate = schema.TextLine(
    title=_(u"Secondary Insurance Authorization"),
    description =_(u"Secondary Insurance Authorization"),
    required=False,
)

sample_secondary_insurance_subscriber_name = schema.TextLine(
    title=_(u"Secondary Insurance Subscriber Name"),
    description =_(u"Secondary Insurance Subscriber Name"),
    required=False,
)

sample_secondary_insurance_relation_to_insured = schema.Choice(
    title=_(u"Secondary Insurance Relation to Insured"),
    description =_(u"Secondary Insurance Relation to Insured"),
    values=[_(u"Self"), _("Spouse"), _("Child"),_("Other")],
    required=False,
)

sample_secondary_insurance_subscriber_DOB = schema.Date(
    title=_(u"Secondary Insurance Subscriber DOB"),
    description =_(u"Secondary Insurance Subscriber DOB"),
    required=False,
)

sample_secondary_insurance_effective_date = schema.Date(
    title=_(u"Secondary Insurance Effective Date"),
    description =_(u"Secondary Insurance Effective Date"),
    required=False,
)

sample_secondary_insurance_address = schema.TextLine(
    title=_(u"Secondary Insurance Address"),
    description =_(u"Secondary Insurance Address"),
    required=False,
)

sample_secondary_city = schema.TextLine(
    title=_(u"Secondary Insurance City"),
    description =_(u"Secondary Insurance City"),
    required=False,
)

sample_secondary_state = schema.TextLine(
    title=_(u"Secondary Insurance State"),
    description =_(u"Secondary Insurance State"),
    required=False,
)

sample_secondary_insurance_zip_code = schema.TextLine(
    title=_(u"Secondary Insurance Zip Code"),
    description =_(u"Secondary Insurance Zip Code"),
    required=False,
)
