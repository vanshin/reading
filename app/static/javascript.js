

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
		grammar = $("p#grammar")
		comment = $("p#comment")
		translation = $("p#translation")
	phrase.empty()
	grammar.empty()
	comment.empty()
	translation.empty()
}

function clearForm(){
	$("input:text").val("")
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
		$.each(data,function(index,value){
			if(index=="reading_sentences"){
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
		grammar = $("p#grammar")
		comment = $("p#comment")
		translation = $("p#translation")
	$test.attr("sen_id",id)
	$test.text(txt)
	$.ajax({
		type: "GET",
		url: "/sentence/"+id+"/note",
		dataType: "json",
	}).done(function(data){
		clearShowing()
		clearForm()
		$.each(data,function(key,value){
			if(key=="phrase" && value != "" && value != null){
				phrase.text("短语："+value)
			}
			
			if(key=="grammar" && value != "" && value != null){
				grammar.text("语法："+value)
			}
			if(key=="comment" && value != "" && value != null){
				comment.text("评论："+value)
			}
			if(key=="translation" && value != "" && value != null){
				translation.text("翻译："+value)
			}
		})
	})
})

$("#submit").click(function(){
	var id = $("#sentence_test").attr("sen_id")
		phrase = $("input#phrase").val()
		grammar = $("input#grammar").val()
		comment = $("input#comment").val()
		translation = $("input#translation").val()
		pphrase = $("p#phrase")
		pgrammar = $("p#grammar")
		pcomment = $("p#comment")
		ptranslation = $("p#translation")
	json_note = {
		
		"phrase": phrase,
		"grammar": grammar,
		"comment": comment,
		"translation": translation
	}
	$.ajax({
		type: "PUT",
		url: "/sentences/"+id+"/note",
		data: JSON.stringify(json_note),
		dataType: "json",
		contentType: "application/json"
	}).done(function(data){
		clearShowing()
		$.each(data,function(key,value){
			if(key=="phrase" && value != "" && value != null){
				pphrase.text("短语："+value)
			}
			if(key=="grammar" && value != "" && value != null){
				pgrammar.text("语法："+value)
			}
			if(key=="comment" && value != "" && value != null){
				pcomment.text("评论："+value)
			}
			if(key=="translation" && value != "" && value != null){
				ptranslation.text("翻译："+value)
			}
			

		})
		clearForm()
	})
})



$("#li-regi").click(function(){
    location.pathname = "/session/new"
})


