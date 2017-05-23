#coding=utf-8

import logging
logging.basicConfig(level=logging.DEBUG)

from . import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User_Reading_Map(db.Model):
    __tablename__ = 'user_reading_maps'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key='True')
    reading_id = db.Column(db.Integer, db.ForeignKey('readings.id'), primary_key='True')
    ctime = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', back_populates='readings')
    reading = db.relationship('Reading', back_populates='users')

class Reading(db.Model):
    __tablename__ = 'readings'  
    id = db.Column(db.Integer, primary_key=True)
    r_id = db.Column(db.Integer, unique=True)
    reading_order = db.Column(db.Text)
    reading_name = db.Column(db.String(64))
    reading_body = db.Column(db.Text)
    sentences = db.relationship('Sentence', backref='reading', lazy='dynamic', cascade="delete")
    owner = db.Column(db.Integer)
    users = db.relationship('User_Reading_Map', back_populates="reading")
    offset = db.Column(db.Integer)

    def __repf__(self):
        return '<Reading %r>' % self.reading_name

    def get_body(self):
        parag_number_set = set()
        parag_body = {}
        for sentence in self.sentences:
            parag_number_set.add(sentence.parag_number)
        logging.debug(parag_number_set)
        for parag_numner in parag_number_set:
            dict_s_id = {x.s_id: x.sentence_body for x in self.sentences if x.parag_number == parag_numner}
            parag_body[parag_numner] = dict_s_id
        return parag_body

    def get_offset(self):
        parag_number_set = set()
        parag_body = {}
        for sentence in self.sentences:
            parag_number_set.add(sentence.parag_number)
        logging.debug(parag_number_set)
        for parag_numner in parag_number_set:
            dict_offset = {x.s_id: x.offset for x in self.sentences if x.parag_number == parag_numner}
            parag_body[parag_numner] = dict_offset
        return parag_body


    def to_json(self):
        json_reading = {
            'id': self.r_id,
            'reading_order': self.reading_order,
            'reading_name': self.reading_name,
            'reading_body': self.get_body(),
            'reading_offset': self.get_offset()
        }
        return json_reading



class Sentence(db.Model):
    __tablename__ = 'sentences'
    id = db.Column(db.Integer, primary_key=True)
    reading_id = db.Column(db.Integer, db.ForeignKey('readings.id'))
    s_id = db.Column(db.Integer, unique=True)
    parag_number = db.Column(db.Integer)
    words = db.relationship('Word', backref='sentence', lazy='dynamic', cascade='all, delete')
    sentence_notes = db.relationship('Sentence_Note',
                                     backref='sentence',
                                     lazy='dynamic',
                                     cascade='delete')
    sentence_body = db.Column(db.Text)
    comment = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    offset = db.Column(db.Integer)

    def __repf__(self):
        return '<Sentence %d>' % self.id

    def to_json(self):
        """ return json data """
        words = list()
        for word in self.words:
            words.append(word.word_body)
        json_sentence = {
            'id': self.s_id,
            'parag_number': self.parag_number,
            'sentence_body': self.sentence_body,
            'words': {x.w_id :x.word_body for x in self.words}
        }
        return json_sentence

    @property
    def password(self):
        raise AttributeError('password is not a readable attr')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class Sentence_Note(db.Model):
    """ sentence_note model """
    __tablename__ = 'sentence_notes'
    id = db.Column(db.Integer, primary_key=True)
    sn_id = db.Column(db.Integer, unique=True)
    sentence_id = db.Column(db.Integer, db.ForeignKey('sentences.id'))
    phrase = db.Column(db.Text)
    grammar = db.Column(db.Text)
    translation = db.Column(db.Text)

    def to_json(self):
        """ 生成JSON数据 """
        json_sentence_note = {
            'sn_id': self.sn_id,
            'phrase': self.phrase,
            'grammar': self.grammar,
            'translation': self.translation
        }
        return json_sentence_note

class Word(db.Model):
    """ word model """
    __tablename__ = 'words'
    id = db.Column(db.Integer, primary_key=True)
    w_id = db.Column(db.Integer, unique=True)
    sentence_id = db.Column(db.Integer, db.ForeignKey('sentences.id'))
    word_note = db.relationship('Word_Note',
                                backref='word',
                                lazy='dynamic',
                                uselist='False',
                                cascade="delete",
                               )
    word_body = db.Column(db.String(32))
    offset = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def to_json(self):
        """ 返回单词 """
        json_word = {
            "id": self.w_id,
            "word_body": self.word_body
        }
        return json_word

class Word_Note(db.Model):
    """ word_note model """
    __tablename__ = 'word_notes'
    id = db.Column(db.Integer, primary_key=True)
    wn_id = db.Column(db.Integer, unique=True)
    word_id = db.Column(db.Integer, db.ForeignKey('words.id'))
    Chinese = db.Column(db.String(64))
    Phonogram = db.Column(db.String(32))

    def to_json(self):
        json_word_note = {
            "id": self.id,
            "Chinese": self.Chinese,
            "Phonogram": self.Phonogram
        }
        return json_word_note


class User(db.Model, UserMixin):
    """ user model """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    u_id = db.Column(db.Integer, unique=True)
    username = db.Column(db.String(64), index=True)
    password_hash = db.Column(db.String(128))
    regi_time = db.Column(db.DateTime(), default=datetime.utcnow)
    avatar_hash = db.Column(db.String(64))
    location = db.Column(db.String(64))
    introduction = db.Column(db.Text)
    sentences = db.relationship('Sentence', backref='user', lazy='dynamic')
    words = db.relationship('Word', backref='user', lazy='dynamic')
    readings = db.relationship('User_Reading_Map', back_populates="user")

    def to_json(self):
        json_user = {
            "id": self.u_id,
            "username": self.username,
            "regi_time": self.regi_time,
            "location": self.location
        }
        return json_user

    @property
    def password(self):
        raise AttributeError("密码不是一个可读的属性")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
