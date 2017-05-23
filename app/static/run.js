$(document).ready(function(){
	var order_ul = $('div#order_ul')
	var order_div = $('ul#order_div')
	var	li = document.createElement('li')
	$.ajax({
		type:'GET',
		url:'/current_user/id',
		dataType:'json'
	}).done(function(data){
		$.each(data, function(key, value){
			if (key=='id'){
				addul2(value)
			}
		})
	})
})

$('.ui.accordion')
  .accordion()
;


function addul3(id){
	var order_div = $('#order_div')
	var id = id
	var div = document.createElement('DIV')
	$.ajax({
		type: 'GET',
		url: '/user/'+id+'/list',
		dataType: 'json'
	}).done(function(data){
		$.each(data, function(key, value){
			if (key!='code' && key!= 'message'){
				var	ul = document.createElement('UL')
				ul.setAttribute("class", "list-group")
				var li_u = document.createElement('LI')
				li_u.setAttribute('class', 'list-group-item')
				li_u.innerHTML = key
				ul.appendChild(li_u)
				// ul.innerHTML = key
				for (index in value){
					li = document.createElement('LI')
					li.innerHTML = value[index]
					li.setAttribute('id', index)
					li.setAttribute('class', 'reading_list list-group-item')
					ul.appendChild(li)
				}
				div.appendChild(ul)
			}
			
		})
		order_div.append(div)
					
	})
}



function addul2(id){
	var order_div = $('#order_div')
	var id = id
	var div = document.createElement('DIV')
	$.ajax({
		type: 'GET',
		url: '/user/'+id+'/list',
		dataType: 'json'
	}).done(function(data){
		$.each(data, function(key, value){
			if (key!='code' && key!= 'message'){
				var title = key
				var content = []
				for (key in value){
					content.push(value[key])
				}
				div_item = get_item(title, value)
				order_div.append(div_item)
			}
		})				
	})
}


$("div").delegate(".reading_list", "click", function(e){
	var id = $(e.target).attr('id')
	var $reading = $("#reading")
	$.ajax({
		type:'GET',
		url:'/reading/'+id,
		dataType:'json'
	}).done(function(data){
		$reading.empty()
		var span = ""
		$.each(data,function(key, value){
			if(key=="reading_sentences"){
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
	
$("div").delegate("span.word_content", "click", function(e){
	var id = $(e.target).attr("word_id")
		Chinese = $("p#Chinese")
		Phonogram = $("p#Phonogram")
		wordshowing = $("p.word")
		txt = $(e.target).text()
		word = $("p.word")
	word.attr("word_id", id)
	wordshowing.text(txt)
	$.ajax({
		type: "GET",
		url: "/word/"+id+"/note",
		dataType: "json"
	}).done(function(data){
		clearWordShowing()
		clearForm()
		$.each(data, function(key, value){
			if (key=="code" && value==404){
				Chinese.text("中文： 未填写")
				Phonogram.text("音标： 未填写")
			} else{
				if (key=="Chinese" && value != "" && value != null){
					Chinese.text("中文：" + value)
				}
				if (key=="Phonogram" && value != "" && value != null){
					Phonogram.text("音标：" + value)
				}
			}
			
		})
	})
})

$("div").delegate("span.reading_content","click",function(e){
	var txt = $(e.target).text()
		id = $(e.target).attr("sen_id")
		sentence = $("p.sentence")
		phrase = $("p#phrase")
		grammar = $("p#grammar")
		comment = $("p#comment")
		translation = $("p#translation")

	sentence.attr("sen_id",id)
	$.ajax({
		type: "GET",
		url: "/sentence/"+id+"/note",
		dataType: "json",
	}).done(function(data){
		clearShowing()
		clearForm()
		$.each(data,function(key,value){
			if (key=='code' && value==404){
				phrase.text("短语： 未填写")
				grammar.text("语法： 未填写")
				comment.text("评论： 未填写")
				translation.text("翻译： 未填写")
			}else{
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
			}
			
		})
	})

	$.ajax({
		type: "GET",
		url: "/sentence/"+id,
		dataType: "json",
	}).done(function(data){
		sentence.empty()
		var span = ""
		$.each(data, function(key, value){
			if (key=="words"){
				for (x in value){
					span = span + '<span class="word_content" word_id="' + x +'" >' + value[x] + " " + "</span>";
				}
			}
		})
		sentence.prepend(span)
	})
})

$("#submitword").click(function(){
	var id = $("p.word").attr("word_id")
		Chinese = $("input#Chinese").val()
		Phonogram = $("input#Phonogram").val()
		

		pChinese = $("p#Chinese")
		pPhonogram = $("p#Phonogram")
	
	json_note = {
		"word_id": id,
		"Chinese": Chinese,
		"Phonogram": Phonogram,
	}
	$.ajax({
		type: "PUT",
		url: "/word/"+id+"/note",
		data: JSON.stringify(json_note),
		contentType: "application/json"
	}).done(function(data){
		clearWordShowing()
		$.each(data, function(key, value){
			if(key=="Chinese" && value != "" && value != null){
				pChinese.text("中文："+value)
			}
			if(key=="Phonogram" && value != "" && value != null){
				pPhonogram.text("音标："+value)
			}
		})
		clearWordForm()
	})
})

$("#submit").click(function(){
	var id = $("p.sentence").attr("sen_id")
		phrase = $("textarea#phrase").val()
		grammar = $("textarea#grammar").val()
		translation = $("textarea#translation").val()

		pphrase = $("p#phrase")
		pgrammar = $("p#grammar")
		ptranslation = $("p#translation")
	json_note = {
		"phrase": phrase,
		"grammar": grammar,
		"translation": translation
	}
	$.ajax({
		type: "PUT",
		url: "/sentence/"+id+"/note",
		data: JSON.stringify(json_note),
		dataType: "json",
		contentType: "application/json"
	}).done(function(data){
		clearShowing()
		$.each(data,function(key,value){
			if(key=="grammar" && value != "" && value != null){
				pgrammar.text("语法："+value)
			}
			if(key=="phrase" && value != "" && value != null){
				pphrase.text("短语："+value)
			}
			if(key=="translation" && value != "" && value != null){
				ptranslation.text("翻译："+value)
			}
		})
		clearForm()
	})
})
