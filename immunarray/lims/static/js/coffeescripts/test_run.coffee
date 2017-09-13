require ['jquery'], ($) ->

    authenticator = $('input[name="_authenticator"]').val()
    $('#assay_selection').change ->
        assay_name = $(this).val()
        $.ajax
            url: 'ctest'
            type: 'POST'
            dataType: 'json'
            data:
                ctest_action: 'selected_an_assay'
                assay_name: assay_name
                _authenticator: authenticator
            success: (responseText, statusText, statusCode, xhr, $form) ->
                if !responseText.success
                    portalMessage responseText.message
                    return
                $("div#plates").empty()
                $.each responseText['TestRun'], (i, v) ->
                    plate_nr = String(i+1)
                    # Clone and fix-up a new Plate table
                    plate = $("#blank-plate").clone()[0]
                    plate.id = '#plate-'+plate_nr
                    $(plate).find(".plate-title").empty().append('Plate '+plate_nr)
                    $(plate).find(".chip-id").addClass("plate-"+plate_nr)
                    # Loop the incoming sample data and populate the table
                    $.each v, (ii, vv) ->
                        ichip_nr = String(ii+1)
                        ichip_id = vv[0]
                        samples = vv[1]
                        $(plate).find(".chip-id.ichip-"+ichip_nr+".plate-"+plate_nr).val ichip_id
                        $.each samples, (iii, vvv) ->
                            well_nr = String(iii+1)
                            $(plate).find(".chip-"+ichip_nr+".well-"+well_nr).val vvv
                            return
                        return
                    # Insert new cloned plate to the HTML
                    $("div#plates").append($(plate))
                    $(plate).removeClass("hidden")
                    return
                # Deleting a plate re-orders and sets titles of remaining plates
                $('button[class="delete-plate"]').on 'click', (ev) ->
                    ev.preventDefault()
                    $(this).closest(".plate-container").remove()
                    $.each $('.plate-container'), (i, plate) ->
                        plate_nr = String(i+1)
                        $(plate).id = "plate-"+plate_nr
                        $(plate).find(".plate-title").empty().append('Plate '+plate_nr)
                        return
                    return
                batches = responseText['solution_batches']
                $('tr.solution_batch').remove()
                $.each batches, (i, v) ->
                    html = '<tr class="solution_batch">'
                    html += '<td>' + v[0] + '</td>'
                    html += '<td>'
                    html += '<select name ="solution-' + v[0] + '">'
                    $.each v[1], (ii, bb) ->
                        html += '<option value="'+bb[0]+'">'+bb[1] + ' ('+ bb[2]+')</option>'
                        return
                    html += '</select>'
                    html += '</td>'
                    html += '</tr>'
                    $("table#assay_solutions").append(html)
                    return
                return
        return

    $("#saverun").click (ev) ->
        ev.preventDefault()
        $.ajax
            url: window.location.href
            type: 'POST'
            dataType: 'json'
            data:
                form_values: $("form#test_run").serializeArray()
                ctest_action: 'save_run'
                _authenticator: authenticator
            success: (responseText, statusText, statusCode, xhr, $form) ->
                if !responseText.success
                    portalMessage responseText.message
                    return
                if responseText.redirect_url
                    window.location.href = responseText.redirect_url
                return
        return

    $("#csv").click (ev) ->
        ev.preventDefault()
        window.location.href = "csv"
        return

    $("#xlsx").click (ev) ->
        ev.preventDefault()
        window.location.href = "xlsx"
        return

    $("#import_data").click (ev) ->
        ev.preventDefault()
        $.ajax
            url: window.location.href
            type: 'POST'
            dataType: 'json'
            data:
                ctest_action: 'import_data'
                _authenticator: authenticator
            success: (responseText, statusText, statusCode, xhr, $form) ->
                if !responseText.success
                    portalMessage responseText.message
                    return
                if responseText.redirect_url
                    window.location.href = responseText.redirect_url
                return
        return

    portalMessage = (message) ->
        $("#global_statusmessage").empty().append("<div class='portalMessage error'><strong>Error</strong>"+message+"</div>")
        return

    return
