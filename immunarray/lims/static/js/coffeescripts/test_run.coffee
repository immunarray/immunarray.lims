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
        $.each responseText['TestRun'], (i, v) ->
          plate_nr = String(i+1)
          # Clone and fix-up a new Plate table
          plate = $("#blank-plate").clone()[0]
          plate.id = '#plate-'+plate_nr
          $(plate).find(".plate-title").empty().append('Plate '+plate_nr)
          $(plate).find(".ichip-id").addClass("plate-"+plate_nr)
          # Loop the incoming sample data and populate the table
          $.each v, (ii, vv) ->
            ichip_nr = String(ii+1)
            ichip_id = vv[0]
            samples = vv[1]
            $(plate).find(".ichip-id.ichip-"+ichip_nr+".plate-"+plate_nr).val ichip_id
            $.each samples, (iii, vvv) ->
              well_nr = String(iii+1)
              $(plate).find(".chip-"+ichip_nr+".well-"+well_nr).val vvv
              return
            return
          # Insert new cloned plate to the HTML
          $("div#plates").append($(plate))
          $(plate).removeClass("hidden")
          return
        return
    return
  return
