require ['jquery'], ($) ->

    $('#assay_selection').change ->
        assaySelected = $(this).val()
        authenticator = $('input[name="_authenticator"]').val()
        $.ajax
            url: 'ctest'
            type: 'POST'
            dataType: 'json',
            data:
                'ctest_action': 'selected_an_assay'
                'assaySelected': assaySelected
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
                return
        return

    $("#saverun").click (ev) ->
        ev.preventDefault()
        data =
            form_values: $("form#commercial_run").serializeArray()
            ctest_action: 'save_run'
            assay_name: $('#assaySelected').val()
        $.ajax
            url: 'view'
            type: 'POST'
            dataType: 'json',
            data: data
            success: (responseText, statusText, statusCode, xhr, $form) ->
                debugger;
                return
        return

    portalMessage (message) ->
        $(".outer-wrapper>.container .row").prepend("<aside id='global_statusmessage'><div class='portalMessage error'><strong>Error</strong>"+message+" </div></aside>")
        return




    return
