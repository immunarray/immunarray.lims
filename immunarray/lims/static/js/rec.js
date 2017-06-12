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

                                        mrn = repeatPatientData["Pt Data from LIMS"]["medical_record_number"]
                                        document.getElementById('mrn').value = mrn;

                                        maritalStatus = repeatPatientData["Pt Data from LIMS"]["marital_status"]
                                        document.getElementById('ssn').value = maritalStatus;

                                        ssn = repeatPatientData["Pt Data from LIMS"]["ssn"]
                                        document.getElementById('ssn').value = ssn;

                                        researchConsent = repeatPatientData["Pt Data from LIMS"]["research_consent"]
                                        document.getElementById('practice_name').value = researchConsent;

                                        ethnicity = repeatPatientData["Pt Data from LIMS"]["ethnicity"]
                                        document.getElementById('practice_name').value = ethnicity;

                                        ethnicity_other = repeatPatientData["Pt Data from LIMS"]["ethnicity_other"]
                                        document.getElementById('practice_name').value = ethnicity_other;

                                        physicalAddress = repeatPatientData["Pt Data from LIMS"]["physical_address"]
                                        document.getElementById('practice_name').value = physicalAddress;

                                        physicalAddressCounty = repeatPatientData["Pt Data from LIMS"]["physical_address_country"]
                                        document.getElementById('practice_name').value = physicalAddressCounty;

                                        physicalAddressState = repeatPatientData["Pt Data from LIMS"]["physical_address_state"]
                                        document.getElementById('practice_name').value = physicalAddressState;

                                        physicalAddressZipCode = repeatPatientData["Pt Data from LIMS"]["physical_address_zipcode"]
                                        document.getElementById('practice_name').value = physicalAddressZipCode;
                                    }else{
                                        document.getElementById('repeat_order_no').checked = true;
                                        //document.getElementById('repeat_order_no').checked = true;
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
                            var site = usnParts[0];
                            var uniqueSampleNumber = usnParts[1] + "-" + usnParts[2];
                            var ptFirstName = $("input[id='patient_first_name']").val();
                            var ptLastName= $("input[id='patient_last_name']").val();
                            //alert("last name: " + ptLastName)
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
                            var diag = [];
                            var diag_D89_89 = $("input[id='diag-D89_89']:checked").val();
                            if (!!diag_D89_89){
                                diag.push(diag_D89_89);
                            }
                            var diag_M32_10 = $("input[id='diag-M32_10']:checked").val();
                            if (!!diag_M32_10){
                                diag.push(diag_M32_10);
                            }
                            var diag_D89_9 = $("input[id='diag-D89_9']:checked").val();
                            if(!!diag_D89_9){
                                diag.push(diag_D89_9);
                            }
                            var diag_M35_9 = $("input[id='diag-M35_9']:checked").val();
                            if(!!diag_M35_9){
                                diag.push(diag_M35_9);
                            }
                            var diag_L93_2 = $("input[id='diag-L93_2']:checked").val();
                            if (!!diag_L93_2){
                                diag.push(diag_L93_2);
                            }
                            // the other diag value can be anything!
                            var diag_other = $("input[id='diag-other']:checked").val();
                            if (!!diag_other){
                                diag.push(diag_other);
                            }
                            var diag_other_specify = $("input[id='diag-other-specify']").val();

                            // do not need practice_name
                            //var practice_name = $("input[id='practice_name']").val();
                            // clean up provider npi to only been the needed value
                            var provider_npis_raw = $("#provider_npis").val().split("-");
                            var provider_nip_clean = provider_npis_raw[1];

                            var provider_signed = $("input[id='provider_signed']:checked").val(); //name
                            var signed_date = $("input[id='signed_date']").val();
                            var draw_location = $("input[id='draw_location']").val();
                            var draw_tel = $("input[id='draw_tel']").val();
                            var phlebotomist_name = $("input[id='phlebotomist_name']").val();
                            var draw_signed = $("input[id='draw_signed']:checked").val(); //name
                            var collection_date = $("input[id='collection_date']").val(); //name

                            authenticator = $('input[name="_authenticator"]').val();
                            var url = window.location.href;
                            $.ajax({
                                url: 'rec',
                                type: 'POST',
                                data: {
                                    'all_data': 1,
                                    'usn_from_from':uniqueSampleNumber,
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
                                    'diagnosis_code':diag,
                                    'diag_other_specify':diag_other_specify,
                                    '_authenticator': authenticator},
                                success: function(responseText, statusText, xhr, $form){
                                }
                            });

            }

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
