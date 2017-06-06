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
            # update kits on site
            import pdb;pdb.set_trace()

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
        # repeat_order = request.get("repeat_order")
        # Prevent user input on this
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
        ''' Site ID to get practice names, and make list of provider NIP's at that
            practice
        '''
        # git Site objects
        # import pdb;pdb.set_trace()
        site_objects = api.content.find(context=api.portal.get(), portal_type='Site')
        # import pdb;pdb.set_trace()
        # make a list of site_objects.Title
        # loop over site objects to find site_objects.title == site_id
        for i in site_objects:
            if i.Title == site_id:
                uid = i.UID
                site = api.content.get(UID=uid)
                site_name = site.name
                import pdb;pdb.set_trace()
                return site_name

        # get UID for object that site_objects.title = site_id
        # get "name" after opening that object!

        provider_objects = api.content.find(context=api.portal.get(), portal_type='Provider')
        provider_uids = [v.UID for v in provider_objects]
        # build list of provider last name and npi's
        providers_at_site= []
        for i in provider_uids:
            provider_object = api.content.get(UID=i)
            if site_id == provider_object.site_id:
                element = provider_object.last_name + "-"+provider_object.npi
                providers_at_site.append(element)
            return providers_at_site



    def check_unique_sample_id(self, usn):
        """Check to see if USN is unique, alert use if not
        """
        # Get all usn (titles) of ClinicalSamples in LIMS
        values = api.content.find(context=api.portal.get(), portal_type='ClinicalSample')
        usns = [v.Title for v in values]

        if usn in usns:
            # Want to git a feedback to tell end user ID is not unique!
            self.context.plone_utils.addPortalMessage(u"USN Not Unique!!!",'info')
            # import pdb;pdb.set_trace()

    def repeat_order_check(self, pt_first, pt_last, pt_dob):
        """Check for repeat patient
        """
        # need to format inputs to work for the search? date field is the most troubling one
        values = api.content.find(context=api.portal.get(), portal_type='Patient')
        # make list of uids
        uids = [u.UID for u in values]
        current_pt_list = []
        for i in uids:
            record = api.content.get(UID=i)
            pt_first_name = record.first_name
            pt_last_name = record.last_name
            pt_dob2 = record.dob
            # make entry
            current_pt_list.append(pt_first_name + "," + pt_last_name + "," +
                                   pt_dob2 + ","+ i)
        # for loop to look at two lists and pull the UID if needed
        for c in current_pt_list:
            if pt_first == current_pt_list[0] and pt_last == current_pt_list[1] and pt_dob == current_pt_list[2]:
                # patient is most likely a repeat order
                # set variable to be the UID (pt_UID = current_pt_list[3])
                # set variable that can be used to track repeat order ()
                pt_UID = current_pt_list[3]
                return pt_UID
            else:
                pt_UID = "new_patient"
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


    """
    cut from __call__()
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
