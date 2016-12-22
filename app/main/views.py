#coding=utf-8
import json
from flask import render_template, jsonify, request
from flask_login import current_user
from ..output import output
from . import main
from .forms import readingForm
from ..models import Reading, Sentence, Sentence_Note, Word, Word_Note, User
from .. import db


@main.route('/', methods=['GET'])
def index():
    """ 首页 """
    return render_template('index.html')

@main.route('/input', methods=['GET'])
def input():
    """ 请求页面 """
    return render_template('input.html')

@main.route('/current_user/id', methods=['GET'])
def get_user_id():
    """ 获取当前用户的ID """
    if current_user.is_anonymous:
        output()
    info = dict(id=current_user.id, current_userid=current_user.userid)
    return output(data=info, to_json=False)

@main.route('/user/<int:id>/list', methods=['GET'])
def get_reading_list(id):
    """ 请求文章列表 """
    readings = User.query.get_or_404(id).readings
    if readings:
        output(to_json=False)
    print readings
    reading_order = list({x.reading_order for x in readings})
    reading_name = [x.reading_name for x in readings]
    print reading_name
    print reading_order
    data = {
        "reading_order": reading_order,
        "reading_name": reading_name
    }
    return output(data=data, to_json=False)

@main.route('/reading', methods=['POST'])
def put_reading():
    """ 输入阅读理解 """
    json_reading = request.get_json(force=True, silent=True)
    reading_order = json_reading.get("reading_order")
    reading_name = json_reading.get("reading_name")
    reading_body = json_reading.get("reading_body")
    user_id = current_user.id

    # 获取句子
    sentences_list_tmp = reading_body.split('.')
    sentences_list = list()
    for sentence in sentences_list_tmp:
        sentence = sentence.replace('\r\n', '').lstrip()
        sentences_list.append(sentence)
    reading = Reading(reading_order=reading_order,
                      reading_name=reading_name,
                      reading_body=reading_body,
                      user_id=user_id)
    db.session.add(reading)
    db.session.commit()
    reading_id = reading.id
    for sentence_body in sentences_list:
        sentence = Sentence(reading_id=reading_id, sentence_body=sentence_body)
        db.session.add(sentence)
        db.session.commit()
        word_list = sentence_body.split(' ')
        for word_body in word_list:
            word = Word(sentence_id=sentence.id, word_body=word_body)
            db.session.add(word)
            db.session.commit()
    return output(reading)

@main.route('/reading/<int:id>', methods=['GET'])
def get_reading(id):
    """ 请求文章 """
    reading = Reading.query.get_or_404(id)
    return output(reading)

@main.route('/reading/<int:id>/word_notes', methods=['GET'])
def get_word_notes(id):
    """ 请求文章下所有的单词笔记 """
    reading = Reading.query.get_or_404(id)
    word_notes = dict()
    for sentence in reading.sentences:
        for word in sentence.words:
            note = dict()
            note['word_id'] = word.id
            note['Phonogram'] = word.Phonogram
            note['Chinese'] = word.Chinese
            word_notes[word.word.body] = note
    return output(word_notes)

@main.route('/reading/<int:id>/sentence_notes', methods=['GET'])
def get_sentence_notes(id):
    """ 请求文章下所有的句子笔记 """
    reading = Reading.query.get_or_404(id)
    sentence_notes = dict()
    for sentence in reading.sentences:
        note = dict()
        note['sentence_id'] = sentence.id
        note['phrase'] = sentence.sentence_notes.phrase
        note['grammar'] = sentence.sentence_notes.grammar
        note['translation'] = sentence.sentence_notes.translation
        sentence_notes[sentence.id] = note
    return output(sentence_notes)

@main.route('/sentence/<int:id>', methods=['GET'])
def sentence(id):
    """ 请求句子 """
    sentence = Sentence.query.get_or_404(id)
    return output(sentence)

@main.route('/sentence/<int:id>/note', methods=['GET'])
def get_sentence_note(id):
    """ 请求句子的笔记 """
    sentence = Sentence.query.get_or_404(id)
    sentence_note = sentence.sentence_notes.order_by(Sentence_Note.id.desc()).first()
    if isinstance(sentence_note, Sentence_Note):
        return output(sentence_note)
    return output()

@main.route('/word/<int:id>', methods=['GET'])
def word(id):
    """ 请求单词 """
    word = Word.query.get_or_404(id)
    return output(word)

@main.route('/word/<int:id>/note', methods=['GET'])
def get_word_note(id):
    """ 请求单词的笔记 """
    word = Word.query.get_or_404(id)
    word_note = word.word_note.order_by(Word_Note.id.desc()).first()
    if isinstance(word_note, Word_Note):
        return output(word_note)
    return output()

@main.route('/sentence/<int:id>/note', methods=['PUT'])
def edit_sentence_notes(id):
    """ 更新/创建句子笔记 """
    json_sentence_notes = request.get_json(force=True, silent=True)
    phrase = json_sentence_notes.get("phrase")
    grammar = json_sentence_notes.get("grammar")
    translation = json_sentence_notes.get("translation")
    sentence_note = Sentence_Note(phrase=phrase,
                                  grammar=grammar,
                                  translation=translation,
                                  sentence_id=id)
    db.session.add(sentence_note)
    return output(sentence_note)

@main.route('/word/<int:id>/note', methods=['PUT'])
def edit_word_notes(id):
    """ 更新/创建单词笔记 """
    json_word_note = request.get_json(force=True, silent=True)
    word_id = json_word_note.get("word_id")
    Chinese = json_word_note.get("Chinese")
    Phonogram = json_word_note.get("Phonogram")
    word_note = Word_Note(word_id=word_id, Chinese=Chinese, Phonogram=Phonogram)
    db.session.add(word_note)
    db.session.commit()
    return output(word_note)



@main.route('/sentence/<int:id>/note', methods=['DELETE'])
def delete_sentence_notes(id):
    """ 删除句子笔记 """
    pass