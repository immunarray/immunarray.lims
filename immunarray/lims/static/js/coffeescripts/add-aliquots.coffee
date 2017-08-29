require ['jquery'], ($) ->
    go = (ev, allow_change_count) ->
        authenticator = $('input[name="_authenticator"]').val()
        $.ajax
            url: window.location.href +'/add-aliquots-feedback'
            type: 'POST'
            dataType: 'json'
            data:
                'aliquot_type': $('.aliquot-type').val()
                'aliquot_volume': $('.aliquot-volume').val()
                'aliquot_count': $('.aliquot-count').val()
            success: (responseText, statusText, statusCode, xhr, $form) ->
                if allow_change_count
                    $('.aliquot-count').val responseText.aliquot_count
                $('.feedback').empty().append responseText.feedback
                $('.feedback').show('fast')
                return
        return
    $(".aliquot-type, .aliquot-volume").on 'change', (ev) ->
        go(ev, true)
        return
    $(".aliquot-count").on 'keyup', (ev) ->
        go(ev, false)
        return
    return
