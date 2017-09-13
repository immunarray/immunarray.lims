(function() {
  require(['jquery'], function($) {
    var authenticator, portalMessage;
    authenticator = $('input[name="_authenticator"]').val();
    $('#assay_selection').change(function() {
      var assay_name;
      assay_name = $(this).val();
      $.ajax({
        url: 'ctest',
        type: 'POST',
        dataType: 'json',
        data: {
          ctest_action: 'selected_an_assay',
          assay_name: assay_name,
          _authenticator: authenticator
        },
        success: function(responseText, statusText, statusCode, xhr, $form) {
          var batches;
          if (!responseText.success) {
            portalMessage(responseText.message);
            return;
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
          batches = responseText['solution_batches'];
          $('tr.solution_batch').remove();
          $.each(batches, function(i, v) {
            var html;
            html = '<tr class="solution_batch">';
            html += '<td>' + v[0] + '</td>';
            html += '<td>';
            html += '<select name ="solution-' + v[0] + '">';
            $.each(v[1], function(ii, bb) {
              html += '<option value="' + bb[0] + '">' + bb[1] + ' (' + bb[2] + ')</option>';
            });
            html += '</select>';
            html += '</td>';
            html += '</tr>';
            $("table#assay_solutions").append(html);
          });
        }
      });
    });
    $("#saverun").click(function(ev) {
      ev.preventDefault();
      $.ajax({
        url: window.location.href,
        type: 'POST',
        dataType: 'json',
        data: {
          form_values: $("form#test_run").serializeArray(),
          ctest_action: 'save_run',
          _authenticator: authenticator
        },
        success: function(responseText, statusText, statusCode, xhr, $form) {
          if (!responseText.success) {
            portalMessage(responseText.message);
            return;
          }
          if (responseText.redirect_url) {
            window.location.href = responseText.redirect_url;
          }
        }
      });
    });
    $("#csv").click(function(ev) {
      ev.preventDefault();
      window.location.href = "csv";
    });
    $("#xlsx").click(function(ev) {
      ev.preventDefault();
      window.location.href = "xlsx";
    });
    $("#import_data").click(function(ev) {
      ev.preventDefault();
      $.ajax({
        url: window.location.href,
        type: 'POST',
        dataType: 'json',
        data: {
          ctest_action: 'import_data',
          _authenticator: authenticator
        },
        success: function(responseText, statusText, statusCode, xhr, $form) {
          if (!responseText.success) {
            portalMessage(responseText.message);
            return;
          }
          if (responseText.redirect_url) {
            window.location.href = responseText.redirect_url;
          }
        }
      });
    });
    portalMessage = function(message) {
      $("#global_statusmessage").empty().append("<div class='portalMessage error'><strong>Error</strong>" + message + "</div>");
    };
  });

}).call(this);
