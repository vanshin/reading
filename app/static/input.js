$("#submitreading").click(function(){
	var reading = $("textarea#reading").val()
		order = $("input#order").val()
		name = $("input#name").val()

	json_reading = {
		"reading_order": order,
		"reading_name": name,
		"reading_body": reading
	}
	$.ajax({
		type: "POST",
		url: "/reading",
		data: JSON.stringify(json_reading),
		dataType: "json",
		contentType: "application/json"
	}).done(function(data){
		
		console.log("post success")
	})
})
