$(document).ready(function(){
    var id = get_userid()
    words(id)
})

function words(id) {
    var words_d = $('#words')
    $.ajax({
        type: 'GET',
        url: '/user/'+id+'/words',
        dataType: 'JSON',
    }).done(function(data){
        words = data.words
        for (word in words){
            var w_id = words[word].word_id
            test = get_vertical_segment('w_id', w_id, words[word].word_body)
            btn = get_ibutton('note')
            btn.setAttribute('w_id', w_id)
            test.append(btn)
            test.setAttribute('id', w_id)
            words_d.append(test)
        }
    })
}

$('div').delegate('input','click', function(e){
	var w_id = $(this).attr('w_id')
    get_note(w_id)
	
})

function get_note(w_id) {
    var word =  $('#'+w_id)
    $.ajax({
        type: 'GET',
        url: 'word/'+w_id+'/note',
        dataType: 'JSON',
    }).done(function(data){
        if (data.code == 200){
            var Chinese = data.Chinese
                Phonogram = data.Phonogram
            word.append(get_p(Chinese, "中文: "))
            word.append(get_p(Chinese, "音标: "))
        }
    })

}