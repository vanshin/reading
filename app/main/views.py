#coding=utf-8
import json
from flask import render_template, jsonify, request
from ..output import output
from . import main
from .forms import readingForm
from ..models import Reading, Sentence, Sentence_Note
from .. import db


@main.route('/')
def index():
    """ 首页 """
    readings = Reading.query.order_by(Reading.reading_order).all()
    order_list = set()
    for reading in readings:
        order_list.add(reading.reading_order)
    return render_template('index.html', order_list=order_list, readings=readings)


@main.route('/input', methods=['POST', 'GET'])
def input():
    """ 输入阅读理解 """
    form = readingForm()
    if form.validate_on_submit():
        reading_order = form.reading_order.data
        reading_name = form.reading_name.data
        reading_body = form.reading_body.data
        sentences_list_tmp = reading_body.split('.')
        sentences_list = list()
        for sentence in sentences_list_tmp:
            sentence = sentence.replace('\r\n', '').lstrip()
            sentences_list.append(sentence)
        reading = Reading(reading_order=reading_order,
                          reading_name=reading_name,
                          reading_body=reading_body)
        db.session.add(reading)
        db.session.commit()
        reading_id = reading.id
        for sentence_body in sentences_list:
            sentence = Sentence(reading_id=reading_id, sentence_body=sentence_body)
            db.session.add(sentence)
    return render_template('input.html', form=form)

@main.route('/reading/<int:id>', methods=['GET'])
def reading(id):
    """ 请求文章 """
    reading = Reading.query.filter_by(id=id).first().to_json()
    return output(reading, 200)

@main.route('/reading/<int:id>/word_notes', methods=['GET'])
def get_word_notes(id):
    """ 请求文章下所有的单词笔记 """
    reading = Reading.query.filter_by(id=id).first()
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
    reading = Reading.query.filter_by(id=id).first()
    sentence_notes = dict()
    for sentence in reading.sentences:
        note = dict()
        note['sentence_id'] = sentence.id
        note['phrase'] = sentence.sentence_notes.phrase
        note['grammar'] = sentence.sentence_notes.grammar
        note['translation'] = sentence.sentence_notes.translation
        sentence_notes[sentence.id] = note
    return output(sentence_notes)

@main.route('/reading/<int:id>/sentences', methods=['GET'])
def get_sentences(id):
    """ 请求文章的句子 """
    pass

@main.route('/sentence/<int:id>', methods=['GET'])
def sentence(id):
    """ 请求句子 """
    sentence = Sentence.query.filter_by(id=id).first().to_json()
    return output(sentence, 200)

@main.route('/sentence/<int:id>/note', methods=['GET'])
def get_sentence_note(id):
    """ 请求句子的笔记 """
    sentence_notes = Sentence.query.filter_by(id=id).first().sentence_notes
    sentence_note = dict()
    for note in sentence_notes:
        sentence_note['phrase'] = note.phrase
        sentence_note['grammar'] = note.grammar
        sentence_note['translation'] = note.translation
    return output(sentence_note, 200)

@main.route('/word/<int:id>', methods=['GET'])
def word(id):
    """ 请求单词 """
    word = Word.query.filter_by(id=id).first().to_json()
    return output(word, 200)

@main.route('/word/<int:id>/note', methods=['GET'])
def get_word_note(id):
    """ 请求单词的笔记 """
    word_notes = Word.query.filter_by(id=id).first().word_notes
    return output(word_notes, 200)



@main.route('/sentences/<int:id>/note', methods=['PUT'])
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
    return output(sentence_note.to_json(),201)

@main.route('/word/<int:id>/note', methods=['PUT'])
def edit_word_notes(id):
    """ 更新/创建单词笔记 """
    json_word_notes = request.get_json(force=True, silent=True)
    Chinese = json_word_notes.get("Chinese")
    Phonogram = json_word_notes.get("Phonogram")
    word_notes = Word_Note(Chinese=Chinese, Phonogram=Phonogram)
    db.session.add(word_notes)
    return output(word_notes, 201)



@main.route('/sentence/<int:id>/note', methods=['DELETE'])
def delete_sentence_notes(id):
    """ 删除句子笔记 """
    pass