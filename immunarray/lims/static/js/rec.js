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
            var data = $(":input" ).serializeArray();
            data.authenticator = $('input[name="_authenticator"]').val();
            data.all_data = 1;
            $.ajax({
                url: 'rec',
                type: 'POST',
                data: data,
                success: function(responseText, statusText, xhr, $form){
                    fullSubmitFeedback = JSON.parse(responseText)
                    if (fullSubmitFeedback['feedback'] === "Missing Key Data Elements"){
                        alert("Missing Key Data Elements, Please update to include Unique Sample Number, First Name, Date of Birth, and Collection Date")
                    }
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
