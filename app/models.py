#coding=utf-8
from . import db
from datetime import datetime

class Reading(db.Model):
    __tablename__ = 'readings'
    id = db.Column(db.Integer,primary_key=True)
    reading_order = db.Column(db.Text)
    reading_name = db.Column(db.String(64))
    reading_body = db.Column(db.Text)
    sentences = db.relationship('Sentence',backref='reading',lazy='dynamic')
    
    def __repf__(self):
        return '<Reading %r>' % self.reading_name

    def to_json(self):
        json_reading = {
            'id':self.id,
            'reading_order':self.reading_order,
            'reading_name':self.reading_name,
            'reading_body':self.reading_body

        }
        return json_reading

class Sentence(db.Model):
    __tablename__ = 'sentences'
    id = db.Column(db.Integer,primary_key=True)
    reading_id = db.Column(db.Integer,db.ForeignKey('readings.id'))
    sentence_body = db.Column(db.Text)
    # words = db.relationship('Word',backref='sentence')
    # 短语
    phrase = db.Column(db.Text)
    grammar_c = db.Column(db.Text)
    grammar_j = db.Column(db.Text)
    translation = db.Column(db.Text)
    comment = db.Column(db.Text)
    def __repf__(self):
        return '<Sentence %d>' % self.id


# class Word(db.Model):
#     __tablename__ = 'words'
#     id = db.Column(db.Integer,primary_key=True)
#     sentence_id = db.Column(db.Integer,db.ForeignKey('sentences.id')
#     word_body = db.Column(db.String(64))
#     def __repf__(self):
#         return '<Word %d>' self.id
    