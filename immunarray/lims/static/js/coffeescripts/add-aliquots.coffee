require ['jquery'], ($) ->
    go = (ev) ->
        authenticator = $('input[name="_authenticator"]').val()
        $.ajax
            url: 'add-aliquots-feedback'
            type: 'POST'
            dataType: 'json'
            data:
                'aliquot_type': $('.aliquot-type').val()
                'aliquot_volume': $('.aliquot-volume').val()
                'aliquot_count': $('.aliquot-count').val()
            success: (responseText, statusText, statusCode, xhr, $form) ->
                $('.aliquot-count').val responseText.aliquot_count
                $('.feedback').empty().append responseText.feedback
                $('.feedback').show('fast')
                return
        return
    $("input, select").on 'change', (ev) ->
        go(ev)
        return
    $("input, select").on 'keyup', (ev) ->
        go(ev)
        return
    return
