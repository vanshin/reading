$(document).ready(function(){
    var id = get_userid()
    get_userlist(id)
})

function get_userlist(id) {
    var readings = $('#readings')
    var tbody = $('#tbody')
    $.ajax({
		type: 'GET',
		url: '/user/'+id+'/list',
		dataType: 'json'
	}).done(function(data){
		$.each(data, function(key, value){
			if (key!='code' && key!= 'message'){
				var title = key
				for (x in value){

                    var tr = get_tr()
                    tr.append(get_td(value[x]))
                    tr.append(get_td(x))
                    tbody.append(tr)
				}
				
			}
		})				
	})
}

$("#submitshare").click(function(){
	var user_id = $("input#user").val()
		r_id = $('input#reading').val()
    if (user_id == '' || r_id == ''){
        alert('请输入id')
        return
    }
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
