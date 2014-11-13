function validate_form(event){
	var firstname = $("input[name='firstname']").val();
	var sex = $("input[name='sex']:checked").val();	
	var random_num = $("input[name='random_num']").val();
	var secondname = $("input[name='secondname']").val();
	var weather = $("input[name='weather']:checked").val();
	var activity = $("#activity option:selected").val();
	var animal = $("input[name='animal']").val();
	var likes = $("input[type='checkbox']:checked").map(function() {
	    return " " + this.value;
	}).get();

	if (firstname == "" || sex == null || 
		random_num == "" || secondname == "" || 
		weather == null || activity == "" || 
		animal == "" || likes == "") {
		
		$("div#madlib-output").empty();
		$("div#madlib-output").append("Oops! You forgot to fill out all the fields in your story");

	} else {
		
		$("div#madlib-output").empty();
		$("div#madlib-output").append("<p>" + firstname + ", a " + 
			sex + " " + animal + ", walked to the store to meet " + 
			secondname +  ". " + firstname + " wanted to buy " + 
			random_num + " tacos on this " + weather + " day. " + 
			firstname + " and " + secondname + " were planning on " + 
			activity + " after they went to the store. Their other friend, another " + 
			animal + ", was planning on meeting up with them. They all enjoy " +
			likes + ".</p>"); 
	}

	event.preventDefault();
}

function main() {
	$("input:submit").click(validate_form);
}

$(document).ready(main);