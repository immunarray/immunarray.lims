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
          'ctest_action': 'selected_an_assay',
          'assaySelected': assaySelected,
          '_authenticator': authenticator
        },
        success: function(responseText, statusText, statusCode, xhr, $form) {
          if (statusCode.status === 210) {
            alert('No Samples Require this Assay Choice!!!');
          }
          $("div#plates").empty();
          $.each(responseText['TestRun'], function(i, v) {
            var plate, plate_nr;
            plate_nr = String(i + 1);
            plate = $("#blank-plate").clone()[0];
            plate.id = '#plate-' + plate_nr;
            $(plate).find(".plate-title").empty().append('Plate ' + plate_nr);
            $(plate).find(".chip-id").addClass("plate-" + plate_nr);
            $.each(v, function(ii, vv) {
              var ichip_id, ichip_nr, samples;
              ichip_nr = String(ii + 1);
              ichip_id = vv[0];
              samples = vv[1];
              $(plate).find(".chip-id.ichip-" + ichip_nr + ".plate-" + plate_nr).val(ichip_id);
              $.each(samples, function(iii, vvv) {
                var well_nr;
                well_nr = String(iii + 1);
                $(plate).find(".chip-" + ichip_nr + ".well-" + well_nr).val(vvv);
              });
            });
            $("div#plates").append($(plate));
            $(plate).removeClass("hidden");
          });
          $('button[class="delete-plate"]').on('click', function(ev) {
            ev.preventDefault();
            $(this).closest(".plate-container").remove();
            $.each($('.plate-container'), function(i, plate) {
              var plate_nr;
              plate_nr = String(i + 1);
              $(plate).id = "plate-" + plate_nr;
              $(plate).find(".plate-title").empty().append('Plate ' + plate_nr);
            });
          });
        }
      });
    });
    $("#saverun").click(function(ev) {
      var data;
      ev.preventDefault();
      data = {
        form_values: $("form#commercial_run").serializeArray(),
        ctest_action: 'save_run',
        assay_name: $('#assaySelected').val()
      };
      $.ajax({
        url: 'ctest',
        type: 'POST',
        dataType: 'json',
        data: data,
        success: function(responseText, statusText, statusCode, xhr, $form) {
          debugger;
        }
      });
    });
  });

}).call(this);
