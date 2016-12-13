#coding=utf-8
from flask_wtf import Form
from wtforms import TextAreaField,SubmitField,StringField
from wtforms.validators import Required,Length

class userForm(Form):
    username = StringField('用户名', validators=[Required()])
    password = StringField('密码', validators=[Required()])
    password2 = StringField('验证密码', validators=[Required()])
    submit = SubmitField('提交')
