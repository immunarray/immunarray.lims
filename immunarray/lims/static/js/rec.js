
/**
 * Brain for acc.pt
 */

(function() {
  require(['jquery'], function($) {
    var checkNameAndDOB, sendAllDataToLims, ssn_validate;
    checkNameAndDOB = function() {
      var authenticator, ptFirstName, ptLastName, ptdob, url;
      ptFirstName = $(patient_first_name).val();
      ptLastName = $(patient_last_name).val();
      ptdob = $(dob).val();
      if (!!ptFirstName || !!ptLastName || !!ptdob) {
        authenticator = $('input[name="_authenticator"]').val();
        url = window.location.href;
        $.ajax({
          url: 'rec',
          type: 'POST',
          dataType: 'json',
          data: {
            'check_name_and_dob': 1,
            'dob': ptdob,
            'patient_first_name': ptFirstName,
            'patient_last_name': ptLastName,
            '_authenticator': authenticator
          },
          success: function(responseText, statusText, xhr, $form) {
            var ethnicity, ethnicity_other, gender, maritalStatus, mrn, physicalAddress, physicalAddressCity, physicalAddressState, physicalAddressZipCode, ssn;
            if (responseText['repeat order'] === 'true') {
              document.getElementById('repeat_order_yes').checked = true;
              if (responseText['Pt Data from LIMS']['medical_record_number'] !== 'null') {
                mrn = responseText['Pt Data from LIMS']['medical_record_number'];
                document.getElementById('mrn').value = mrn;
              }
              if (responseText['Pt Data from LIMS']['marital_status'] === 'Single') {
                maritalStatus = responseText['Pt Data from LIMS']['marital_status'];
                document.getElementById('marital_status_single').checked = true;
              }
              if (responseText['Pt Data from LIMS']['marital_status'] === 'Married') {
                maritalStatus = responseText['Pt Data from LIMS']['marital_status'];
                document.getElementById('marital_status_married').checked = true;
              }
              if (responseText['Pt Data from LIMS']['marital_status'] === 'Other') {
                maritalStatus = responseText['Pt Data from LIMS']['marital_status'];
                document.getElementById('marital_status_other').checked = true;
              }
              if (responseText['Pt Data from LIMS']['gender'] === 'Female') {
                gender = responseText['Pt Data from LIMS']['gender'];
                document.getElementById('gender_female').checked = true;
              }
              if (responseText['Pt Data from LIMS']['gender'] === 'Male') {
                gender = responseText['Pt Data from LIMS']['gender'];
                document.getElementById('gender_male').checked = true;
              }
              if (responseText['Pt Data from LIMS']['ssn'] !== 'null') {
                ssn = responseText['Pt Data from LIMS']['ssn'];
                document.getElementById('ssn').value = ssn;
              }
              if (responseText['Pt Data from LIMS']['ethnicity'] === 'African American or Black') {
                ethnicity = responseText['Pt Data from LIMS']['ethnicity'];
                document.getElementById('ethnicity_african_american').checked = true;
              }
              if (responseText['Pt Data from LIMS']['ethnicity'] === 'Asian, Indian, Middle Eastern') {
                ethnicity = responseText['Pt Data from LIMS']['ethnicity'];
                document.getElementById('ethnicity_asian_indian').checked = true;
              }
              if (responseText['Pt Data from LIMS']['ethnicity'] === 'Caucasian') {
                ethnicity = responseText['Pt Data from LIMS']['ethnicity'];
                document.getElementById('ethnicity_caucasian').checked = true;
              }
              if (responseText['Pt Data from LIMS']['ethnicity'] === 'Hispanic or Latino') {
                ethnicity = responseText['Pt Data from LIMS']['ethnicity'];
                document.getElementById('ethnicity_hispanic_or_latino').checked = true;
              }
              if (responseText['Pt Data from LIMS']['ethnicity'] === 'Other') {
                ethnicity = responseText['Pt Data from LIMS']['ethnicity'];
                document.getElementById('ethnicity_other').checked = true;
              }
              if (responseText['Pt Data from LIMS']['ethnicity_other'] !== 'null') {
                ethnicity_other = responseText['Pt Data from LIMS']['ethnicity_other'];
                document.getElementById('ethnicity_specify').value = ethnicity_other;
              }
              if (responseText['Pt Data from LIMS']['physical_address'] !== 'null') {
                physicalAddress = responseText['Pt Data from LIMS']['physical_address'];
                document.getElementById('p_add_street').value = physicalAddress;
              }
              if (responseText['Pt Data from LIMS']['physical_address_state'] !== 'null') {
                physicalAddressState = responseText['Pt Data from LIMS']['physical_address_state'];
                document.getElementById('p_add_state').value = physicalAddressState;
              }
              if (responseText['Pt Data from LIMS']['physical_address_state'] !== 'null') {
                physicalAddressCity = responseText['Pt Data from LIMS']['physical_address_city'];
                document.getElementById('p_add_city').value = physicalAddressCity;
              }
              if (responseText['Pt Data from LIMS']['physical_address_zipcode'] !== 'null') {
                physicalAddressZipCode = responseText['Pt Data from LIMS']['physical_address_zipcode'];
                document.getElementById('p_add_zip').value = physicalAddressZipCode;
              }
              if (responseText['Pt Data from LIMS']['pt_phone_number'] !== 'null') {
                physicalAddressZipCode = responseText['Pt Data from LIMS']['pt_phone_number'];
                document.getElementById('patient_phone').value = physicalAddressZipCode[0];
              }
            } else {
              document.getElementById('repeat_order_no').checked = true;
            }
          }
        });
      }
    };
    sendAllDataToLims = function() {
      var ana_testing, authenticator, billable_primary, billable_secondary, clin_hair_loss, clin_inflam, clin_inflam_specify, clin_joint_pain, clin_joint_pain_specify, clin_mouth_sores, clin_other, clin_other_specify, clin_rash, clin_seiz_psych, clinical_impression, collection_date, consent_acquired, consent_date, consent_signed, diag_D89_89, diag_D89_9, diag_L93_2, diag_M32_10, diag_M35_9, diag_other, diag_other_specify, draw_location, draw_signed, draw_tel, ethnicity, ethnicity_specify, gender, marital_status, mrn, ordering_provider_name, p_add_city, p_add_street, p_add_zip, p_state, patient_phone, phlebotomist_name, provider_nip_clean, provider_npis_raw, provider_signed, ptFirstName, ptLastName, ptdob, shipment_date, signed_date, siteId, ssn, test_other, test_other_specify, test_xray, testsOrdered, uniqueSampleNumber, usnParts;
      usnParts = $('input[id=\'usn\']').val().split('-');
      siteId = usnParts[0];
      uniqueSampleNumber = usnParts[1] + '-' + usnParts[2];
      ptFirstName = $('input[id=\'patient_first_name\']').val();
      ptLastName = $('input[id=\'patient_last_name\']').val();
      ptdob = $('input[id=\'dob\']').val();
      mrn = $('input[id=\'mrn\']').val();
      ssn = $('input[id=\'ssn\']').val();
      gender = $('input[name=\'gender\']:checked').val();
      ethnicity = $('input[name=\'ethnicity\']:checked').val();
      ethnicity_specify = $('input[name=\'ethnicity_specify\']').val();
      p_add_street = $('input[id=\'p_add_street\']').val();
      marital_status = $('input[name=\'marital_status\']:checked').val();
      p_add_city = $('input[id=\'p_add_city\']').val();
      p_state = $('#p_add_state option:selected').val();
      p_add_zip = $('input[id=\'p_add_zip\']').val();
      patient_phone = $('input[id=\'patient_phone\']').val();
      consent_acquired = $('input[name=\'consent_acquired\']:checked').val();
      consent_signed = $('input[name=\'consent_signed\']:checked').val();
      consent_date = $('input[id=\'consent_date\']').val();
      ana_testing = $('input[name=\'ana_testing\']:checked').val();
      clinical_impression = $('input[name=\'clinical_impression\']:checked').val();
      test_xray = $('input[id=\'test-xray\']:checked').val();
      test_other = $('input[id=\'test-other\']:checked').val();
      test_other_specify = $('input[id=\'test-other-specify\']').val();
      clin_rash = $('input[id=\'clin-rash\']:checked').val();
      clin_seiz_psych = $('input[id=\'clin-seiz-psych\']:checked').val();
      clin_mouth_sores = $('input[id=\'clin-mouth-sores\']:checked').val();
      clin_hair_loss = $('input[id=\'clin-hair-loss\']:checked').val();
      clin_joint_pain = $('input[id=\'clin-joint-pain\']:checked').val();
      clin_joint_pain_specify = $('input[id=\'clin-joint-pain-specify\']').val();
      clin_inflam = $('input[id=\'clin-inflam\']:checked').val();
      clin_inflam_specify = $('input[id=\'clin-inflam-specify\']').val();
      clin_other = $('input[id=\'clin-other\']:checked').val();
      clin_other_specify = $('input[id=\'clin-other-specify\']').val();
      diag_D89_89 = $('input[id=\'diag-D89_89\']:checked').val();
      diag_M32_10 = $('input[id=\'diag-M32_10\']:checked').val();
      diag_D89_9 = $('input[id=\'diag-D89_9\']:checked').val();
      diag_M35_9 = $('input[id=\'diag-M35_9\']:checked').val();
      diag_L93_2 = $('input[id=\'diag-L93_2\']:checked').val();
      diag_other = $('input[id=\'diag-other\']:checked').val();
      diag_other_specify = $('input[id=\'diag-other-specify\']').val().split(', ');
      provider_npis_raw = $('#provider_npis').val().split('-');
      ordering_provider_name = provider_npis_raw[0];
      provider_nip_clean = provider_npis_raw[1];
      provider_signed = $('input[name=\'provider_signed\']:checked').val();
      signed_date = $('input[id=\'signed_date\']').val();
      draw_location = $('input[id=\'draw_location\']').val();
      draw_tel = $('input[id=\'draw_tel\']').val();
      phlebotomist_name = $('input[id=\'phlebotomist_name\']').val();
      draw_signed = $('input[name=\'draw_signed\']:checked').val();
      collection_date = $('input[name=\'collection_date\']').val();
      shipment_date = $('input[name=\'shipment_date\']').val();
      billable_primary = $('input[id=\'billable_code\']').val();
      billable_secondary = $('input[id=\'billable_code_designation\']').val();
      testsOrdered = [];
      $('.test-choice').each(function(i) {
        if (this.checked) {
          testsOrdered.push($(this).val());
        }
      });
      authenticator = $('input[name="_authenticator"]').val();
      $.ajax({
        url: 'rec',
        type: 'POST',
        data: {
          'all_data': 1,
          'usn_from_from': uniqueSampleNumber,
          'site_id': siteId,
          'dob': ptdob,
          'patient_first_name': ptFirstName,
          'patient_last_name': ptLastName,
          'mrn': mrn,
          'ssn': ssn,
          'gender': gender,
          'marital_status': marital_status,
          'ethnicity': ethnicity,
          'ethnicity_specify': ethnicity_specify,
          'p_add_street': p_add_street,
          'p_add_city': p_add_city,
          'p_state': p_state,
          'p_add_zip': p_add_zip,
          'patient_phone': patient_phone,
          'consent_acquired': consent_acquired,
          'consent_signed': consent_signed,
          'consent_date': consent_date,
          'ana_testing': ana_testing,
          'clinical_impression': clinical_impression,
          'test_xray': test_xray,
          'test_other': test_other,
          'test_other_specify': test_other_specify,
          'clin_rash': clin_rash,
          'clin_seiz_psych': clin_seiz_psych,
          'clin_mouth_sores': clin_mouth_sores,
          'clin_hair_loss': clin_hair_loss,
          'clin_joint_pain': clin_joint_pain,
          'clin_inflam': clin_inflam,
          'clin_other': clin_other,
          'clin_other_specify': clin_other_specify,
          'diag_D89_89': diag_D89_89,
          'diag_M32_10': diag_M32_10,
          'diag_D89_9': diag_D89_9,
          'diag_M35_9': diag_M35_9,
          'diag_L93_2': diag_L93_2,
          'diag_other': diag_other,
          'diag_other_specify': diag_other_specify,
          'provider_nip_clean': provider_nip_clean,
          'provider_signed': provider_signed,
          'draw_location': draw_location,
          'draw_tel': draw_tel,
          'phlebotomist_name': phlebotomist_name,
          'draw_signed': draw_signed,
          'collection_date': collection_date,
          'shipment_date': shipment_date,
          'ordering_provider_name': ordering_provider_name,
          'billing_primary': billable_primary,
          'billing_secondary': billable_secondary,
          'assay_choice': testsOrdered,
          '_authenticator': authenticator
        },
        success: function(responseText, statusText, xhr, $form) {
          var fullSubmitFeedback;
          fullSubmitFeedback = JSON.parse(responseText);
          if (fullSubmitFeedback['feedback'] === 'Missing Key Data Elements') {
            alert('Missing Key Data Elements, Please update to include Unique Sample Number, First Name, Date of Birth, and Collection Date');
          }
          if (fullSubmitFeedback['feedback'] === 'Successful Sample') {
            alert('Sample Added to LIMS ' + uniqueSampleNumber);
            location.reload();
          }
        }
      });
    };
    ssn_validate = function() {
      var regExp1, regExp2, ssn;
      ssn = '#ssn';
      regExp1 = '^d{3}-d{2}-d{4}$';
      regExp2 = '^d{4}$';
      alert('SSN format can be either \'###-##-####\' or \'####\' Please Correct');
    };
    $(function() {
      document.getElementById('repeat_order_yes').disabled = true;
      document.getElementById('repeat_order_no').disabled = true;
      $('#usn').on('change', function() {
        var authenticator, site, uniqueSampleNumber, url, usnParts;
        usnParts = $(usn).val().split('-');
        site = usnParts[0];
        uniqueSampleNumber = usnParts[1] + '-' + usnParts[2];
        authenticator = $('input[name="_authenticator"]').val();
        url = window.location.href;
        $.ajax({
          url: 'rec',
          type: 'POST',
          data: {
            'usn_update': 1,
            'usn': uniqueSampleNumber,
            'site_id': site,
            '_authenticator': authenticator
          },
          success: function(responseText, statusText, statusCode, xhr, $form) {
            var a, currentNpiList, i, length, n, option, providersAtSite, salesRepKit, siteInfo, siteName;
            if (statusCode.status === 207) {
              alert('Non Unique Sample Number!!!');
            }
            siteInfo = JSON.parse(responseText);
            siteName = siteInfo['site_name'];
            document.getElementById('practice_name').value = siteName;
            providersAtSite = siteInfo['docs_at_barcode_site'];
            currentNpiList = document.getElementById('provider_npis');
            length = currentNpiList.options.length;
            i = 1;
            while (i < length) {
              currentNpiList.options[i] = null;
              i++;
            }
            for (n in providersAtSite) {
              n = n;
              option = document.createElement('option');
              a = providersAtSite[n];
              option.text = a;
              currentNpiList.append(option);
            }
            salesRepKit = siteInfo['sales_rep_kit'];
            if (salesRepKit === true) {
              alert('Kit Site is a Sales Rep, Please Update Site ID');
            }
          }
        });
      });
    });
    document.getElementById('fullSubmit').onclick = sendAllDataToLims;
    $('#dob').on('focusout', function() {
      var ptdob;
      ptdob = $(dob).val();
      checkNameAndDOB();
    });
    $('#ethnicity_specify').hide();
    $('#ethnicity_other').on('click', function() {
      $(this).next().slideToggle(400);
    });
    $('#test-other-specify').hide();
    $('#test-other').on('click', function() {
      $(this).next().slideToggle(400);
    });
    $('#clin-joint-pain-specify').hide();
    $('#clin-joint-pain').on('click', function() {
      $(this).next().slideToggle(400);
    });
    $('#clin-inflam-specify').hide();
    $('#clin-inflam').on('click', function() {
      $(this).next().slideToggle(400);
    });
    $('#clin-other-specify').hide();
    $('#clin-other').on('click', function() {
      $(this).next().slideToggle(400);
    });
    $('#diag-other-specify').hide();
    $('#diag-other').on('click', function() {
      $(this).next().slideToggle(400);
    });
    $(function() {});
  });

}).call(this);
