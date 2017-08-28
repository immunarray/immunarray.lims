(function() {
  require(['jquery'], function($) {
    var go;
    go = function(ev) {
      var authenticator;
      authenticator = $('input[name="_authenticator"]').val();
      $.ajax({
        url: 'add-aliquots-feedback',
        type: 'POST',
        dataType: 'json',
        data: {
          'aliquot_type': $('.aliquot-type').val(),
          'aliquot_volume': $('.aliquot-volume').val(),
          'aliquot_count': $('.aliquot-count').val()
        },
        success: function(responseText, statusText, statusCode, xhr, $form) {
          $('.aliquot-count').val(responseText.aliquot_count);
          $('.feedback').empty().append(responseText.feedback);
          $('.feedback').show('fast');
        }
      });
    };
    $("input, select").on('change', function(ev) {
      go(ev);
    });
    $("input, select").on('keyup', function(ev) {
      go(ev);
    });
  });

}).call(this);
