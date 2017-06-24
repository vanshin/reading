#coding=utf-8
import json
import sys
import logging
logging.basicConfig(level=logging.INFO)


from flask import render_template, jsonify, request
from flask_login import current_user, login_required


from config import RRET
from ..output import output
from ..decorator import check_user
from . import show
from ..models import (
    Reading, Sentence,
    Sentence_Note, Word, Word_Note,
    User, User_Reading_Map
)
from .. import db
from ..reading import ReadingProcess, get_random

@check_user('user')
@show.route('/user/<int:id>/list', methods=['GET'])
def get_reading_list(id):
    """ 请求文章列表 """
    user_readings = User.query.filter_by(u_id=id).first().readings

    # 生成reading ORM OBJECT的列表
    readings = []
    for reading in user_readings:
        readings.append(Reading.query.filter_by(id=reading.reading_id).first())
    if not readings:
        return output(RRET.RES_NOT_EXIST)

    # 获取 order
    order_set = {x.reading_order for x in readings}

    # 根据order生成数据，name_dict是id:name
    data = {}
    for order in order_set:
        name_dict = {y.r_id: y.reading_name for y in readings if y.reading_order == order}
        data[order] = name_dict
    return output(RRET.SUCCESS, data=data)


@check_user('reading')
@show.route('/reading/<int:id>/sentence_notes', methods=['GET'])
def get_sentence_notes(id):
    """ 请求文章下所有的句子笔记 """
    reading = Reading.query.filter_by(r_id=id).first()
    sentence_notes = {}
    for sentence in reading.sentences:
        note = {}
        note['sentence_id'] = sentence.id
        note['phrase'] = sentence.sentence_notes.phrase
        note['grammar'] = sentence.sentence_notes.grammar
        note['translation'] = sentence.sentence_notes.translation
        sentence_notes[sentence.id] = note
    return output(RRET.SUCCESS, data=sentence_notes)

@check_user('reading')
@show.route('/reading/<int:id>', methods=['GET'])
def get_reading(id):
    """ 请求文章 """
    reading = Reading.query.filter_by(r_id=id).first()
    print(reading)
    return output(RRET.SUCCESS, data=reading)

@show.route('/reading/<int:id>/word_notes', methods=['GET'])
@check_user('reading')
def get_word_notes(id):
    """ 请求文章下所有的单词笔记 """
    reading = Reading.query.filter_by(r_id=id).first()
    word_notes = {}
    for sentence in reading.sentences:
        for word in sentence.words:
            note = dict()
            note['word_id'] = word.id
            note['Phonogram'] = word.Phonogram
            note['Chinese'] = word.Chinese
            word_notes[word]
    return output(RRET.SUCCESS ,data=word_notes)

@show.route('/sentence/<int:id>', methods=['GET'])
@check_user('sentence')
def sentence(id):
    """ 请求句子 """
    sentence = Sentence.query.filter_by(s_id=id).first()
    return output(RRET.SUCCESS, data=sentence)

@show.route('/sentence/<int:id>/note', methods=['GET'])
@check_user('sentence')
def get_sentence_note(id):
    """ 请求句子的笔记 """
    sentence = Sentence.query.filter_by(s_id=id).first()
    sentence_note = sentence.sentence_notes.order_by(Sentence_Note.id.desc()).first()
    if isinstance(sentence_note, Sentence_Note):
        return output(RRET.SUCCESS, data=sentence_note)
    return output()

@show.route('/word/<int:id>', methods=['GET'])
@check_user('word')
def word(id):
    """ 请求单词 """
    word = Word.query.filter_by(w_id=id).first()
    return output(word)

@show.route('/word/<int:id>/note', methods=['GET'])
@check_user('word')
def get_word_note(id):
    """ 请求单词的笔记 """
    word = Word.query.filter_by(w_id=id).first()
    word_note = word.word_note.order_by(Word_Note.id.desc()).first()
    if isinstance(word_note, Word_Note):
        return output(word_note)
    return output()


