# coding=utf-8
from flask_wtf import Form
from ..models import User
from wtforms import TextAreaField, SubmitField, StringField, PasswordField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError


class LoginForm(Form):
    """ 用户 """
    username = StringField('用户名', validators=[Required()])
    password = PasswordField('密码', validators=[Required()])
    submit = SubmitField('提交')


class RegiForm(Form):
    username = StringField('用户名', validators=[Required(),
                                              Length(1, 64),
                                              Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                     '用户名必须只有字母，数字，点或者下划线')])
    password = PasswordField('密码', validators=[Required(), EqualTo('password2', message='密码必须相同')])
    password2 = PasswordField('再次输入密码', validators=[Required()])
    submit = SubmitField('注册')

    def validata_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('此用户名已经注册')
