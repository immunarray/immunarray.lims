(function() {
  require(['jquery'], function($) {
    $('#assay_selection').change(function() {
      var assaySelected, authenticator;
      assaySelected = $(this).val();
      authenticator = $('input[name="_authenticator"]').val();
      $.ajax({
        url: 'ctest',
        type: 'POST',
        dataType: 'json',
        data: {
          'assaySeleced': assaySelected,
          '_authenticator': authenticator
        },
        success: function(responseText, statusText, statusCode, xhr, $form) {
          if (statusCode.status === 210) {
            alert('No Samples Require this Assay Choice!!!');
          }
          $("div#plates").empty();
          $.each(responseText['TestRun'], function(plate_nr, v) {
            var plate;
            plate = $("#blank-plate").clone()[0];
            plate.id = '#plate-' + String(plate_nr + 1);
            $(plate).find(".plate-title").empty().append('Plate ' + String(plate_nr + 1));
            $(plate).find(".ichip-id").addClass("plate-" + String(plate_nr + 1));
            $.each(v, function(ichip_nr, vv) {
              var ichip_id, samples;
              ichip_id = vv[0];
              samples = vv[1];
              $(plate).find(".ichip-id.plate-" + String(plate_nr + 1)).val(ichip_id);
              $.each(samples, function(well_nr, sv) {
                $(plate).find(".sampleid-aliquot.chip-" + String(ichip_nr + 1) + ".well-" + String(well_nr + 1)).val(sv);
              });
            });
            $("div#plates").append($(plate));
            $(plate).removeClass("hidden");
          });
        }
      });
    });
  });

}).call(this);
