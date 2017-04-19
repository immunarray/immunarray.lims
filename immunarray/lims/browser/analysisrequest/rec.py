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

        # ID
        usn = request.get("usn")

        # Patient Info
        repeat_order = request.get("repeat_order")
        first = request.get("patient_first_name")
        last = request.get("patient_last_name")
        ssn = request.get("ssn")
        mrn = request.get("mrn")
        dob = request.get("dob")
        gender = request.get("gender")
        ethnicity = request.get("ethnicity")
        ethnicity_other = request.get("ethnicity_specify")
        marital_status = request.get("marital_status")
        patient_address = request.get("p_add_street")
        patient_city = request.get("p_add_city")
        patient_state = request.get("p_add_state")
        patient_zip_code = request.get("p_add_zip")
        patient_phone = request.get("phone_number")

        # Consent
        consent_acquired = request.get("consent_acquired")
        consent_signed = request.get("consent_signed")
        consent_name = request.get("consent_name")
        consent_date = request.get("consent_date")

        # Tests
        ana_testing = request.get("ana_testing")
        test_xray = request.get("test-xray")
        test_other = request.get("test-other")
        test_other_specify = request.get("test-other-specify")

        # Clinical info
        clins = {}
        for key in request.keys():
            if key.startswith("clin-"):
                code = key.split("clin-")[-1]
                clins[code] = request[key]

        # Diagnosis
        diags = {}
        for key in request.keys():
            if key.startswith("diag-"):
                code = key.split("diag-")[-1]
                diags[code] = request[key]

        # Should exist in the system before the sample arrives
        # make practice_name and npi lookup from existing providers (dropdowns)
        provider = {
            "practice_name": request.get("practice_name"),
            "npi": request.get("npi"),
            "provider_printed_name": request.get("provider_printed_name"),
            "signed": request.get("signed"),
            "signed_date": request.get("signed_date")
        }

        specimen = {
            "draw_location": request.get("draw_location"),
            "draw_tel": request.get("draw_tel"),
            "draw_signed": request.get("draw_signed"),
            "collection_date": request.get("collection_date"),
            "shipment_date": request.get("shipment_date"),
        }

        import pdb;pdb.set_trace()

        # check unique sample ID
        if not usn:
            self.errors.append(
                {"UniqueSampleNumber": "Sample number was not specified."})
        else:
            self.check_unique_sample_id(usn)

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

        if self.errors:
            # We must re-render the form, making sure to pass existing request
            # values formatted so that the form can consume them and provide
            # the alread-entered values to the user.
            import pdb;pdb.set_trace()

    def check_unique_sample_id(self, usn):
        self.errors.append({"UniqueSampleNumber", "Sample number %s is not unique"%usn})
        return False
