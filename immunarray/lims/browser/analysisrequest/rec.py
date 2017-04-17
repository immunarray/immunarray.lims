from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class AddRecView(BrowserView):

    template = ViewPageTemplateFile("templates/accessioning/acc.pt")

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.errors = []

    def __call__(self):
        request = self.request

        if "submitted" not in request:
            return self.template()

        #
        usn = request.get("usn")
        #
        repeat_order = request.get("repeat_order")
        first = request.get("patient_first_name")
        last = request.get("patient_last_name")
        ssn = request.get("ssn")
        mrn = request.get("mrn")
        dob = request.get("dob")
        gender = request.get("gender")
        ethnicity = request.get("ethnicity")
        ethnicity_other = request.get("ethnicity_other")
        marital_status = request.get("marital_status")
        patient_address = request.get("add_street")
        patient_city = request.get("add_city")
        patient_state = request.get("add_state")
        patient_zip_code = request.get("add_zip")
        patient_phone = request.get("phone_number")
        #
        consent_acquired = request.get("consent_acquired")
        consent_signed = request.get("consent_signed")
        consent_name = request.get("consent_name")
        consent_date = request.get("consent_date")
        #
        ana_testing = request.get("ana_testing")
        #
        other_tests =


        import pdb;pdb.set_trace()

        # check unique sample ID
        if not usid:
            self.errors.append(
                {"UniqueSampleNumber": "Sample number was not specified."})
        else:
            self.check_unique_sample_id(usid)

        # validate patient data (only a few fields are required)
        if not first:
            self.errors.append(
                {"PatientFirstName": "Patient First Name not specified."})
        if not last:
            self.errors.append(
                {"PatientLastName": "Patient Last Name not specified."})
        if not dob:
            self.errors.append(
                {"DOB": "Patient DOB not specified."})


# 'DateofCollection': '',
# 'DateofShipment': '',
# 'DrawLocation': '',
# 'DrawingLabPhoneNumber': '',
# 'HealthCareProviderPrintedName': '',
# 'LocationofInflmmation': '',
# 'NPI': '',
# 'OtherDiagnosisCode': '',
# 'OtherSymptoms': '',
# 'OtherTestsRun': '',
# 'PhlebotomistName': '',
# 'PracticeName': '',
# 'SignatureDate': '',

        if self.errors:
            raise up

    def check_unique_sample_id(self, usid):

        self.errors.append({"UniqueSampleNumber", "Sample number %s is not unique"%usid})
        return False

        return True
