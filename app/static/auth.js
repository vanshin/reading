function clearForm(){
	$("input:text").val("")
}

$("#submitus").click(function(){
    var username = $("#username").val()
        password = $("#password").val()
        password2 = $("#password2").val()
    userinfo = {
        "username": username,
        "password": password,
        "password2": password2
    }
    console.log("test")
    if (password != password2) {
        alert("密码不同")
    }else{
        $.ajax({
            type: "POST",
            url: "/auth/user",
            data: JSON.stringify(userinfo),
            dataType: "json",
            contentType: "application/json"
        }).done(function(data){
            clearForm()
        })
    }
    

})

$("#li-regi").click(function(){
    location.pathname = "/regi"
})

$("#li-login").click(function(){
	location.pathname = "/login"
})

