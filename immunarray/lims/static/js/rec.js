require([
  'jquery'
],
  (function($) {
    $(function() {
      var $usn=$('.usn')
      var $ptFirstName =$('.patient_first_name')
      var $ptLastName =$('.patient_last_name')
      var $ptdob = $('.dob')

      $('#usn').on("change", function(){
        //alert("USN was changed")
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
})
})
)
