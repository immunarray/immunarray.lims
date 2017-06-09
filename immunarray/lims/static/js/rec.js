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
                // split USN field into site and true usn
                var usnParts = $(usn).val().split("-");
                var site = usnParts[0];
                var uniqueSampleNumber = usnParts[1] + "-" + usnParts[2];
                // alert("site: " + site);
                // alert("Unique Sample Number: " + uniqueSampleNumber);
                // is usn unique?
                authenticator = $('input[name="_authenticator"]').val();
                // alert(authenticator);
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

        function alertUser() {
            alert("From BrowserView/Python feedback!")
        }
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
