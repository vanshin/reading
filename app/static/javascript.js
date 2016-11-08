$(document).ready(function () {
			$(".post1").mouseup(getSentence);
			$(".sidebar").click(addul)
			 
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
	$(".reading_id").each(function(){
		var $reading = $("#reading")
		var $id;
		var $test = $("#test")
		var $reading = $("#reading")
		$(this).click(function(){
			var $id = $(this).attr("id");

		})
		$.ajax({
			type:'GET',
			url:'/reading',
			data:{reading_id:$id},
			dataType:'json'

		}).done(function(data){
			$.each(data,function(n,value){
				var p = "";
				p = "<p>" + value.reaing_body + "</p>";
			})
			$reading.prepend(p)
		})
	});
}