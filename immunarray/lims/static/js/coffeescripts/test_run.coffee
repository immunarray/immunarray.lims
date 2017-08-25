#Brain for SLE-key_v_2_0_commercial.pt
require [ 'jquery'], ($) ->

  $('#assay_selection').change ->
    assaySelected = $(this).val()
    authenticator = $('input[name="_authenticator"]').val()
    $.ajax
      url: 'ctest'
      type: 'POST'
      dataType: 'json',
      data:
        'assaySeleced': assaySelected
        '_authenticator': authenticator
      success: (responseText, statusText, statusCode, xhr, $form) ->
        if statusCode.status == 210
          alert 'No Samples Require this Assay Choice!!!'
        $("div#plates").empty()
        $.each responseText['TestRun'], (plate_nr, v) ->
          # Clone and fix-up a new Plate table
          plate = $("#blank-plate").clone()[0]
          plate.id = '#plate-'+String(plate_nr+1)
          $(plate).find(".plate-title").empty().append('Plate '+String(plate_nr+1))
          $(plate).find(".ichip-id").addClass("plate-"+String(plate_nr+1))
          # Loop the incoming sample data and populate the table
          $.each v, (ichip_nr, vv) ->
            ichip_id = vv[0]
            samples = vv[1]
            $(plate).find(".ichip-id.plate-"+String(plate_nr+1)).val ichip_id
            $.each samples, (well_nr, sv) ->
              $(plate).find(".sampleid-aliquot.chip-"+String(ichip_nr+1)+".well-"+String(well_nr+1)).val sv
              return
            return
          # Insert new cloned plate to the HTML
          $("div#plates").append($(plate))
          $(plate).removeClass("hidden")
          return
        return
    return
  return
