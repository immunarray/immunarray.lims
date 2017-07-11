/**
 * Brain for acc.pt
 */
require([
  'jquery'
],
    (function($) {
        $(function() {
            document.getElementById('repeat_order_yes').disabled = true;
            document.getElementById('repeat_order_no').disabled = true;
            $('#usn').on("change", function() {
                var usnParts = $(usn).val().split("-");
                var site = usnParts[0];
                var uniqueSampleNumber = usnParts[1] + "-" + usnParts[2];
                authenticator = $('input[name="_authenticator"]').val();
                var url = window.location.href;
                $.ajax({
                    url: 'rec',
                    type: 'POST',
                    data: {
                        'usn_update': 1,
                        'usn': uniqueSampleNumber,
                        'site_id': site,
                        '_authenticator': authenticator},
                    success: function(responseText, statusText, statusCode, xhr, $form){
                        if (statusCode.status === 207){
                            alert("Non Unique Sample Number!!!")
                        }
                        var siteInfo = JSON.parse(responseText)
                        var siteName = siteInfo["site_name"]
                        document.getElementById('practice_name').value = siteName;
                        providersAtSite = siteInfo["docs_at_barcode_site"]
                        // clear list of previous values for n[1] and higher
                        var currentNpiList = document.getElementById('provider_npis');
                        var length = currentNpiList.options.length;
                        for (i=1; i < length; i++){
                            currentNpiList.options[i] = null;
                        }
                        for (n in providersAtSite) {
                            var option = document.createElement('option');
                            a = providersAtSite[n]
                            option.text= a;
                            currentNpiList.append(option);
                        }
                        var salesRepKit = siteInfo["sales_rep_kit"]
                        if (salesRepKit===true){
                            alert("Kit Site is a Sales Rep, Please Update Site ID")}
                        //alert (providersAtSite[0])
                    }
                });
            })
        });


        function checkNameAndDOB() {
                            var ptFirstName = $(patient_first_name).val();
                            var ptLastName= $(patient_last_name).val();
                            var ptdob = $(dob).val();
                            if ((!!ptFirstName) || (!!ptLastName) || (!!ptdob)){
                            authenticator = $('input[name="_authenticator"]').val();
                            var url = window.location.href;
                            $.ajax({
                                url: 'rec',
                                type: 'POST',
                                data: {
                                    'check_name_and_dob': 1,
                                    'dob': ptdob,
                                    'patient_first_name': ptFirstName,
                                    'patient_last_name': ptLastName,
                                    '_authenticator': authenticator},
                                success: function(responseText, statusText, xhr, $form){
                                    repeatPatientData = JSON.parse(responseText)
                                    if(repeatPatientData["repeat order"] === "true"){
                                        document.getElementById('repeat_order_yes').checked = true;

                                        if(repeatPatientData["Pt Data from LIMS"]["medical_record_number"]!='null')
                                        {
                                        mrn = repeatPatientData["Pt Data from LIMS"]["medical_record_number"]
                                        document.getElementById('mrn').value = mrn;
                                        }

                                        if(repeatPatientData["Pt Data from LIMS"]["marital_status"]==='Single')
                                        {
                                        maritalStatus = repeatPatientData["Pt Data from LIMS"]["marital_status"]
                                        document.getElementById('marital_status_single').checked = true;
                                        }

                                        if(repeatPatientData["Pt Data from LIMS"]["marital_status"]==='Married')
                                        {
                                        maritalStatus = repeatPatientData["Pt Data from LIMS"]["marital_status"]
                                        document.getElementById('marital_status_married').checked = true;
                                        }

                                        if(repeatPatientData["Pt Data from LIMS"]["marital_status"]==='Other')
                                        {
                                        maritalStatus = repeatPatientData["Pt Data from LIMS"]["marital_status"]
                                        document.getElementById('marital_status_other').checked = true;
                                        }

                                        if(repeatPatientData["Pt Data from LIMS"]["gender"]==="Female")
                                        {
                                        gender = repeatPatientData["Pt Data from LIMS"]["gender"]
                                        document.getElementById('gender_female').checked = true;
                                        }

                                        if(repeatPatientData["Pt Data from LIMS"]["gender"]==="Male")
                                        {
                                        gender = repeatPatientData["Pt Data from LIMS"]["gender"]
                                        document.getElementById('gender_male').checked = true;
                                        }

                                        if(repeatPatientData["Pt Data from LIMS"]["ssn"]!='null')
                                        {
                                        ssn = repeatPatientData["Pt Data from LIMS"]["ssn"]
                                        document.getElementById('ssn').value = ssn;
                                        }

                                        if(repeatPatientData["Pt Data from LIMS"]["ethnicity"]==='African American or Black'){
                                        ethnicity = repeatPatientData["Pt Data from LIMS"]["ethnicity"]
                                        document.getElementById('ethnicity_african_american').checked = true;}
                                        if(repeatPatientData["Pt Data from LIMS"]["ethnicity"]==='Asian, Indian, Middle Eastern'){
                                        ethnicity = repeatPatientData["Pt Data from LIMS"]["ethnicity"]
                                        document.getElementById('ethnicity_asian_indian').checked = true;}
                                        if(repeatPatientData["Pt Data from LIMS"]["ethnicity"]==='Caucasian'){
                                        ethnicity = repeatPatientData["Pt Data from LIMS"]["ethnicity"]
                                        document.getElementById('ethnicity_caucasian').checked = true;}
                                        if(repeatPatientData["Pt Data from LIMS"]["ethnicity"]==='Hispanic or Latino'){
                                        ethnicity = repeatPatientData["Pt Data from LIMS"]["ethnicity"]
                                        document.getElementById('ethnicity_hispanic_or_latino').checked = true;}
                                        if(repeatPatientData["Pt Data from LIMS"]["ethnicity"]==='Other'){
                                        ethnicity = repeatPatientData["Pt Data from LIMS"]["ethnicity"]
                                        document.getElementById('ethnicity_other').checked = true;}

                                        if(repeatPatientData["Pt Data from LIMS"]["ethnicity_other"]!='null')
                                        {
                                        ethnicity_other = repeatPatientData["Pt Data from LIMS"]["ethnicity_other"]
                                        document.getElementById('ethnicity_specify').value = ethnicity_other;
                                        }

                                        if(repeatPatientData["Pt Data from LIMS"]["physical_address"]!='null')
                                        {
                                        physicalAddress = repeatPatientData["Pt Data from LIMS"]["physical_address"]
                                        document.getElementById('p_add_street').value = physicalAddress;
                                        }

                                        //if(repeatPatientData["Pt Data from LIMS"]["physical_address_country"]!='null')
                                        //{
                                        //physicalAddressCounty = repeatPatientData["Pt Data from LIMS"]["physical_address_country"]
                                        //document.getElementById('p_add_country').value = physicalAddressCounty;
                                        //}

                                        if(repeatPatientData["Pt Data from LIMS"]["physical_address_state"]!='null')
                                        {
                                        physicalAddressState = repeatPatientData["Pt Data from LIMS"]["physical_address_state"]
                                        document.getElementById('p_add_state').value = physicalAddressState;
                                        }

                                        if(repeatPatientData["Pt Data from LIMS"]["physical_address_state"]!='null')
                                        {
                                        physicalAddressCity = repeatPatientData["Pt Data from LIMS"]["physical_address_city"]
                                        document.getElementById('p_add_city').value = physicalAddressCity;
                                        }

                                        if(repeatPatientData["Pt Data from LIMS"]["physical_address_zipcode"]!='null')
                                        {
                                        physicalAddressZipCode = repeatPatientData["Pt Data from LIMS"]["physical_address_zipcode"]
                                        document.getElementById('p_add_zip').value = physicalAddressZipCode;
                                        }
                                        if(repeatPatientData["Pt Data from LIMS"]["pt_phone_number"]!='null')
                                        {
                                        physicalAddressZipCode = repeatPatientData["Pt Data from LIMS"]["pt_phone_number"]
                                        document.getElementById('patient_phone').value = physicalAddressZipCode[0];
                                        }
                                    }else{
                                        document.getElementById('repeat_order_no').checked = true;
                                    }
                                        // set
                                        //document.getElementById()
                                    //if(responseText) {
                                    //    alert ("Patient is Repeat");
                                    //}
                                }
                            });
                        }
            }



        function sendAllDataToLims() {
                            //alert("sendAllDataToLims Started")
                            var usnParts = $("input[id='usn']").val().split("-");
                            var siteId = usnParts[0];
                            var uniqueSampleNumber = usnParts[1] + "-" + usnParts[2];
                            var ptFirstName = $("input[id='patient_first_name']").val();
                            var ptLastName= $("input[id='patient_last_name']").val();
                            var ptdob = $("input[id='dob']").val();
                            var mrn = $("input[id='mrn']").val();
                            var ssn = $("input[id='ssn']").val();
                            var gender = $("input[name='gender']:checked").val(); //name
                            var ethnicity = $("input[name='ethnicity']:checked").val(); //name
                            var ethnicity_specify = $("input[name='ethnicity_specify']").val(); //name
                            var p_add_street = $("input[id='p_add_street']").val();
                            var marital_status = $("input[name='marital_status']:checked").val(); //name
                            var p_add_city = $("input[id='p_add_city']").val();
                            var p_state = $("#p_add_state option:selected").val();
                            var p_add_zip = $("input[id='p_add_zip']").val();
                            var patient_phone = $("input[id='patient_phone']").val();
                            var consent_acquired = $("input[name='consent_acquired']:checked").val(); //name
                            var consent_signed = $("input[name='consent_signed']:checked").val(); //name
                            var consent_date = $("input[id='consent_date']").val();
                            var ana_testing = $("input[name='ana_testing']:checked").val(); //name
                            var clinical_impression = $("input[name='clinical_impression']:checked").val(); //name
                            var test_xray = $("input[id='test-xray']:checked").val();
                            var test_other = $("input[id='test-other']:checked").val();
                            var test_other_specify = $("input[id='test-other-specify']").val();
                            var clin_rash = $("input[id='clin-rash']:checked").val();
                            var clin_seiz_psych = $("input[id='clin-seiz-psych']:checked").val();
                            var clin_mouth_sores = $("input[id='clin-mouth-sores']:checked").val();
                            var clin_hair_loss = $("input[id='clin-hair-loss']:checked").val();
                            var clin_joint_pain = $("input[id='clin-joint-pain']:checked").val();
                            var clin_joint_pain_specify = $("input[id='clin-joint-pain-specify']").val();
                            var clin_inflam = $("input[id='clin-inflam']:checked").val();
                            var clin_inflam_specify = $("input[id='clin-inflam-specify']").val();
                            var clin_other = $("input[id='clin-other']:checked").val();
                            var clin_other_specify = $("input[id='clin-other-specify']").val();
                            // need to allow for all the entires to be entered but must match the LIMS Values...
                            var diag_D89_89 = $("input[id='diag-D89_89']:checked").val();
                            var diag_M32_10 = $("input[id='diag-M32_10']:checked").val();
                            var diag_D89_9 = $("input[id='diag-D89_9']:checked").val();
                            var diag_M35_9 = $("input[id='diag-M35_9']:checked").val();
                            var diag_L93_2 = $("input[id='diag-L93_2']:checked").val();
                            var diag_other = $("input[id='diag-other']:checked").val();
                            // the other diag value can be anything!
                            var diag_other_specify = $("input[id='diag-other-specify']").val().split(", ");
                            // do not need practice_name
                            //var practice_name = $("input[id='practice_name']").val();
                            // clean up provider npi to only been the needed value
                            var provider_npis_raw = $("#provider_npis").val().split("-");
                            var ordering_provider_name = provider_npis_raw[0];
                            var provider_nip_clean = provider_npis_raw[1];
                            var provider_signed = $("input[name='provider_signed']:checked").val(); //name
                            var signed_date = $("input[id='signed_date']").val();
                            var draw_location = $("input[id='draw_location']").val();
                            var draw_tel = $("input[id='draw_tel']").val();
                            var phlebotomist_name = $("input[id='phlebotomist_name']").val();
                            var draw_signed = $("input[name='draw_signed']:checked").val(); //name
                            var collection_date = $("input[name='collection_date']").val(); //name
                            var shipment_date = $("input[name='shipment_date']").val()
                            authenticator = $('input[name="_authenticator"]').val();
                            var url = window.location.href;
                            $.ajax({
                                url: 'rec',
                                type: 'POST',
                                data: {
                                    'all_data': 1,
                                    'usn_from_from':uniqueSampleNumber,
                                    'site_id':siteId,
                                    'dob':ptdob,
                                    'patient_first_name': ptFirstName,
                                    'patient_last_name': ptLastName,
                                    'mrn':mrn,
                                    'ssn':ssn,
                                    'gender':gender,
                                    'marital_status':marital_status,
                                    'ethnicity':ethnicity,
                                    'ethnicity_specify':ethnicity_specify,
                                    'p_add_street':p_add_street,
                                    'p_add_city':p_add_city,
                                    'p_state':p_state,
                                    'p_add_zip':p_add_zip,
                                    'patient_phone':patient_phone,
                                    'consent_acquired':consent_acquired,
                                    'consent_signed':consent_signed,
                                    'consent_date':consent_date,
                                    'ana_testing':ana_testing,
                                    'clinical_impression':clinical_impression,
                                    'test_xray':test_xray,
                                    'test_other':test_other,
                                    'test_other_specify':test_other_specify,
                                    'clin_rash':clin_rash,
                                    'clin_seiz_psych':clin_seiz_psych,
                                    'clin_mouth_sores':clin_mouth_sores,
                                    'clin_hair_loss':clin_hair_loss,
                                    'clin_joint_pain':clin_joint_pain,
                                    'clin_inflam':clin_inflam,
                                    'clin_other':clin_other,
                                    'clin_other_specify':clin_other_specify,
                                    'diag_D89_89':diag_D89_89,
                                    'diag_M32_10':diag_M32_10,
                                    'diag_D89_9':diag_D89_9,
                                    'diag_M35_9':diag_M35_9,
                                    'diag_L93_2':diag_L93_2,
                                    'diag_other':diag_other,
                                    'diag_other_specify':diag_other_specify,
                                    'provider_nip_clean':provider_nip_clean,
                                    'provider_signed':provider_signed,
                                    'draw_location':draw_location,
                                    'draw_tel':draw_tel,
                                    'phlebotomist_name':phlebotomist_name,
                                    'draw_signed':draw_signed,
                                    'collection_date':collection_date,
                                    'shipment_date':shipment_date,
                                    'ordering_provider_name':ordering_provider_name,
                                    '_authenticator': authenticator},
                                success: function(responseText, statusText, xhr, $form){
                                fullSubmitFeedback = JSON.parse(responseText)
                                if (fullSubmitFeedback['feedback'] === "Missing Key Data Elements"){alert("Missing Key Data Elements, Please update to include Unique Sample Number, First Name, Date of Birth, and Collection Date")}
                                if (fullSubmitFeedback['feedback'] === "Successful Sample"){
                                    alert("Sample Added to LIMS " + uniqueSampleNumber)
                                    location.reload()
                                }
                            }
            })}

        document.getElementById("fullSubmit").onclick = sendAllDataToLims;


        //$('#patient_first_name').on("change", function(){
            // get patient first name on change of field
        //    var ptFirstName = $(patient_first_name).val();
        //    alert("Pt First Name: " + ptFirstName);
        //    return ptFirstName;
        //    checkNameAndDOB(ptFirstName, ptLastName, ptdob);
        //});

        //$('#patient_last_name').on("change", function(){
        //    var ptLastName= $(patient_last_name).val(); //YYYY-MM-DD
        //    alert("Pt Last Name: " + ptLastName);
        //    return ptLastName;
        //    checkNameAndDOB(ptFirstName, ptLastName, ptdob);
        //});

        $('#dob').on("focusout", function(){
            var ptdob = $(dob).val();
            //alert("Pt DOB: " + ptdob);
            //return ptdob;
            checkNameAndDOB();
        });

        // SSN validate, allow for XXX-XX-XXXX or XXXX
        function ssn_validate(){
            var ssn = '#ssn';
            var regExp1 = "^\d{3}\-\d{2}\-\d{4}$";
            var regExp2 = "^\d{4}$";
            //logic to check input
            alert("SSN format can be either '###-##-####' or '####' Please Correct")
        }

        // is patient a repeat that first name, last name, and dob match existing
        // patient?
        // if yes load previous, and append usn to patient
        // if no allow user to continue to fill out form
        // load primary provider from site data
        // Make form easier to use, hide all boxes that have click dependency

        $('#ethnicity_specify').hide();
        $('#ethnicity_other').on('click', function(){
            $(this).next().slideToggle(400);
        });
        $('#test-other-specify').hide();
        $('#test-other').on('click', function(){
            $(this).next().slideToggle(400);
        });
        $('#clin-joint-pain-specify').hide();
        $('#clin-joint-pain').on('click', function(){
            $(this).next().slideToggle(400);
        });
        $('#clin-inflam-specify').hide();
        $('#clin-inflam').on('click', function(){
            $(this).next().slideToggle(400);
        });
        $('#clin-other-specify').hide();
        $('#clin-other').on('click', function(){
            $(this).next().slideToggle(400);
        });
        $('#diag-other-specify').hide();
        $('#diag-other').on('click', function(){
            $(this).next().slideToggle(400);
        });

        $(function usnNonUniquePopUp (){

        });
    })
)
