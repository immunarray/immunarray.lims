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
                    success: function(responseText, statusText, xhr, $form){
                        if(responseText.success) {
                            window.location.href = responseText.url;
                        }
                    }
                });
            })
        });

    })
)
