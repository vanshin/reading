$(document).ready(function(){
    var id = get_userid()
    sentences(id)
})

function sentences(id) {
    var sen = $('#sentences')
    $.ajax({
        type: 'GET',
        url: '/user/'+id+'/sentences',
        dataType: 'JSON',
    }).done(function(data){
        sentences = data.sentences
        for (sentence in sentences){
            var sen_id = sentences[sentence].sen_id
            test = get_vertical_segment('sen_id', sen_id, sentences[sentence].sen_body)
            btn = get_ibutton('note')
            btn.setAttribute('sen_id', sen_id)
            test.append(btn)
            test.setAttribute('id', sen_id)
            sen.append(test)
        }
    })
}

$('div').delegate('input','click', function(e){
	var sen_id = $(this).attr('sen_id')
    get_note(sen_id)
	
})

function get_note(sen_id) {
    var sen =  $('#'+sen_id)
    $.ajax({
        type: 'GET',
        url: 'sentence/'+sen_id+'/note',
        dataType: 'JSON',
    }).done(function(data){
        if (data.code == 200){
            var grammar = data.grammar
                phrase = data.phrase
                translation = data.translation
            sen.append(get_p(grammar, "语法: "))
            sen.append(get_p(phrase, "短语: "))
            sen.append(get_p(translation, "翻译: "))
        }
    })

}