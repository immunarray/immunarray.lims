from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


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
        usn = request.get("usn")
        # Primary Insurance
        insurance_name = request.get("InsuranceName")
        insurance_payer_id = request.get("InsurancePayerID")
        insurance_policy_number = request.get("InsurancePolicyNumber")
        insurance_group_number = request.get("InsuranceGroupNumber")
        insurance_plan_number = request.get("InsurancePlanNumber")
        authorization_precertification = request.get("AuthorizationPrecertification")
        insurance_subscriber_name = request.get("InsuranceSubscriberName")
<strong><p>Relationship to Insured&nbsp;&nbsp;<input type="checkbox">Self&nbsp;&nbsp;<input type="checkbox">Spouse&nbsp;&nbsp;<input type="checkbox">Child&nbsp;&nbsp;<input type="checkbox">Other&nbsp;&nbsp;</p></strong>
        insurance_subscriber_dob = request.get("InsuranceSubscriberDOB")
<strong><p>Insurance Subscriber Gender:&nbsp;&nbsp;<input type="checkbox">Female&nbsp;&nbsp;<input type="checkbox">Male</p></strong>
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
<strong><p>Relationship to Insured&nbsp;&nbsp;<input type="checkbox">Self&nbsp;&nbsp;<input type="checkbox">Spouse&nbsp;&nbsp;<input type="checkbox">Child&nbsp;&nbsp;<input type="checkbox">Other&nbsp;&nbsp;</p></strong>
        secondary_insurance_subscriber_dob = request.get("SecondaryInsuranceSubscriberDOB")
<strong><p>Insurance Subscriber Gender:&nbsp;&nbsp;<input type="checkbox">Female&nbsp;&nbsp;<input type="checkbox">Male</p></strong>
        secondary_number_of_days_authorized = request.get("SecondaryNumberofDaysAuthorized")
        secondary_effective_date = request.get("SecondaryEffectiveDate")
        secondary_insurance_address = request.get("SecondaryInsuranceAddress")
        secondary_insurance_city = request.get("SecondaryInsuranceCity")
        secondary_insurance_zip_code = request.get("SecondaryInsuranceZipCode")
        assignment_of_benefits_patient_name = request.get("AssignmentofBenefitsPatientName")
<p>Signed:&nbsp;<input type="checkbox">Yes&nbsp;&nbsp;<input type="checkbox">No</p>

        assignment_of_benefits_signature_date = request.get("AssignmentofBenefitsSignatureDate")
        authorization_signature_patient_name = request.get("AuthorizationSignaturePatientName")
<p>Signed:&nbsp;<input type="checkbox">Yes&nbsp;&nbsp;<input type="checkbox">No</p>
        authorization_signature_signature_date = request.get("AuthorizationSignatureSignatureDate")



