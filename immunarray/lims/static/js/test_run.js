//Brain for SLE-key_v_2_0_commercial.pt
require(['jquery'],

(function($) {
    $('#assay_selection').change(function() {
        var assaySelected = $(this).val()
        authenticator = $('input[name="_authenticator"]').val();
        alert (assaySelected)
        $.ajax({
            url: 'ctest',
            type: 'POST',
            data: {
                'assaySeleced': assaySelected,
                '_authenticator': authenticator},
            success: function(responseText, statusText, statusCode, xhr, $form){
            if (statusCode.status === 210){
                alert("No Samples Require this Assay Choice!!!")
            }
            var testPlanData = JSON.parse(responseText);
            var arrayOfPlates = testPlanData["TestRun"];
            var numberOfPlates = arrayOfPlates.length
            alert (numberOfPlates); //number of plates sent back from LIMS
            for (i = 0; i < numberOfPlates; i++){
                var plateNumber = i +1;
            }
            }
        });

    })
}))
