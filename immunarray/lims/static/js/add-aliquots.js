(function() {
  require(['jquery'], function($) {
    var go;
    go = function(ev, allow_change_count) {
      var authenticator, base_url;
      authenticator = $('input[name="_authenticator"]').val();
      base_url = $('body').attr('data-base-url');
      $.ajax({
        url: base_url + '/add-aliquots-feedback',
        type: 'POST',
        dataType: 'json',
        data: {
          'aliquot_type': $('.aliquot-type').val(),
          'aliquot_volume': $('.aliquot-volume').val(),
          'aliquot_count': $('.aliquot-count').val()
        },
        success: function(responseText, statusText, statusCode, xhr, $form) {
          if (allow_change_count) {
            $('.aliquot-count').val(responseText.aliquot_count);
          }
          $('.feedback').empty().append(responseText.feedback);
          $('.feedback').show('fast');
        }
      });
    };
    $(".aliquot-type, .aliquot-volume").on('change', function(ev) {
      go(ev, true);
    });
    $(".aliquot-count").on('keyup', function(ev) {
      go(ev, false);
    });
  });

}).call(this);
