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
						span = span + '<span class="reading_content">' + value[x] + ". " + "</span>";
					}					
				}
			})
			$reading.prepend(span)
	
		}).fail(function(jqXHR,textStatus){
			console.log("错误:"+textStatus)
		})
	
	})
	

$("div").delegate("span","click",function(e){
	console.log("span")
	
	var _id = $(e.target).attr('id')
	
	var $test = $("#sentence_test")
	var txt = $("[id='_id']").text()
	$test.text(txt)
})


// $(document).on("click",".reading_content",function(){
// 	console.log("1")
// })
