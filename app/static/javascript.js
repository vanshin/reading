// function getSentence(){
// 	// var txt;
// 	// var parentOffset = $(this).offset();
// 	// var x = e.pageX - parentOffset.left;
// 	// var y = e.pageY - parentOffset.top;
// 	var selectSentence = $("#selectSentence")
// 	txt = window.getSelection();
// 	if (txt.toString().length > 1) {
// 		// txt = $("<p></p>").text(txt);
// 		console.log(txt)
// 		$("p.test").text(txt);
		
// 	}

function addul(){
	if ((tmp = $("inputul").val()) == " ") {
		alert($("inputul").val())
	}else{
		var text = $("#inputul").val()
		var a = "<li><a href="+  +">"+ text +"</a></li>"
		var txt = "<li>" + text + "</li>"
		$("#addul").after(txt)
		$("#inputul").val(" ")
	}
	
}
$(".reading_list").click(function(e){
		var id = $(e.target).attr('id')
		var $reading = $("#reading")
		$.ajax({
			type:'GET',
			url:'/reading/'+id,
			dataType:'json'
		}).done(function(data){
			$reading.empty()
			var span = ""
			$.each(data,function(n,value){
				if(n=="reading_sentences"){
					for	(x in value){
						
						span = span + '<span class="reading_content" sen_id="' + x +'" >' + value[x] + ". " + "</span>";
					}					
				}
			})
			$reading.prepend(span)
	
		}).fail(function(jqXHR,textStatus){
			console.log("错误:"+textStatus)
		})
	
	})
	

$("div").delegate("span","click",function(e){
	
	
	var txt = $(e.target).text()
	var id = $(e.target).attr("sen_id")
	console.log("sen_id"+id)
	
	var $test = $("#sentence_test")
	$test.attr("sen_id",id)
	$test.text(txt)
})

$("#submit").click(function(){
	var id = $("#sentence_test").attr("sen_id")
	var phrase = $("#phrase").val()
	var grammar_c = $("#grammar_c").val()
	var grammar_j = $("#grammar_j").val()
	var comment = $("#comment").val()
	var translaiton = $("#translation").val()
	console.log(phrase)
	json_note = {
		
		"phrase": phrase,
		"grammar_c": grammar_c,
		"grammar_j": grammar_j,
		"comment": comment,
		"translaiton": translaiton
	}
	$.ajax({
		type: "PUT",
		url: "/sentence/notes/"+id,
		data: json_note,
		dataType: "json",
		contentType: "application/json"
	}).done(function(data){
		alert("1")
	})
})
// $(document).on("cli(ck",".reading_content",function(){
// 	console.log("1")
// })
