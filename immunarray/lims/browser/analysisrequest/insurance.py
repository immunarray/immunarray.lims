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
        relationship_to_insured= request.get("relationship_to_insured")
        insurance_subscriber_dob = request.get("InsuranceSubscriberDOB")
        insurance_subscriber_gender = request.get("insurance_subscriber_gender")
        number_of_days_authorized = request.get("NumberofDaysAuthorized")
        effective_date = request.get("EffectiveDate")
        insurance_address = request.get("InsuranceAddress")
        insurance_city = request.get("InsuranceCity")
        insurance_state = request.get("InsuranceState")
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
        secondary_insurance_zip_code= request.get("SecondaryInsuranceZipCode")
        secondary_insurance_state = request.get("SecondaryInsuranceState")
        # Signature section (need to add this to clinical sample!)
        # = request.get("AssignmentofBenefitsPatientName")
        release_signed = request.get("release_signed")
        assignment_of_benefits_signature_date = request.get("AssignmentofBenefitsSignatureDate")
        authorization_signature_patient_name = request.get("AuthorizationSignaturePatientName")
        payment_signed = request.get("payment_signed")
        authorization_signature_date = request.get("AuthorizationSignatureSignatureDate")

    # update clinical sample!
        portal = api.portal.get("samples")
        obj = api.content.create(
            type = 'ClinicalSample',
            title = usn,
            tests_ordered = insurance_name,
            sample_primary_insurance_name = insurance_name, # schema.TextLine,
            sample_primary_insurance_payerID = insurance_payer_id, # schema.TextLine,
            sample_primary_insurance_policy_number = insurance_policy_number, # schema.TextLine,
            sample_primary_insurance_plan_number = insurance_plan_number, # schema.TextLine,
            sample_primary_insurance_subscriber_name = insurance_subscriber_name, # schema.TextLine,
            sample_primary_insurance_relation_to_insured = relationship_to_insured, # schema.Choice,
            sample_primary_insurance_subscriber_DOB = secondary_insurance_subscriber_dob, # schema.Date,
            sample_primary_insurance_effective_date = effective_date, # schema.Date,
            sample_primary_insurance_address = insurance_address, # schema.TextLine,
            sample_primary_city = insurance_city, # schema.TextLine,
            sample_primary_state = insurance_state, # schema.TextLine,
            sample_primary_insurance_zip_code = insurance_zip_code, # schema.TextLine,
            sample_secondary_insurance_name = secondary_insurance_name, # schema.TextLine,
            sample_secondary_insurance_payerID = secondary_insurance_payer_id, # schema.TextLine,
            sample_secondary_insurance_policy_number = secondary_insurance_policy_number, # schema.TextLine,
            sample_secondary_insurance_plan_number = secondary_insurance_plan_number, # schema.TextLine,
            sample_secondary_insurance_authorization_precertificate = secondary_authorization_precertification, # schema.TextLine,
            sample_secondary_insurance_subscriber_name = secondary_insurance_subscriber_dob, # schema.TextLine,
            sample_secondary_insurance_relation_to_insured = secondary_relationship_to_insured, # schema.Choice,
            sample_secondary_insurance_subscriber_DOB = secondary_insurance_subscriber_dob, # schema.Datetime,
            sample_secondary_insurance_effective_date = secondary_effective_date, # schema.Datetime,
            sample_secondary_insurance_address = secondary_insurance_address, # schema.TextLine,
            sample_secondary_city = secondary_insurance_city, # schema.TextLine,
            sample_secondary_state = secondary_insurance_state, # schema.TextLine,
            sample_secondary_insurance_zip_code = secondary_insurance_zip_code, # schema.TextLine,
            assignment_of_benefits_patient_name = assignment_of_benefits_patient_name, # schema.TextLine
            release_signed = release_signed, # schema.Bool
            assignment_of_benefits_signature_date = assignment_of_benefits_signature_date, # schema.Date
            authorization_signature_patient_name = authorization_signature_patient_name, # schema.TextLine
            payment_signed = payment_signed, #schema.Bool
            authorization_signature_date = authorization_signature_date, #schema.Date
            )
