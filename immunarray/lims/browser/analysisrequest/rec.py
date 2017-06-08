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
from Products.statusmessages.interfaces import IStatusMessage
import plone.protect
import json
import datetime



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
            # define request.form.get's
            usn = request.form.get('usn')
            site_id = request.form.get('site_id')
            # Do things
            self.check_unique_sample_id(usn)
            # Get Data Back
            site_name = self.site_lookup(site_id)
            docs_at_barcode_site = self.providers_at_site(site_id)
            #import pdb;pdb.set_trace()
            return json.dumps({"site_name":site_name, "docs_at_barcode_site":docs_at_barcode_site})
            #import pdb;pdb.set_trace()

        if "check_name_and_dob" in request.form:
            authenticator = request.form.get('_authenticator')
            try:
                plone.protect.CheckAuthenticator(authenticator)
            except:
                import pdb;pdb.set_trace()
            # define request.form.get's
            # import pdb;pdb.set_trace()
            pt_UID = "new_patient"
            dob_string = request.form.get('dob') # string value '%Y-%m-%d'
            patient_first_name = request.form.get('patient_first_name')
            patient_last_name = request.form.get('patient_last_name')
            pt_UID = self.repeat_order_check(dob_string, patient_first_name,patient_last_name, pt_UID)
            if pt_UID != "new_patient":
                previous_data = self.pull_previous_patient_data(pt_UID)
                # import pdb;pdb.set_trace()
                return json.dumps({"repeat order":"true", "Pt Data from LIMS":previous_data})
            import pdb;pdb.set_trace()
            # Do things
            # orders can be repeat with only first name or medical record number
            # and dob! Think of it as a de-identified sample


        #if "submitted" in request.form:
        #    import pdb;pdb.set_trace()
            # Do things
        # Patient Info
        # repeat_order = request.get("repeat_order")
        # Prevent user input on this
        # values comeing in via ajax
        # first = request.get("patient_first_name")
        # last = request.get("patient_last_name")

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
        #self.update_kit_count(site_id)
        return self.template()
        # import pdb;pdb.set_trace()
        # pop up to select assays that are active in system!
        # tests at the top
        # self.check_unique_sample_id(usn)
        # check if patient is unique
        # self.make_clinical_sample(usn)

        # clear rec form and reset for next sample entry

    def site_lookup(self, site_id):
        ''' Site ID to get practice names, and make list of provider NIP's at that
            practice
        '''
        site_objects = api.content.find(context=api.portal.get(), portal_type='Site')
        site_uids = [i.UID for i in site_objects]
        site_name= "null"
        for j in site_uids:
            site = api.content.get(UID=j)
            if site_id == str(site.title):
                site_name = site.site_name
        return site_name

    def providers_at_site(self, site_id):
        """Create list of providers based on the site ID from the rec input
        """
        provider_objects = api.content.find(context=api.portal.get(),
                                            portal_type='Provider')
        provider_uids = [v.UID for v in provider_objects]
        # build list of provider last name and npi's
        providers_at_site= []
        npis_at_site=[]
        for i in provider_uids:
            provider_object = api.content.get(UID=i)
            if int(site_id) == provider_object.site_ID:
                element = provider_object.last_name + "-"+ str(provider_object.npi)
                print "Found Provider : " + provider_object.last_name + "-" + str(provider_object.npi)
                element2 = str(provider_object.npi)
                npis_at_site.append(element2)
                providers_at_site.append(element)
        return providers_at_site

    def check_unique_sample_id(self, usn):
        """Check to see if USN is unique, alert use if not
        """
        values = api.content.find(context=api.portal.get(), portal_type='ClinicalSample')
        usns = [v.Title for v in values]
        if usn in usns:
            self.request.response.setHeader('Content-Type', "application/json")
            self.request.response.setStatus(207, "USN Non Unique")

    def repeat_order_check(self, dob_string, patient_first_name,
                           patient_last_name, pt_UID):
        """Check for repeat patient
        """
        values = api.content.find(context=api.portal.get(), portal_type='Patient')
        uids = [u.UID for u in values]
        current_pt_list = []
        for i in uids:
            record = api.content.get(UID=i)
            pt_first_name = record.first_name
            pt_last_name = record.last_name
            pt_dob2 = record.dob
            entry =[]
            entry.append(pt_first_name)
            entry.append(pt_last_name)
            entry.append(pt_dob2.strftime('%Y-%m-%d'))
            entry.append(i)
            current_pt_list.append(entry)
        for c in current_pt_list:
            if patient_first_name == c[0] and patient_last_name == c[1] and dob_string == c[2]:
                # patient is most likely a repeat order
                # set variable to be the UID (pt_UID = current_pt_list[3])
                # set variable that can be used to track repeat order ()
                pt_UID = c[3]
                # end the loop on FIRST pt that matches!
                print "Match: " + c[0] + ", " + c[1] + ", " + c[2] + ", " + pt_UID
                return pt_UID

                # return alert for repeat patient!
        return pt_UID

    def make_clinical_sample(self, usn):
        """Make a clinical sample via api, set serial number
        """
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
        #import pdb;pdb.set_trace()

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
        #import pdb;pdb.set_trace()

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
        # import pdb;pdb.set_trace()

    def update_kit_count(self, site_id):
        """Update site kits on hand count to be reduced by 1
        """
        site_objects = api.content.find(context=api.portal.get(), portal_type='Site')
        for i in site_objects:
            if i.Title == site_id:
                uid = i.UID
                site = api.content.get(UID=uid)
                site.kits_on_site -= 1
                # make alert if kits_on_site value is at or below desired level?

    def pull_previous_patient_data(self, pt_UID):
        """Take pt_UID and package up information to send back to end user
        """
        pt_record = api.content.get(UID=pt_UID)
        # fields in patient record
        data = {"first_name": pt_record.first_name,
        "last_name":pt_record.last_name,
        "dob":pt_record.dob.strftime('%Y-%m-%d'),
        "marital_status":pt_record.marital_status,
        "gender":pt_record.gender,
        "ssn":pt_record.ssn,
        "medical_record_number":pt_record.medical_record_number,
        "research_consent":pt_record.research_consent,
        "ethnicity":pt_record.ethnicity,
        "ethnicity_other":pt_record.ethnicity_other,
        "tested_unique_sample_ids":pt_record.tested_unique_sample_ids,
        "physical_address":pt_record.physical_address, # title=_("Physical address")
        "physical_address_cont":pt_record.physical_address_cont,
        "physical_address_city":pt_record.physical_address_city,
        "physical_address_state":pt_record.physical_address_state,
        "physical_address_zipcode":pt_record.physical_address_zipcode,
        "physical_address_country":pt_record.physical_address_country}
        # import pdb;pdb.set_trace()
        return data
