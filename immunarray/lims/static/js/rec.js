/**
 * Brain for acc.pt
 */
require([
  'jquery'
],
    (function($) {
        $(function() {
            $('#usn').on("change", function() {
                // split USN field into site and true usn
                var usnParts = $(usn).val().split("-");
                var site = usnParts[0];
                var uniqueSampleNumber = usnParts[1] + "-" + usnParts[2];
                alert("site: " + site);
                alert("Unique Sample Number: " + uniqueSampleNumber);
                // is usn unique?
                authenticator = $('input[name="_authenticator"]').val();
                alert(authenticator);
                $ajax({
                    type: 'POST',
                    url: 'rec',
                    data: {
                        'submitted':1,
                        'entry': uniqueSampleNumber,
                        '_authenticator': authenticator},
                    success: function(responseText, statusText, xhr, $form){
                        if(responseText.success) {
                            window.location.href = responseText.url;
                        }
                    }
                });
            })
        });

        $('#patient_first_name').on("change", function(){
            // get patient first name on change of field
            var ptFirstName = $(patient_first_name).val();
            alert("Pt First Name: " + ptFirstName);
        });

        $('#patient_last_name').on("change", function(){
            //alert("PT last name was changed")
            var ptLastName= $(patient_last_name).val(); //YYYY-MM-DD
            alert("Pt Last Name: " + ptLastName);
        });

        $('#dob').on("focusout", function(){
            //alert("PT DOB was changed")
            var ptdob = $(dob).val();
            alert("Pt DOB: " + ptdob);
        });
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
    })
)
