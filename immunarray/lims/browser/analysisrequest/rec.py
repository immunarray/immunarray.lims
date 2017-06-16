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
            usn_check = self.check_unique_sample_id(usn)
            site_name = self.site_lookup(site_id)
            docs_at_barcode_site = self.providers_at_site(site_id)
            if usn_check != "non unique usn":
                return json.dumps({"site_name":site_name, "docs_at_barcode_site":docs_at_barcode_site})

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
            else:
                return json.dumps({"repeat order": "false"})
            # Do things
            # orders can be repeat with only first name or medical record number
            # and dob! Think of it as a de-identified sample


        if "all_data" in request.form:
            authenticator = request.form.get('_authenticator')
            # import pdb;pdb.set_trace()
            try:
                plone.protect.CheckAuthenticator(authenticator)
            except:
                import pdb;pdb.set_trace()
            # Patient Data Elemetns
            usn_from_form = request.form.get('usn_from_from')
            site_id = request.form.get('site_id')
            dob = request.form.get('dob')
            first = request.form.get('patient_first_name')
            last = request.form.get('patient_last_name')
            mrn= request.form.get('mrn')
            ssn = request.form.get('ssn')
            gender = request.form.get('gender')
            marital_status = request.form.get('marital_status')
            ethnicity = request.form.get('ethnicity')
            ethnicity_other = request.form.get('ethnicity_specify')
            patient_address = request.form.get('p_add_street')
            patient_city = request.form.get('p_add_city')
            patient_state = request.form.get('p_state')
            patient_zip_code = request.form.get('p_add_zip')
            patient_phone = request.form.get('patient_phone')
            # Clinical Sample Data
            consent_acquired = request.form.get('consent_acquired')
            consent_signed = request.form.get('consent_signed')
            consent_date = request.form.get('consent_date')
            ana_testing = request.form.get('ana_testing')
            clinical_impression = request.form.get('clinical_impression')
            test_xray = request.form.get('test_xray')
            test_other = request.form.get('test_other')
            test_other_specify = request.form.get('test_other_specify')
            clin_rash = request.form.get('clin_rash')
            clin_seiz_psych = request.form.get('clin_seiz_psych')
            clin_mouth_sores = request.form.get('clin_mouth_sores')
            clin_hair_loss = request.form.get('clin_hair_loss')
            clin_joint_pain = request.form.get('clin_joint_pain')
            clin_inflam = request.form.get('clin_inflam')
            clin_other = request.form.get('clin_other')
            clin_other_specify = request.form.get('clin_other_specify')
            diagnosis_code = request.form.get('diagnosis_code')
            diag_other_specify = request.form.get('diag_other_specify')
            provider_nip_clean = request.form.get('provider_nip_clean')
            provider_signed = request.form.get('provider_signed')
            draw_location = request.form.get('draw_location')
            draw_tel = request.form.get('draw_tel')
            phlebotomist_name = request.form.get('phlebotomist_name')
            draw_signed = request.form.get('draw_signed')
            collection_date = request.form.get('collection_date')
            shipment_date = request.form.get('shipment_date')
            ordering_provider_name = request.form.get('ordering_provider_name')
            pt_UID = "new_patient"
            # import pdb;pdb.set_trace()
            # See if we have an existing pt
            pt_UID = self.repeat_order_check(dob, first, last, pt_UID)

            if pt_UID != "new_patient":
                print ("PT UID: " + pt_UID + " USN from Form : "+ usn_from_form)
                self.append_usn(usn_from_form, pt_UID)

            else:
                print "Make a new patient record"
                self.make_patient(first, last, ssn, mrn, dob, gender, ethnicity,
                                  ethnicity_other, marital_status, patient_address,
                                  patient_city, patient_state, patient_zip_code,
                                  patient_phone, usn_from_form)



            self.make_clinical_sample(usn_from_form, consent_acquired, ana_testing, clin_rash,
                                      clin_seiz_psych, clin_mouth_sores, clin_hair_loss, clin_joint_pain,
                                      clin_inflam, clin_other, clin_other_specify, diagnosis_code, diag_other_specify,
                                      provider_nip_clean, provider_signed, draw_location, draw_tel, phlebotomist_name,
                                      draw_signed, collection_date, shipment_date, test_other_specify,
                                      clinical_impression, ordering_provider_name, site_id)

            # import pdb;pdb.set_trace()
            return json.dumps({"feedback":"got it"})

        #self.update_kit_count(site_id)
        return self.template()
        # pop up to select assays that are active in system!
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
                element = provider_object.first_name + " " + provider_object.last_name + "-"+ str(provider_object.npi)
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
            return "non unique usn"

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
            #need to exclued any patients that have null values for fields
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

    def make_clinical_sample(self, usn_from_form, consent_acquired, ana_testing, clin_rash,
                             clin_seiz_psych, clin_mouth_sores, clin_hair_loss, clin_joint_pain,
                             clin_inflam, clin_other, clin_other_specify, diagnosis_code, diag_other_specify,
                             provider_nip_clean, provider_signed, draw_location, draw_tel, phlebotomist_name,
                             draw_signed, collection_date, shipment_date, test_other_specify,
                             clinical_impression, ordering_provider_name, site_id):
        """Make a clinical sample via api, set serial number
            Need to add option for assay choice at a later date
        """
        default_test_order = {u"SLEKEY-RO-V2-0-COMMERCIAL": u"Received"}
        default_sample_status = u"Received"
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

        symptoms_choice=[]
        if clin_rash != "": symptoms_choice.append(clin_rash)
        if clin_seiz_psych != "": symptoms_choice.append(clin_seiz_psych)
        if clin_mouth_sores != "": symptoms_choice.append(clin_mouth_sores)
        if clin_hair_loss != "": symptoms_choice.append(clin_hair_loss)
        if clin_joint_pain != "": symptoms_choice.append(clin_joint_pain)
        if clin_inflam != "": symptoms_choice.append(clin_inflam)
        if clin_other != "": symptoms_choice.append(clin_other)
        # datetime.datetime.strptime
        try:
            py_collection_date = datetime.datetime.strptime(collection_date, "%Y-%m-%d").date()
        except:
            py_collection_date = None
        try:
            py_shipment_date = datetime.datetime.strptime(shipment_date, "%Y-%m-%d").date()
        except:
            py_shipment_date = None
        # clin_other_specify

        # Get primary health care provider from site!
        site_objects = api.content.find(context=api.portal.get(), portal_type='Site')
        site_uids = [i.UID for i in site_objects]
        primary_provider= "null"
        for j in site_uids:
            site = api.content.get(UID=j)
            if site_id == str(site.title):
                primary_provider = site.primary_provider
        # import pdb;pdb.set_trace()
        # set permission for clinical sample
        cs = api.portal.get()
        sample = cs['lims']['samples']
        sample.manage_permission(
            AddClinicalSample, ['Manager', 'LabManager', 'LabClerk', 'Owner'], 0)
        disallow_default_contenttypes(sample)
        clinical_sample = api.content.create(container=sample,
                                             type='ClinicalSample',
                                             id=usn_from_form,
                                             title=usn_from_form,
                                             safe_id=True,
                                             sample_serial_number=serial_number,
                                             research_consent=consent_acquired,
                                             sample_status = default_sample_status,
                                             test_ordered_status =default_test_order,
                                             sample_ordering_healthcare_provider=ordering_provider_name,
                                             sample_ordering_healthcare_provider_signature=provider_signed,
                                             primary_healthcare_provider=primary_provider,
                                             ana_testing = ana_testing,
                                             clinical_impression=clinical_impression,
                                             other_test_ordered=test_other_specify,
                                             symptoms_choice=symptoms_choice,
                                             symptoms_text=clin_other_specify,
                                             diagnosis_code=diagnosis_code,
                                             diagnosis_code_other=diag_other_specify,
                                             phlebotomist_name=phlebotomist_name,
                                             phlebotomist_signature_provided=draw_signed,
                                             collection_date=py_collection_date,
                                             received_date=py_shipment_date,
                                            )
        print ("Clinical Sample Made with id of " + usn_from_form)
        # make aliquots for testing
        #import pdb;pdb.set_trace()

    def make_patient(self, first, last, ssn, mrn, dob, gender, ethnicity,
                     ethnicity_other, marital_status, patient_address,
                     patient_city, patient_state, patient_zip_code,
                     patient_phone, usn_from_form,
                     ):
        """determine if ethnicity or ethnicity_other is filled
         determine if patient has been tested before
         set permission for new patient
        """
        usn=[]
        usn.append(usn_from_form)
        pt_phone=[]
        pt_phone.append(patient_phone)
        #import pdb;pdb.set_trace()
        try:
            py_date = datetime.datetime.strptime(dob, "%Y-%m-%d").date()
        except:
            py_date = None
        title = first + " " + last
        #import pdb;pdb.set_trace()
        pt = api.portal.get()
        patient = pt['lims']['patients']
        patient.manage_permission(
            AddClinicalSample, ['Manager', 'LabManager', 'LabClerk', 'Owner'], 0)
        disallow_default_contenttypes(patient)
        clinical_sample = api.content.create(container=patient,
                                             type = 'Patient',
                                             title = title,
                                             first_name = first,
                                             last_name = last,
                                             safe_id = True,
                                             dob = py_date,
                                             marital_status = marital_status,
                                             gender= gender,
                                             ssn = ssn,
                                             medical_record_number = mrn,
                                             ethnicity = ethnicity,
                                             ethnicity_other = ethnicity_other,
                                             physical_address = patient_address,
                                             physical_address_city = patient_city,
                                             physical_address_state = patient_state,
                                             physical_address_zipcode = patient_zip_code,
                                             phone_numbers = pt_phone,
                                             tested_unique_sample_ids = usn,
                                             )
        # import pdb;pdb.set_trace()

    def append_usn(self, usn_from_form, pt_UID):
        """If patient exist this will be used to "update" pt object and append usn
           to object.
        """
        #
        pt_record = api.content.get(UID=pt_UID)
        pt_record.tested_unique_sample_ids.append(usn_from_form)
        pass
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

    def make_bulk_aliquots(self, usn_from_form):
        """Make aliquots based on USN
            2 bulk
            3 working
        """
        tubes_in_kit = 2
        # YY - USN - A01 vol = 1900 uL
        # YY - USN - B01 vol = 2000 uL
