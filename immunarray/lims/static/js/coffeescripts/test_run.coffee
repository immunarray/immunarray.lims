#Brain for SLE-key_v_2_0_commercial.pt
# something to test
require [ 'jquery' ], ($) ->
  $('#assay_selection').change ->
    assaySelected = $(this).val()
    authenticator = $('input[name="_authenticator"]').val()
    alert assaySelected
    $.ajax
      url: 'ctest'
      type: 'POST'
      data:
        'assaySeleced': assaySelected
        '_authenticator': authenticator
      success: (responseText, statusText, statusCode, xhr, $form) ->
        if statusCode.status == 210
          alert 'No Samples Require this Assay Choice!!!'
        testPlanData = JSON.parse(responseText)
        arrayOfPlates = testPlanData['TestRun']
        numberOfPlates = arrayOfPlates.length
        alert numberOfPlates
        #number of plates sent back from LIMS
        i = 0
        while i < numberOfPlates
          plateNumber = i + 1
          i++
        return
    return
  return
