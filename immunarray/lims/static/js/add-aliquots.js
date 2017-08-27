(function() {
  require(['jquery'], function($) {
    $("input, select").on('change', function(ev) {
      var authenticator;
      authenticator = $('input[name="_authenticator"]').val();
      $.ajax({
        url: 'add-aliquots',
        type: 'POST',
        dataType: 'json',
        data: {
          'form': $(this).parent('form').serializeArray(),
          '_authenticator': authenticator
        },
        success: function(responseText, statusText, statusCode, xhr, $form) {
          debugger;
        }
      });
    });
  });

}).call(this);
