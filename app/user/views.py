#coding=utf-8

import random
import logging
logging.basicConfig(level=logging.INFO)

from flask import render_template, redirect, request, url_for, flash, jsonify
from flask_login import login_user, login_required, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from .. output import output
from . import user
from ..models import User
from .. import db
from ..reading import get_random
from forms import LoginForm, RegiForm
from config import RRET

@user.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for('main.index'))
        flash('错误的用户名或者密码')
    return render_template('auth/login.html', form=form)

@user.route('/logout')
@login_required
def logout():
    logout_user()
    flash('已经注销登录')
    return redirect(url_for('main.index'))

@user.route('/regi', methods=['GET', 'POST'])
def regi():
    form = RegiForm()
    if form.validate_on_submit():
        # 先假设不会重复
        username = form.username.data
        if not username:
            flash("用户名未填写")
            return render_template('auth/regi.html', form=form)

        password = form.password.data
        password2 = form.password2.data
        if password == password2:
            user = User(username=username,
                        password=password,
                        u_id=get_random())
            db.session.add(user)
            db.session.commit()
            flash("注册成功")
            return redirect(url_for('user.login'))
        else:
            flash("密码相同")
    return render_template('auth/regi.html', form=form)




@user.route('/current_user/id', methods=['GET'])
@login_required
def get_user_id():
    """ 获取当前用户的ID """
    logging.info("current_user is %s" % current_user    )
    if current_user.is_anonymous:
        return output(RRET.USER_NOT_LOGIN)
    info = dict(id=current_user.u_id)
    return output(RRET.SUCCESS, data=info)


@user.route('/user/<int:id>/sentences', methods=['GET'])
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

@user.route('/user/<int:id>/words', methods=['GET'])
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

















# @user.route('/session/new', methods=['GET'])
# def regi_form():
#     """ 获取注册页面 """
#     return render_template('auth/regi.html')


# @user.route('/users/new' ,methods=['GET'])
# def login_form():
#     """ 获取用户登录页面 """
#     return render_template('/auth/login.html')

# @user.route('/user', methods=['POST'])
# def regi():
#     """ 用户注册 """
#     userid = random.randint(000000, 999999)
#     userinfo = request.get_json(silent='True')
#     username = userinfo.get("username")
#     password = userinfo.get("password")
#     password2 = userinfo.get("password2")
#     if password == password2:
#         user = User(userid=userid, username=username, password=password)
#         db.session.add(user)
#         db.session.commit()
#         return render_template('auth/login.html')
#     else:
#         flash("password is not same")
#         return render_template('auth/regi.html')

# @user.route('/session', methods=['POST'])
# def login():
#     """ login view """
#     userinfo = request.get_json(silent='True')
#     user = User.query.filter_by(email=userinfo.get("email")).first()
#     if user is not None and user.verify_password(userinfo.get("password")):
#         login_user(user)
#         return {
#             "code": 201,
#             "data": jsonify(user.to_json()),
#             "location": url_for('auth.get_user', id=user.id, _external=True)
#         }
#     else:
#         return {
#             "code": 400,
#             "data": "invaild username or password",

#         }

# @user.route('/session', methods=['DELETE'])
# def logout():
#     """" logout view """
#     userinfo = request.get_json(silent='True')
#     user = User.query.filter_by(email=userinfo.get("email")).first()
#     if user is not None:
#         logout_user(user)
#         return {
#             "code": 204
#         }

# @user.route('/users/<int:id>', methods=['GET'])
# def get_user(id):
#     """ get user view """
#     user = User.query.filter_by(id=id).first()
#     if user is not None:
#         return {
#             "code": 200,
#             "data": jsonify(user.to_json())
#         }
#     else:
#         return {
#             "code": 404,
#             "data": "NOT FOUND"
#         }
