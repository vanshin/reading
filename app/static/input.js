button = $('#submitreading')

function clearForm(){
	var reading = $("textarea#reading")
		order = $("input#order")
		rname = $("input#rname")
	reading.val("")
	order.val("")
	rname.val("")
}

$("#submitreading").click(function(){
	var reading = $("textarea#reading").val()
		order = $("input#order").val()
		rname = $("input#rname").val()
		// button = $('#submitreading')
		button.attr({"disabled":"disabled"})
	json_reading = {
		"reading_order": order,
		"reading_name": rname,
		"reading_body": reading
	}
	$.ajax({
		type: "POST",
		url: "/reading",
		data: JSON.stringify(json_reading),
		dataType: "json",
		contentType: "application/json"
	}).done(function(data){
		clearForm()
		button.removeAttr("disabled")
		
	})
})
