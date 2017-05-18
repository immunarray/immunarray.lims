require([
  'jquery'
],
  (function($) {
    $(function() {
      var $usn=$('.usn')
      var $ptFirstName =$('.patient_first_name')
      var $ptLastName =$('.patient_last_name')
      var $ptdob = $('.dob')
      // clean up raw input to seperate site id from 
      $('#usn').on("change", function(){
        //alert("USN was changed")
        var usnParts = $(usn).val().split("-");
        var site = usnParts[0];
        var uniqueSampleNumber = usnParts[1] + "-" + usnParts[2];
        alert("site: " + site);
        alert("Unique Sample Number: " + uniqueSampleNumber);
        //return uniqueSampleNumber, site;
      });

      $('#patient_first_name').on("change", function(){
        //alert("PT first name was changed")
      });

      $('#patient_last_name').on("change", function(){
         //alert("PT last name was changed")
      });

      $('#dob').on("change", function(){
         //alert("PT DOB was changed")
      });

      // Make form easier to use, hide all boxes that have click dependency
      $('#ethnicity_specify').hide();
      $('#ethnicity_other').on('click', function(){
        $(this).next().slideToggle(400);
      });

      $('#test-other-specify').hide();
      $('#test-other').on('click', function(){
        $(this).next().slideToggle(400);
      });

      $('#clin-joint-pain-specify').hide();
      $('#clin-joint-pain').on('click', function(){
        $(this).next().slideToggle(400);
      });

      $('#clin-inflam-specify').hide();
      $('#clin-inflam').on('click', function(){
              $(this).next().slideToggle(400);
            });

      $('#clin-other-specify').hide();
      $('#clin-other').on('click', function(){
        $(this).next().slideToggle(400);
      });

      $('#diag-other-specify').hide();
      $('#diag-other').on('click', function(){
        $(this).next().slideToggle(400);
      });
})
})
)
