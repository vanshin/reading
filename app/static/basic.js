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