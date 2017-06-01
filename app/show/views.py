#coding=utf-8
import json
import sys
import logging
logging.basicConfig(level=logging.INFO)


from flask import render_template, jsonify, request
from flask_login import current_user, login_required

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

@show.route('/user/<int:id>/list', methods=['GET'])
@login_required
def get_reading_list(id):
    """ 请求文章列表 """
    if current_user.u_id != id:
        output()
    readings_map = User.query.filter_by(u_id=id).first().readings
    readings = []
    for reading in readings_map:
        readings.append(Reading.query.filter_by(id=reading.reading_id).first())
    logging.info('readings=%s' % readings)
    if readings:
        output(to_json=False)

    order_set = {x.reading_order for x in readings}
    data = {}

    for order in order_set:
        name_dict = {}
        for x in Reading.query.filter_by(reading_order=order).all():
            name_dict[x.r_id] = x.reading_name
        data[order] = name_dict

    # data = {x:y for x in order_list for y in name_list}
    return output(data=data, to_json=False)


@show.route('/reading/<int:id>/sentence_notes', methods=['GET'])
# @check_user('reading')
def get_sentence_notes(id):
    """ 请求文章下所有的句子笔记 """
    reading = Reading.query.filter_by(r_id=id).first()
    sentence_notes = dict()
    for sentence in reading.sentences:
        note = dict()
        note['sentence_id'] = sentence.id
        note['phrase'] = sentence.sentence_notes.phrase
        note['grammar'] = sentence.sentence_notes.grammar
        note['translation'] = sentence.sentence_notes.translation
        sentence_notes[sentence.id] = note
    return output(sentence_notes)

@show.route('/reading/<int:id>', methods=['GET'])
# @check_user('reading')
def get_reading(id):
    """ 请求文章 """
    reading = Reading.query.filter_by(r_id=id).first()
    return output(reading)

@show.route('/reading/<int:id>/word_notes', methods=['GET'])
# @check_user('reading')
def get_word_notes(id):
    """ 请求文章下所有的单词笔记 """
    reading = Reading.query.filter_by(r_id=id).first()
    word_notes = dict()
    for sentence in reading.sentences:
        for word in sentence.words:
            note = dict()
            note['word_id'] = word.id
            note['Phonogram'] = word.Phonogram
            note['Chinese'] = word.Chinese
            word_notes[word]
    return output(word_notes)

@show.route('/sentence/<int:id>', methods=['GET'])
# @check_user('sentence')
def sentence(id):
    """ 请求句子 """
    sentence = Sentence.query.filter_by(s_id=id).first()
    return output(sentence)

@show.route('/sentence/<int:id>/note', methods=['GET'])
# @check_user('sentence')
def get_sentence_note(id):
    """ 请求句子的笔记 """
    sentence = Sentence.query.filter_by(s_id=id).first()
    sentence_note = sentence.sentence_notes.order_by(Sentence_Note.id.desc()).first()
    if isinstance(sentence_note, Sentence_Note):
        return output(sentence_note)
    return output()

@show.route('/word/<int:id>', methods=['GET'])
# @check_user('word')
def word(id):
    """ 请求单词 """
    word = Word.query.filter_by(w_id=id).first()
    return output(word)

@show.route('/word/<int:id>/note', methods=['GET'])
# @check_user('word')
def get_word_note(id):
    """ 请求单词的笔记 """
    word = Word.query.filter_by(w_id=id).first()
    word_note = word.word_note.order_by(Word_Note.id.desc()).first()
    if isinstance(word_note, Word_Note):
        return output(word_note)
    return output()


@show.route('/user/<int:id>/sentences', methods=['GET'])
def get_user_sentences(id):
    """ 请求用户所有笔记句子 """
    user = User.query.filter_by(u_id=id).first()
    sentences = user.sentences.all()
    noted_sens = [ sen for sen in sentences if sen.sentence_notes.first() is not None ]
    # data
    ret = {}
    sentences = []
    for sen in noted_sens:
        data = {}
        data['sen_id'] = sen.s_id
        data['reading_id'] = sen.reading_id
        data['sen_body'] = sen.sentence_body
        sentences.append(data)
    if not sentences:
        logging.info('user_sentences_data not exist')
    ret['sentences'] = sentences
    return output(ret, to_json=False)

@show.route('/user/<int:id>/words', methods=['GET'])
def get_user_words(id):
    """ 请求用户所有笔记单词 """
    user = User.query.filter_by(u_id=id).first()
    words = user.words.all()
    noted_words = [ word for word in words if word.word_note.first() is not None ]

    if not noted_words:
        return output()

    # set ret data
    ret = {}
    words = []
    for word in noted_words:
        data = {}
        data['word_id'] = word.w_id
        sen_id = word.sentence_id
        logging.debug('sen_id={}'.format(sen_id))
        sentence = Sentence.query.filter_by(s_id=sen_id).first()
        if not sentence:
            logging.info('user_word_sentence not exist')
            data['reading_id'] = 0
        else:
            data['reading_id'] = sentence.reading_id
        data['sen_id'] = sen_id
        data['word_body'] = word.word_body
        words.append(data)
    if not words:
        logging.info('user_sentence_data not exist')
    ret['words'] = words
    return output(ret, to_json=False)

