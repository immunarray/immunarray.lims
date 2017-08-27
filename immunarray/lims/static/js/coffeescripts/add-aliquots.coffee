require ['jquery'], ($) ->
    $("input, select").on 'change', (ev) ->
        authenticator = $('input[name="_authenticator"]').val()
        $.ajax
            url: 'add-aliquots'
            type: 'POST'
            dataType: 'json',
            data:
                'form': $(this).parent('form').serializeArray()
                '_authenticator': authenticator
            success: (responseText, statusText, statusCode, xhr, $form) ->
                debugger
        return

    return
