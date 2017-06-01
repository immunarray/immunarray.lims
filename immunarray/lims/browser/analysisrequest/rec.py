from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from immunarray.lims.interfaces.clinicalsample import IClinicalSample
from plone.dexterity.utils import createContentInContainer
from plone import api
from bika.lims.permissions import disallow_default_contenttypes
from immunarray.lims.permissions import AddClinicalSample
from immunarray.lims.permissions import AddPatient
from plone.dexterity.utils import createContentInContainer
from Products.CMFPlone.resources import add_resource_on_request
import plone.protect
import json



class AddRecView(BrowserView):

    template = ViewPageTemplateFile("templates/accessioning/acc.pt")

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.errors = []

    def __call__(self):
        add_resource_on_request(self.request, "static.js.rec")
        request = self.request

        #if "submitted" in request:
            # submit button pushed
            # return self.template()

        if "usn_update" in request.form:
            authenticator = request.form.get('_authenticator')
            try:
                plone.protect.CheckAuthenticator(authenticator)
                #is this working?  the except is not kicking off
                # what does it do?
            except:
                import pdb;pdb.set_trace()
            usn = request.form.get('usn')
            site = request.form.get('site_id')
            # Do things
            self.check_unique_sample_id(usn)
            self.site_lookup(site)

        if "check_name_and_dob" in request.form:
            authenticator = request.form.get('_authenticator')
            try:
                plone.protect.CheckAuthenticator(authenticator)
                #is this working?  the except is not kicking off
                # what does it do?
            except:
                import pdb;pdb.set_trace()

        if "submitted" in request:
            import pdb;pdb.set_trace()
            # Do things
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
        patient_phone = request.get("patient_phone")

        # Consent
        consent_acquired = request.get("consent_acquired")
        consent_signed = request.get("consent_signed")
        consent_name = request.get("consent_name")
        consent_date = request.get("consent_date")

        # Tests
        # other_test_ordered = schema.List() need to make this into a list of data!
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
        return self.template()
        # import pdb;pdb.set_trace()
        # pop up to select assays that are active in system!
        # tests at the top
        # self.check_unique_sample_id(usn)
        # check if patient is unique
        # self.make_clinical_sample(usn)

        # clear rec form and reset for next sample entry
    def site_lookup(self, site_id):
        values = api.content.find(context=api.portal.get(), portal_type='Site')

    def check_unique_sample_id(self, usn):
        # Get all usn (titles) of ClinicalSamples in LIMS
        values = api.content.find(context=api.portal.get(), portal_type='ClinicalSample')
        usns = [v.Title for v in values]

        if usn in usns:
            # Want to git a feedback to tell end user ID is not unique!
            self.context.plone_utils.addPortalMessage("USN Not Unique!!!",'info')
            import pdb;pdb.set_trace()

    def repeat_order_check(self, pt_first, pt_last, pt_dob):
        # want t
        pass

    def make_clinical_sample(self, usn):
        # assign serial number for sample
        sn = api.content.find(context=api.portal.get(),
                              portal_type='ClinicalSample')
        all_sn = []
        #list of all serial numbers
        sn_uid = [s.UID for s in sn]
        for i in sn_uid:
            value = api.content.get(UID=i)
            all_sn.append(value.sample_serial_number)
        serial_number = max(all_sn) + 1
        import pdb;pdb.set_trace()

        # set permission for clinical sample
        cs = api.portal.get()
        sample = cs['lims']['samples']
        sample.manage_permission(
            AddClinicalSample, ['Manager', 'LabManager', 'LabClerk', 'Owner'], 0)
        disallow_default_contenttypes(sample)
        clinical_sample = api.content.create(container=sample,
                                             type='ClinicalSample',
                                             id=usn_from_form,
                                             safe_id=True,
                                             sample_serial_number=serial_number,
                                            )
        import pdb;pdb.set_trace()

    def make_patient(self, first, last, ssn, mrn, dob, gender, ethnicity,
                     ethnicity_other, marital_status, patient_address,
                     patient_city, patient_state, patient_zip_code,
                     patient_phone, usn, site_from_usn, usn_from_form,
                     consent_acquired):

        """determine if ethnicity or ethnicity_other is filled
         determine if patient has been tested before
         set permission for new patient
        """

        title = first + " " + last
        import pdb;pdb.set_trace()
        pt = api.portal.get()
        patient = pt['lims']['patients']
        patient.manage_permission(
            AddClinicalSample, ['Manager', 'LabManager', 'LabClerk', 'Owner'], 0)
        disallow_default_contenttypes(patient)
        clinical_sample = api.content.create(container=patient,
                                             type = 'Patient',
                                             id = first +" "+ last,
                                             safe_id = True,
                                             dob = dob,
                                             marital_status = marital_status,
                                             gender= gender,
                                             ssn = ssn,
                                             medical_record_number = mrn,
                                             research_consent = consent_acquired,
                                             ethnicity = ethnicity,
                                             ethnicity_other = ethnicity_other,
                                             tested_unique_sample_ids = usn_from_form,
                                             )
        import pdb;pdb.set_trace()


    """
    cut from __call__()


    # schema.TextLine

            tests_ordered = ,
            sample_primary_insurance_name = ,#schema.TextLine,
            sample_primary_insurance_payerID = ,#schema.TextLine,
            sample_primary_insurance_policy_number = , # schema.TextLine,
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

            phlebotomist_last_name = schema.TextLine,
            phlebotomist_signature_provided=schema.Bool,
            collection_date = schema.Date,
            received_date = schema.Date,

        # make patient record (if new patient, check first, last name, and
        # dob to see if it is a unique person)

        # check unique sample ID
        if not usn:
            self.errors.append(
                {"UniqueSampleNumber": "Sample number was not specified."})
        else:
            self.check_unique_sample_id(usn)

        if self.errors:
            # We must re-render the form, making sure to pass existing request
            # values formatted so that the form can consume them and provide
            # the alread-entered values to the user.
            import pdb;pdb.set_trace()
        else:
            # make clinical sample
            pass

"""
