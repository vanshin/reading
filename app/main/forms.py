#coding=utf-8
from flask_wtf import Form
from wtforms import TextAreaField,SubmitField,StringField
from wtforms.validators import Required,Length

class readingForm(Form):
    reading_order = StringField('序列',validators=[Required()])
    reading_name = StringField('标题',validators=[Required()])
    reading_body = TextAreaField('阅读理解')
    submit = SubmitField('提交')
class controlForm(Form):
    word = StringField('单词')
    phrase = TextAreaField('短语')
    grammar_c = TextAreaField('词法')
    grammar_j = TextAreaField('句法')
    translation = TextAreaField('翻译')
    comment = TextAreaField('评论')
    submit = SubmitField('提交')