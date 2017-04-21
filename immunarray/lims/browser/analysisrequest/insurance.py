from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api
from immunarray.lims.interfaces.clinicalsample import IClinicalSample


class AddInsuranceView(BrowserView):

    template = ViewPageTemplateFile("templates/billing/insurance.pt")

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.errors = []

    def __call__(self):
        request = self.request

        if "submitted" not in request:
            return self.template()

        # ID
        # This ID should exist in the system as this step follows in the process
        # The USN should selected from ones that have been entered previously

        usn = request.get("usn")
        # Primary Insurance
        insurance_name = request.get("InsuranceName")
        insurance_payer_id = request.get("InsurancePayerID")
        insurance_policy_number = request.get("InsurancePolicyNumber")
        insurance_group_number = request.get("InsuranceGroupNumber")
        insurance_plan_number = request.get("InsurancePlanNumber")
        authorization_precertification = request.get("AuthorizationPrecertification")
        insurance_subscriber_name = request.get("InsuranceSubscriberName")
        relationship_to_insured= request.get(relationship_to_insured)
        insurance_subscriber_dob = request.get("InsuranceSubscriberDOB")
        insurance_subscriber_gender = request.get("insurance_subscriber_gender")
        number_of_days_authorized = request.get("NumberofDaysAuthorized")
        effective_date = request.get("EffectiveDate")
        insurance_address = request.get("InsuranceAddress")
        insurance_city = request.get("InsuranceCity")
        insurance_zip_code = request.get("InsuranceZipCode")
        # Secondary Insurance
        secondary_insurance_name = request.get("SecondaryInsuranceName")
        secondary_insurance_payer_id = request.get("SecondaryInsurancePayerID")
        secondary_insurance_policy_number = request.get("SecondaryInsurancePolicyNumber")
        secondary_insurance_group_number = request.get("SecondaryInsuranceGroupNumber")
        secondary_insurance_plan_number = request.get("SecondaryInsurancePlanNumber")
        secondary_authorization_precertification = request.get("SecondaryAuthorizationPrecertification")
        secondary_insurance_subscriber_name = request.get("SecondaryInsuranceSubscriberName")
        secondary_relationship_to_insured = request.get("secondary_relationship_to_insured")
        secondary_insurance_subscriber_dob = request.get("SecondaryInsuranceSubscriberDOB")
        secondary_insurance_subscriber_gender = request.get("secondary_insurance_subscriber_gender")
        secondary_number_of_days_authorized = request.get("SecondaryNumberofDaysAuthorized")
        secondary_effective_date = request.get("SecondaryEffectiveDate")
        secondary_insurance_address = request.get("SecondaryInsuranceAddress")
        secondary_insurance_city = request.get("SecondaryInsuranceCity")
        secondary_insurance_zip_code = request.get("SecondaryInsuranceZipCode")
        assignment_of_benefits_patient_name = request.get("AssignmentofBenefitsPatientName")
        # Signature section (need to add this to clinical sample!)
        release_signed = request.get("release_signed")
        assignment_of_benefits_signature_date = request.get("AssignmentofBenefitsSignatureDate")
        authorization_signature_patient_name = request.get("AuthorizationSignaturePatientName")
        payment_signed = request.get("payment_signed")
        authorization_signature_signature_date = request.get("AuthorizationSignatureSignatureDate")



    def add_insurance_info_to_clinical_sample(self):
        # find sample that has the usn
        # update fields with data from this input
        portal = api.portal.get("samples")
        obj = api.content.create(
            type = 'ClinicalSample',
            title = usn,
            tests_ordered = ,
            sample_primary_insurance_name = schema.TextLine,
            sample_primary_insurance_payerID = schema.TextLine,
            sample_primary_insurance_policy_number = schema.TextLine,
            sample_primary_insurance_plan_number = schema.TextLine,
            sample_primary_insurance_subscriber_name = schema.TextLine,
            sample_primary_insurance_relation_to_insured = schema.Choice,
            sample_primary_insurance_subscriber_DOB = schema.Date,
            sample_primary_insurance_effective_date = schema.Date,
            sample_primary_insurance_address = schema.TextLine,
            sample_primary_city = schema.TextLine,
            sample_primary_state = schema.TextLine,
            sample_primary_insurance_zip_code = schema.TextLine,
            sample_secondary_insurance_name = schema.TextLine,
            sample_secondary_insurance_payerID = schema.TextLine,
            sample_secondary_insurance_policy_number = schema.TextLine,
            sample_secondary_insurance_plan_number = schema.TextLine,
            sample_secondary_insurance_authorization_precertificate = schema.TextLine,
            sample_secondary_insurance_subscriber_name = schema.TextLine,
            sample_secondary_insurance_relation_to_insured = schema.Choice,
            sample_secondary_insurance_subscriber_DOB = schema.Datetime,
            sample_secondary_insurance_effective_date = schema.Datetime,
            sample_secondary_insurance_address = schema.TextLine,
            sample_secondary_city = schema.TextLine,
            sample_secondary_state = schema.TextLine,
            sample_secondary_insurance_zip_code = schema.TextLine,
            billable_code = schema.Choice,
            sample_serial_number = schema.Int,
            sample_ordering_healthcare_provider = schema.Choice,
            sample_ordering_healthcare_provider_signature = schema.Bool,
            primary_healthcare_provider = schema.Choice,
            ana_teesting = schema.Choice,
            clinical_impression = schema.Choice,
            other_test_ordered = schema.List,
            symptoms_choice = schema.List,
            symptoms_text = schema.List,
            diagnosis_code = schema.List,
            diagnosis_code_other = schema.List,
            phlebotomist_last_name = schema.TextLine,
            phlebotomist_signature_provided=schema.Bool,
            collection_date = schema.Date,
            received_date = schema.Date,
        )
