# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from immunarray.lims.interfaces.clinicalsample import IClinicalSample
from plone.dexterity.utils import createContentInContainer
from plone import api
from bika.lims.permissions import disallow_default_contenttypes
from immunarray.lims.permissions import AddClinicalSample
from immunarray.lims.permissions import AddClinicalAliquot
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
            # need to know if the site has free kits, requires siteID, and to get free_kits_left
            # need to pass billing status to make sample def, default will be billable_code will be "Billable"
            # with no billable_code_designation
            # need to alert user if the kit site is a sales person so the value
            # can be updated, sales person needs to add the kits to the site for this to work

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
            check_if_site_is_sales_rep = self.check_if_site_is_sales_rep(site_id)
            docs_at_barcode_site = self.providers_at_site(site_id)
            if check_if_site_is_sales_rep is True:
                return json.dumps({"site_name":site_name, "docs_at_barcode_site":docs_at_barcode_site, "sales_rep_kit":check_if_site_is_sales_rep})
            elif usn_check != "non unique usn":
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
            raw_test_other = request.form.get('test_other')
            test_other=[]
            test_other.append(raw_test_other)
            test_other_specify = request.form.get('test_other_specify')
            clin_rash = request.form.get('clin_rash')
            clin_seiz_psych = request.form.get('clin_seiz_psych')
            clin_mouth_sores = request.form.get('clin_mouth_sores')
            clin_hair_loss = request.form.get('clin_hair_loss')
            clin_joint_pain = request.form.get('clin_joint_pain')
            clin_inflam = request.form.get('clin_inflam')
            clin_other = request.form.get('clin_other')
            clin_other_specify = request.form.get('clin_other_specify')
            diag_D89_89 = request.form.get('diag_D89_89')
            diag_M32_10 = request.form.get('diag_M32_10')
            diag_D89_9 = request.form.get('diag_D89_9')
            diag_M35_9 = request.form.get('diag_M35_9')
            diag_L93_2 = request.form.get('diag_L93_2')
            diag_other = request.form.get('diag_other')
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
            # See if we have an existing pt
            missing_date_feedback =  json.dumps({"feedback":"Missing Key Data Elements"})
            # protection for making samples and new patient records, usn must be unique, first name not null, dob not null, collection date not null
            if usn_from_form == 'undefined-undefined':
                return missing_date_feedback
            elif first == '':
                return missing_date_feedback
            elif dob == '':
                return missing_date_feedback
            elif collection_date == '':
                return missing_date_feedback
            else:
                pt_UID = self.repeat_order_check(dob, first, last, pt_UID)
                if pt_UID != "new_patient":
                    print ("PT UID: " + pt_UID + " USN from Form : "+ usn_from_form)
                 # update existing record
                    self.update_existing_patient_data(pt_UID,dob, first, last, mrn, ssn, gender, marital_status, ethnicity, ethnicity_other,
                                                      patient_address, patient_city, patient_state, patient_zip_code, patient_phone)
                    self.append_usn(usn_from_form, pt_UID)
                else:
                    print "Make a new patient record"
                    self.make_patient(first, last, ssn, mrn, dob, gender, ethnicity,
                                      ethnicity_other, marital_status, patient_address,
                                      patient_city, patient_state, patient_zip_code,
                                      patient_phone, usn_from_form)
                sample_UID = self.make_clinical_sample(usn_from_form, consent_acquired, ana_testing, clin_rash,
                                          clin_seiz_psych, clin_mouth_sores, clin_hair_loss, clin_joint_pain,
                                          clin_inflam, clin_other, clin_other_specify, diag_D89_89, diag_M32_10, diag_D89_9,
                                          diag_M35_9, diag_L93_2, diag_other, diag_other_specify,
                                          provider_nip_clean, provider_signed, draw_location, draw_tel, phlebotomist_name,
                                          draw_signed, collection_date, shipment_date, test_other_specify,
                                          clinical_impression, ordering_provider_name, site_id)
                # make bulk aliquots
                # fancy way to have multiple tubes in the system, update letter list as more tubes are added
                # easy way
                draw_tubes = ['A','B']
                bulk_aliquotA = self.make_bulk_aliquots(sample_UID, usn_from_form, draw_tubes[0])
                print bulk_aliquotA
                bulk_aliquotB = self.make_bulk_aliquots(sample_UID, usn_from_form, draw_tubes[1])
                print  bulk_aliquotB
                # make working aliquots
                working_tubes = ['02','03','04']
                working_aliquotA02 = self.make_working_aliquots(usn_from_form, bulk_aliquotA, working_tubes[0])
                print working_aliquotA02
                working_aliquotA03 = self.make_working_aliquots(usn_from_form, bulk_aliquotA, working_tubes[1])
                print working_aliquotA03
                working_aliquotA04 = self.make_working_aliquots(usn_from_form, bulk_aliquotA, working_tubes[2])
                print working_aliquotA04
                #for t in tubes:
                #    exec ("bulk_aliquot" %t) = self.make_bulk_aliquots(sample_UID, usn_from_form, t)
                #    print"bulk_aliquot" % (t)
                # make working aliquots
                # import pdb;pdb.set_trace()
                try:
                    self.update_kit_count(site_id)
                except:
                    print "Kit Count for Site " + site_id + " Failed to Update"
                # add aliquots to box for storage!
                return json.dumps({"feedback":"Successful Sample"})
        return self.template()
        # pop up to select assays that are active in system!
        # clear rec form and reset for next sample entry, using javascript to do that on success!

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
            entry.append(datetime.datetime.strftime(pt_dob2, '%Y-%m-%d'))
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
                             clin_inflam, clin_other, clin_other_specify, diag_D89_89, diag_M32_10, diag_D89_9,
                             diag_M35_9, diag_L93_2, diag_other, diag_other_specify,
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

        if len(all_sn) == 0:serial_number = 10000
        else:serial_number = max(all_sn) + 1

        symptoms_choice=[]
        if clin_rash != None: symptoms_choice.append(unicode(clin_rash, "utf-8"))
        if clin_seiz_psych != None: symptoms_choice.append(unicode(clin_seiz_psych, "utf-8"))
        if clin_mouth_sores != None: symptoms_choice.append(unicode(clin_mouth_sores, "utf-8"))
        if clin_hair_loss != None: symptoms_choice.append(unicode(clin_hair_loss, "utf-8"))
        if clin_joint_pain != None: symptoms_choice.append(unicode(clin_joint_pain, "utf-8"))
        if clin_inflam != None: symptoms_choice.append(unicode(clin_inflam, "utf-8"))
        if clin_other != None: symptoms_choice.append(unicode(clin_other, "utf-8"))
        # datetime.datetime.strptime

        diagnosis_code=[]
        if diag_D89_89 != None: diagnosis_code.append(unicode(diag_D89_89, "utf-8"))
        if diag_M32_10 != None: diagnosis_code.append(unicode(diag_M32_10, "utf-8"))
        if diag_D89_9 != None: diagnosis_code.append(unicode(diag_D89_9, "utf-8"))
        if diag_M35_9 != None: diagnosis_code.append(unicode(diag_M35_9, "utf-8"))
        if diag_L93_2 != None: diagnosis_code.append(unicode(diag_L93_2, "utf-8"))
        if diag_other != None: diagnosis_code.append(unicode(diag_other, "utf-8"))

        try:
            py_collection_date = datetime.datetime.strptime(collection_date, "%Y-%m-%d").date()
        except:
            py_collection_date = None
        try:
            py_shipment_date = datetime.datetime.strptime(shipment_date, "%Y-%m-%d").date()
        except:
            py_shipment_date = None
        # need to split clin_other_specify on ', '
        # if clin_other_specify != "":

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
        clinical_sample_uid = clinical_sample.UID()
        return clinical_sample_uid
        # pass UID to be the start point for making aliquots
        # make aliquots for testing

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
        "physical_address_country":pt_record.physical_address_country,
        "pt_phone_number":pt_record.phone_numbers}
        # import pdb;pdb.set_trace()
        return data

    def update_existing_patient_data(self, pt_UID,dob, first, last, mrn, ssn, gender, marital_status, ethnicity, ethnicity_other,
    patient_address, patient_city, patient_state, patient_zip_code, patient_phone):
        """Update existing patient with the data that was entered by user
        """
        # fields in patient record, not able to update first, last, or dob by definition
        # not working as expected this redefines the form data to existing data
        # phone number update is not simple! need to think about best practice
        pt_record = api.content.get(UID=pt_UID)
        pt_record.medical_record_number = mrn
        pt_record.ssn = ssn
        pt_record.gender = gender
        pt_record.marital_status = marital_status
        pt_record.ethnicity = ethnicity
        pt_record.ethnicity_other = ethnicity_other
        pt_record.physical_address = patient_address
        pt_record.physical_address_city = patient_city
        pt_record.physical_address_state = patient_state
        pt_record.physical_address_zipcode = patient_zip_code
        print "Patient Record Updated UID: " + pt_UID

    def make_bulk_aliquots(self,sample_UID, usn_from_form, letter_to_add):
        """Make aliquot A based on USN and UID of the parent sample
        """
        today = datetime.datetime.today().date()
        target_clinical_sample = api.content.get(UID=sample_UID)
        clinical_aliquot = api.content.create(container=target_clinical_sample,
                                               type ='ClinicalAliquot',
                                               title =usn_from_form + "-"+letter_to_add+"01",
                                               sample_id = usn_from_form,
                                               aliquot_type = 'Bulk',
                                               volume = 2000,
                                               pour_date = today
                                              )
        print "Clinical Bulk Aliquot with ID of "+clinical_aliquot.title +"made"
        clinical_aliquot_UID = clinical_aliquot.UID()
        return clinical_aliquot_UID


    def make_working_aliquots(self, usn_from_form, bulk_aliquot_UID, tube_number):
        today = datetime.datetime.today().date()
        target_clinical_sample = api.content.get(UID=bulk_aliquot_UID)
        #adjust volume for child aliquot
        target_clinical_sample.volume -= 12
        clinical_aliquot = api.content.create(container=target_clinical_sample,
                                              type='ClinicalAliquot',
                                              title=usn_from_form + "-A" + tube_number,
                                              sample_id=target_clinical_sample.title,
                                              aliquot_type='Working',
                                              volume=12,
                                              pour_date=today
                                              )
        print "Clinical Working Aliquot with ID of " + clinical_aliquot.title + " made"
        clinical_aliquot_UID = clinical_aliquot.UID()
        return clinical_aliquot_UID

    def check_if_site_is_sales_rep(self,site_id):
        """See if kit came from a sales rep site
        """
        site_objects = api.content.find(context=api.portal.get(), portal_type='Site')
        site_uids = [i.UID for i in site_objects]
        site_is_sales_rep=False
        for j in site_uids:
            site = api.content.get(UID=j)
            if site_id == str(site.title):
                site_is_sales_rep=site.sales_rep
        return site_is_sales_rep
