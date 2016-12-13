#coding=utf-8
from . import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash



class Reading(db.Model):
    __tablename__ = 'readings'
    id = db.Column(db.Integer, primary_key=True)
    reading_order = db.Column(db.Text)
    reading_name = db.Column(db.String(64))
    reading_body = db.Column(db.Text)
    editors = db.Column(db.String(64))
    sentences = db.relationship('Sentence', backref='reading', lazy='dynamic')

    def __repf__(self):
        return '<Reading %r>' % self.reading_name

    def to_json(self):
        json_reading = {
            'id': self.id,
            'reading_order': self.reading_order,
            'reading_name': self.reading_name,
            'reading_body': self.reading_body,
            'reading_sentences': {x.id: x.sentence_body for x in self.sentences}
            # 'reading_sentences':[x.sentence_body for x in self.sentences]
        }
        return json_reading


class Sentence(db.Model):
    __tablename__ = 'sentences'
    id = db.Column(db.Integer, primary_key=True)
    reading_id = db.Column(db.Integer, db.ForeignKey('readings.id'))
    words = db.relationship('Word', backref='sentence', lazy='dynamic')
    sentence_notes = db.relationship('Sentence_Note', backref='sentence', lazy='dynamic')
    sentence_body = db.Column(db.Text)
    comment = db.Column(db.Text)

    def __repf__(self):
        return '<Sentence %d>' % self.id

    def to_json(self):
        """ return json data """
        json_sentence = {
            'id': self.id,
            'sentence_body': self.sentence_body
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
    sentence_id = db.Column(db.Integer, db.ForeignKey('sentences.id'))
    phrase = db.Column(db.Text)
    grammar = db.Column(db.Text)
    translation = db.Column(db.Text)

    def to_json(self):
        """ 生成json数据 """
        json_sentence_note = {
            'phrase': self.phrase,
            'grammer': self.grammar,
            'translation': self.translation 
        }
        return json_sentence_note

class Word(db.Model):
    """ word model """
    __tablename__ = 'words'
    id = db.Column(db.Integer, primary_key=True)
    sentence_id = db.Column(db.Integer, db.ForeignKey('sentences.id'))
    word_note = db.relationship('Word_Note', backref='word', lazy='dynamic', uselist='False')
    word_body = db.Column(db.String(32))

    def to_json(self):
        """ 返回单词 """
        json_word = {
            "id": self.id,
            "word_body": self.word_body
        }

class Word_Note(db.Model):
    """ word_note model """
    __tablename__ = 'word_notes'
    id = db.Column(db.Integer, primary_key=True)
    word_id = db.Column(db.Integer, db.ForeignKey('words.id'))
    Chinese = db.Column(db.String(64))
    Phonogram = db.Column(db.String(32))
    

class User(db.Model, UserMixin):
    """ user model """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer)
    username = db.Column(db.String(64), index=True)
    password_hash = db.Column(db.String(128))
    regi_time = db.Column(db.DateTime(), default=datetime.utcnow)
    avatar_hash = db.Column(db.String(64))
    location = db.Column(db.String(64))

    def to_json(self):
        json_user = {
            "id": self.id,
            "userid": self.userid,
            "username": self.username,
            "regi_time": self.regi_time,
            "location": self.location
        }

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



# class Word(db.Model):
#     __tablename__ = 'words'
#     id = db.Column(db.Integer,primary_key=True)
#     sentence_id = db.Column(db.Integer,db.ForeignKey('sentences.id')
#     word_body = db.Column(db.String(64))
#     def __repf__(self):
#         return '<Word %d>' self.id
