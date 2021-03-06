function clearShowing(){
	var phrase = $("p#phrase")
		grammar = $("p#grammar")
		translation = $("p#translation")
	phrase.empty()
	grammar.empty()
	translation.empty()
}

function clearWordShowing(){
	var Chinese = $("p#Chinese")
		Phonogram = $("p#Phonogram")
	Chinese.empty()
	Phonogram.empty()
}

function clearWordForm(){
	var Chinese = $("input#Chinese")
		Phonogram = $("input#Phonogram")
	Chinese.val("")
	Phonogram.val("")
}

function clearForm(){
	form = $('textarea.form-control')
	form.val("")
}

function get_userid() {
	var id
	$.ajax({
		type:'GET',
		url:'/current_user/id',
		dataType:'json',
		async: false,
		cache: false,
	}).done(function(data){
        if (data.code == 200){
            id = data.id
        }
	})
	return id
}

function create_title(title) {
	var i = document.createElement('I')
	i.setAttribute("class", "dropdown icon")
	var a = document.createElement('A')
	a.setAttribute("class", "title")
	var b = document.createElement('B')
	b.innerText = title
	a.append(i)
	a.append(b)
	return a
}

function create_content(content) {
	var div_con = document.createElement('DIV')
	div_con.setAttribute("class", "content menu")
	div_con.append(get_list(content))
	return div_con
}

function get_item(title, content) {
	div_item = document.createElement('DIV')
	div_item.setAttribute("class", "item")
	title_div = create_title(title)
	content_div = create_content(content)
	div_item.append(title_div)
	div_item.append(content_div)
	return div_item
}

function get_keys(json) {
	keys = []
	for (index in json) {
		keys.push(index)
	}
	return keys
}

function get_values(json) {
	values = []
	for (index in json) {
		values.push(json[index])
	}
	return values
}

function get_list(content_json) {
	var div_list = document.createElement('DIV')
	div_list.setAttribute("class", "ui link list")
	contents = get_values(content_json)
	ids = get_keys(content_json)
	for (i=0;i<contents.length;i++){
		var a = document.createElement('A')
		a.setAttribute("class", "item reading_list")
		a.setAttribute("id", ids[i])
		a.innerHTML = contents[i]
		div_list.append(a)
	}
	return div_list
}


function get_span(sen_id, text) {
	var span = document.createElement('SPAN')
	span.setAttribute('class', 'reading_content')
	span.setAttribute('sen_id', sen_id)
	span.innerText = text
	return span
}

function get_vertical_segment(type, type_id, content) {
	var div = document.createElement('DIV')
	div.setAttribute('class', 'ui vertical segment')
	div.setAttribute(type, type_id)
	div.innerText = content
	return div
}

function get_button(content) {
	var button = document.createElement('BUTTON')
	button.setAttribute('class', 'compact ui button')
	button.innerText = content
	return button
}

function get_p(content, prefix) {
	var p = document.createElement('P')
	p.setAttribute('class', '')
	p.innerText = prefix + content
	// if (prefix) {
	// 	p.innerText = content
	// } else {
	// 	p.innerText = prefix + content
	// }
	
	return p
}

function get_ibutton(content) {
	var ibutton = document.createElement('INPUT')
	ibutton.setAttribute('type', 'button')
	ibutton.setAttribute('value', content)
	return ibutton
}

function get_div() {
	var div = document.createElement('DIV')
	return div
}

function get_tbody() {
	var tbody = document.createElement('TBODY')
	return tbody
}

function get_tr() {
	var tr = document.createElement('TR')
	return tr
}

function get_td(content) {
	var td = document.createElement('TD')
	td.innerText = content
	return td
}


function a_get(){
	$.ajax({
		type: 'GET',
		url: 'user/1235139/list',

	}).done(function(data){
		return data
	})
}

// function x_get(){
// 	axios.get({
// 		url: '/user'
// 	})
// }


