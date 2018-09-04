var formValid = {mail_num: false, name: false};

function checkValidation() {
	if (formValid.mail_num == true && formValid.name == true) {
		$('#submitButton').removeAttr("disabled");
	} else {
		$('#submitButton').attr("disabled");
	}
};

$('#mail_num').on('input', function() {
	var mail_num = $('this').val();

	function msg(content) {
		$('#mail_num_error').text(content).show();
	};

	function hide() {
		$('#mail_num_error').hide();
	};

	var num_exp = new RegExp('^[0-9]+$');
	var char_exp = new RegExp('^[a-z]+$');
	var arroba_exp = new RegExp('[@]$');

	num_test = num_exp.test(mail_num);
	char_test = char_exp.test(mail_num);

	var arroba_counter = 0;
	var dot_counter = 0;
	var num_counter = 0;
	var char_counter = 0;
	var non_valid_counter = 0;
	var char;

	

	

	if (num_test && mail_num.length() == 9) {		
		formValid.mail_num = true
	}

	else if (mail_num.length() < 5) {
		msg('Too short to be a valid mail or number');
	}

	else if (char_test) {
		msg('The mail should contain "@" and "." ');
	}

	else {
		for (char_ind in mail_num) {
		char = mail_num[char_ind];

		if (char == "@") {
			arroba_counter += 1;
		}

		else if (char == ".") {
			dot_counter += 1;
		}

		else if (num_exp.test(char)) {
			num_counter += 1;
		}

		else if (char_exp.test(char)) {
			char_counter += 1;
		} 

		else {
			non_valid_counter += 1;
		}

		if (arroba_counter > 1) {
		msg("The mail should contain only one '@' ");
		}

		else if (dot_counter > 1) {
			msg("The mail should contain only one '.' ");
		}

		else if (non_valid_counter >= 1) {
			msg("Only letters, '@' and '.' are permitted in mails");
		}

		else if (arroba_counter == 0 && dot_counter == 0 && !num_test) {
			msg("The number should contain only numbers");
		}

		else {
			formValid.mail_num == true;
		}






	}
	}



	

	checkValidation();




});

































var formValid = {mail_num_valid: false, name_valid: false};

function checkValidation() {
  if (formValid.mail_num_valid == true && formValid.name_valid == true) {
    $('#submitButton').removeAttr("disabled");
  } else {
    $('#submitButton').attr("disabled");
  }
};

$('#{{ form.mail_or_num.id_for_label }}').on('input', function() {
  var mail_num = $('this').val();
  alert(mail_num)

  function msg(content) {
    $('#mail_num_error').text(content).show();
  };

  function hide() {
    $('#mail_num_error').hide();
  };

  var num_exp = new RegExp('^[0-9]+$');
  var char_exp = new RegExp('^[a-z]+$');
  var arroba_exp = new RegExp('[@]$');

  num_test = num_exp.test(mail_num);
  char_test = char_exp.test(mail_num);

  var arroba_counter = 0;
  var dot_counter = 0;
  var num_counter = 0;
  var char_counter = 0;
  var non_valid_counter = 0;
  var char;

  

  

  if (num_test && mail_num.length() == 9) {   
    formValid.mail_num_valid = true
  }

  else if (mail_num.length() < 5) {
    msg('Too short to be a valid mail or number');
  }

  else if (char_test) {
    msg('The mail should contain "@" and "." ');
  }

  else {
    for (char_ind in mail_num) {
    char = mail_num[char_ind];

    if (char == "@") {
      arroba_counter += 1;
    }

    else if (char == ".") {
      dot_counter += 1;
    }

    else if (num_exp.test(char)) {
      num_counter += 1;
    }

    else if (char_exp.test(char)) {
      char_counter += 1;
    } 

    else {
      non_valid_counter += 1;
    }

    if (arroba_counter > 1) {
    msg("The mail should contain only one '@' ");
    }

    else if (dot_counter > 1) {
      msg("The mail should contain only one '.' ");
    }

    else if (non_valid_counter >= 1) {
      msg("Only letters, '@' and '.' are permitted in mails");
    }

    else if (arroba_counter == 0 && dot_counter == 0 && !num_test) {
      msg("The number should contain only numbers");
    }

    else {
      formValid.mail_num_valid == true;
    }






  }
  }



  

  checkValidation();




});