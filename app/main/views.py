#coding=utf-8
import json
import sys
import logging
logging.basicConfig(level=logging.INFO)


from flask import render_template, jsonify, request
from flask_login import current_user, login_required

from ..output import output
from ..decorator import check_user
from . import main
from .forms import readingForm
from ..models import (
    Reading, Sentence,
    Sentence_Note, Word, Word_Note,
    User, User_Reading_Map
)
from .. import db
from ..reading import ReadingProcess, get_random



@main.route('/', methods=['GET'])
def index():
    """ 首页 """
    return render_template('index.html')


@main.route('/input', methods=['GET'])
def input():
    """ 请求页面 """
    return render_template('input.html')


@main.route('/test', methods=['GET'])
def test():
    """ 测试有的没的 """
    return render_template('test.html')
# @main.route('/user/<int:id>/list', methods=['GET'])
# @login_required
# def get_reading_list(id):
#     """ 请求文章列表 """
#     if current_user.u_id != id:
#         output()
#     readings_map = User.query.filter_by(u_id=id).first().readings
#     readings = []
#     for reading in readings_map:
#         readings.append(Reading.query.filter_by(id=reading.reading_id).first())
#     logging.info('readings=%s' % readings)
#     if readings:
#         output(to_json=False)

#     order_set = {x.reading_order for x in readings}
#     data = {}

#     for order in order_set:
#         name_dict = {}
#         for x in Reading.query.filter_by(reading_order=order).all():
#             name_dict[x.r_id] = x.reading_name
#         data[order] = name_dict

#     # data = {x:y for x in order_list for y in name_list}
#     return output(data=data, to_json=False)

# @main.route('/reading', methods=['POST'])
# def put_reading():
#     """ 输入阅读理解 """
#     json_reading = request.get_json(force=True, silent=True)
#     reading_order = json_reading.get("reading_order")
#     reading_name = json_reading.get("reading_name")
#     reading_body = json_reading.get("reading_body")
#     user_id = current_user.id
#     # 处理文章
#     reading_offset = 1
#     reading = ReadingProcess(reading_body)
#     reading_ = Reading(reading_order=reading_order,
#                        reading_name=reading_name,
#                        reading_body=reading_body,
#                        r_id=get_random(),    # 此处需要验证reading是不是唯一的
#                        owner=user_id,
#                        offset=reading_offset
#                       )
#     reading_offset += 1
#     db.session.add(reading_)
#     db.session.commit()

#     reading_id = reading_.id
#     # 处理句子，句子需要添加段落id
#     sentence_offset = 1
#     for index in range(1, reading.parag_count()+1):
#         logging.info('reading parag_number=%s' % index)
#         logging.info('reading parag=%s' % ','.join(reading.parags().get(index, [])))
#         for sentence_body in reading.parags().get(index, []):
#             logging.info('sentence_body=%s' % sentence_body)
#             sentence = Sentence(reading_id=reading_id,
#                                 s_id=get_random(),
#                                 parag_number=index,
#                                 sentence_body=sentence_body,
#                                 user_id=user_id,
#                                 offset = sentence_offset
#                                )
#             reading_offset += 1
#             db.session.add(sentence)
#             db.session.commit()
#             # 处理单词
#             word_offset = 1
#             word_list = sentence_body.split(' ')
#             for word_body in word_list:
#                 word = Word(sentence_id=sentence.id,
#                             w_id=get_random(),
#                             word_body=word_body,
#                             user_id=user_id,
#                             offset = word_offset
#                            )
#                 word_offset += 1
#                 db.session.add(word)
#                 db.session.commit()

#     ur_map = User_Reading_Map(reading_id=reading_id, user_id=user_id)
#     db.session.add(ur_map)
#     db.session.commit()
#     return output(reading_)

# @main.route('/reading/<int:id>', methods=['GET'])
# # @check_user('reading')
# def get_reading(id):
#     """ 请求文章 """
#     reading = Reading.query.filter_by(r_id=id).first()
#     return output(reading)

