$("#submitshare").click(function(){
	var user_id = $("input#user").val()
		r_id = $('input#reading').val()
	data = {
		"reading_id": r_id
	}
	$.ajax({
		type: 'POST',
		url: '/user/'+user_id+'/edit_list',
		data: JSON.stringify(data),
		dataType: "JSON",
		contentType: "application/json",
	}).done(function(data){
		if (data.code == 200) {
			alert('分享成功')
		} else {
			alert('分享失败')
		}
	})
})
