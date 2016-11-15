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

function clearShowing(){
	var phrase = $("p#phrase")
		grammar_c = $("p#grammar_c")
		grammar_j = $("p#grammar_j")
		comment = $("p#comment")
		translation = $("p#translation")
	phrase.empty()
	grammar_c.empty()
	grammar_j.empty()
	comment.empty()
	translation.empty()
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
		id = $(e.target).attr("sen_id")
		$test = $("#sentence_test")
		phrase = $("p#phrase")
		grammar_c = $("p#grammar_c")
		grammar_j = $("p#grammar_j")
		comment = $("p#comment")
		translation = $("p#translation")
	$test.attr("sen_id",id)
	$test.text(txt)
	$.ajax({
		type: "GET",
		url: "/sentence/notes/"+id,
		dataType: "json",
	}).done(function(data){
		clearShowing()
		$.each(data,function(key,value){
			
			if(key=="phrase" && value != null){
				phrase.text("短语："+value)
			}
			if(key=="grammar_c" && value != null){
				grammar_c.text("词法："+value)
			}
			if(key=="grammar_j" && value != null){
				grammar_j.text("句法："+value)
			}
			if(key=="comment" && value != null){
				comment.text("评论："+value)
			}
			if(key=="translation" && value != null){
				translation.text("翻译："+value)
			}
		})
	})
})

$("#submit").click(function(){
	var id = $("#sentence_test").attr("sen_id")
		phrase = $("input#phrase").val()
		grammar_c = $("input#grammar_c").val()
		grammar_j = $("input#grammar_j").val()
		comment = $("input#comment").val()
		translation = $("input#translation").val()
		pphrase = $("p#phrase")
		pgrammar_c = $("p#grammar_c")
		pgrammar_j = $("p#grammar_j")
		pcomment = $("p#comment")
		ptranslation = $("p#translation")
	json_note = {
		
		"phrase": phrase,
		"grammar_c": grammar_c,
		"grammar_j": grammar_j,
		"comment": comment,
		"translation": translation
	}
	$.ajax({
		type: "PUT",
		url: "/sentence/notes/"+id,
		data: JSON.stringify(json_note),
		dataType: "json",
		contentType: "application/json"
	}).done(function(data){
		clearShowing()
		$.each(data,function(key,value){
			if(key=="phrase" && value != null ){
				pphrase.text("短语："+value)
			}
			if(key=="grammar_c" && value != null){
				pgrammar_c.text("词法："+value)
			}
			if(key=="grammar_j" && value != null){
				pgrammar_j.text("句法："+value)
			}
			if(key=="comment" && value != null){
				pcomment.text("评论："+value)
			}
			if(key=="translation" && value != null){
				ptranslation.text("翻译："+value)
			}

		})
	})
})
// $(document).on("cli(ck",".reading_content",function(){
// 	console.log("1")
// })