# @main.route('/reading/<int:id>/word_notes', methods=['GET'])
# # @check_user('reading')
# def get_word_notes(id):
#     """ 请求文章下所有的单词笔记 """
#     reading = Reading.query.filter_by(r_id=id).first()
#     word_notes = dict()
#     for sentence in reading.sentences:
#         for word in sentence.words:
#             note = dict()
#             note['word_id'] = word.id
#             note['Phonogram'] = word.Phonogram
#             note['Chinese'] = word.Chinese
#             word_notes[word.word.body] = note
    # return output(word_notes)


# @main.route('/reading/<int:id>/sentence_notes', methods=['GET'])
# # @check_user('reading')
# def get_sentence_notes(id):
#     """ 请求文章下所有的句子笔记 """
#     reading = Reading.query.filter_by(r_id=id).first()
#     sentence_notes = dict()
#     for sentence in reading.sentences:
#         note = dict()
#         note['sentence_id'] = sentence.id
#         note['phrase'] = sentence.sentence_notes.phrase
#         note['grammar'] = sentence.sentence_notes.grammar
#         note['translation'] = sentence.sentence_notes.translation
#         sentence_notes[sentence.id] = note
#     return output(sentence_notes)

# @main.route('/sentence/<int:id>', methods=['GET'])
# # @check_user('sentence')
# def sentence(id):
#     """ 请求句子 """
#     sentence = Sentence.query.filter_by(s_id=id).first()
#     return output(sentence)

# @main.route('/sentence/<int:id>/note', methods=['GET'])
# # @check_user('sentence')
# def get_sentence_note(id):
#     """ 请求句子的笔记 """
#     sentence = Sentence.query.filter_by(s_id=id).first()
#     sentence_note = sentence.sentence_notes.order_by(Sentence_Note.id.desc()).first()
#     if isinstance(sentence_note, Sentence_Note):
#         return output(sentence_note)
#     return output()

# @main.route('/word/<int:id>', methods=['GET'])
# # @check_user('word')
# def word(id):
#     """ 请求单词 """
#     word = Word.query.filter_by(w_id=id).first()
#     return output(word)

# @main.route('/word/<int:id>/note', methods=['GET'])
# # @check_user('word')
# def get_word_note(id):
#     """ 请求单词的笔记 """
#     word = Word.query.filter_by(w_id=id).first()
#     word_note = word.word_note.order_by(Word_Note.id.desc()).first()
#     if isinstance(word_note, Word_Note):
#         return output(word_note)
#     return output()

# @main.route('/sentence/<int:id>/note', methods=['PUT'])
# def edit_sentence_notes(id):
#     """ 更新/创建句子笔记 """
#     json_sentence_notes = request.get_json(force=True, silent=True)
#     phrase = json_sentence_notes.get("phrase")
#     grammar = json_sentence_notes.get("grammar")
#     translation = json_sentence_notes.get("translation")
#     sentence_id = Sentence.query.filter_by(s_id=id).first().id
#     sentence_note = Sentence_Note(phrase=phrase,
#                                   grammar=grammar,
#                                   translation=translation,
#                                   sentence_id=sentence_id,
#                                   sn_id=get_random()
#                                  )
#     db.session.add(sentence_note)
#     return output(sentence_note)

# @main.route('/word/<int:id>/note', methods=['PUT'])
# def edit_word_notes(id):
#     """ 更新/创建单词笔记 """
#     json_word_note = request.get_json(force=True, silent=True)
#     word = Word.query.filter_by(w_id=id).first()
#     Chinese = json_word_note.get("Chinese")
#     Phonogram = json_word_note.get("Phonogram")
#     word_note = Word_Note(word_id=word.id,
#                           Chinese=Chinese,
#                           Phonogram=Phonogram,
#                           wn_id=get_random(),
#                          )
#     db.session.add(word_note)
#     # db.session.commit()
#     return output(word_note)

# @main.route('/reading/<int:id>/parag', methods=['GET'])
# def get_parag(id):
#     r = Reading.query.filter_by(r_id=id).first()
#     data = r.reading_body1()
#     return jsonify(data)

# @main.route('/sentence/<int:id>/note', methods=['DELETE'])
# def delete_sentence_notes(id):
#     """ 删除句子笔记 """
#     pass