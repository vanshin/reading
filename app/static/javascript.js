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
	$().click(function(){
		$.ajax({
			
			type:'GET',
			url:'/show',
			 data:{reading_name:},
		

		});
	});
}