$(document).ready(function () {
			$(".post1").mouseup(getSentence);
			$(".sidebar").click(addul)
			// $(".order").click(showReading)
		});

function getSentence(){
	// var txt;
	// var parentOffset = $(this).offset();
	// var x = e.pageX - parentOffset.left;
	// var y = e.pageY - parentOffset.top;
	txt = window.getSelection();
	if (txt.toString().length > 1) {
		// txt = $("<p></p>").text(txt);
		$(".test").text(txt);
		
	}
			
}

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

function showReading(){
	$(document).click(function(e){
		var id = $(e.target).attr('id')
		console.log('请求id：'+id)
		var $reading = $("#reading")
		$.ajax({
			type:'GET',
			url:'/reading/'+id,
			dataType:'json'
		}).done(function(data){
			$.each(data,function(n,value){
				if(n=="reading_body"){
					p = "<p>" + value + "</p>";
					$reading.prepend(p)
				}
			})
	
		}).fail(function(jqXHR,textStatus){
			console.log("错误:"+textStatus)
		})
	
	})
	
	
	



	// $(".reading_id").each(function(){
	// 	var 
			
	// 		$test = $("#test")
	// 		$reading = $("#reading")
		

	// 	var id = $(this).attr("id");
	// 	console.log('请求id：'+id)
	// 	if(id){
	// 		$.ajax({
	// 			type:'GET',
	// 			url:'/reading/'+id,
	// 			dataType:'json'
	// 		}).done(function(data){
	// 			$.each(data,function(n,value){
	// 				if(n=="reading_body"){
	// 					p = "<p>" + value + "</p>";
	// 					$reading.prepend(p)
	// 				}
	// 			})
		
	// 		}).fail(function(jqXHR,textStatus){
	// 			console.log("错误:"+textStatus)
	// 		})
	// 	}
			

		
		
	// }
}

// var app = new Vue({
// 	el:'reading_id'
// })