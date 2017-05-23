#coding=utf-8

import random

from flask import render_template, redirect, request, url_for, flash, jsonify
from flask_login import login_user, login_required, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from . import auth
from .forms import LoginForm, RegiForm
from ..models import User
from .. import db
from ..reading import get_random

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for('main.index'))
        flash('错误的用户名或者密码')
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('已经注销登录')
    return redirect(url_for('main.index'))

@auth.route('/regi', methods=['GET', 'POST'])
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
            return redirect(url_for('auth.login'))
        else:
            flash("密码相同")
    return render_template('auth/regi.html', form=form)























# @auth.route('/session/new', methods=['GET'])
# def regi_form():
#     """ 获取注册页面 """
#     return render_template('auth/regi.html')


# @auth.route('/users/new' ,methods=['GET'])
# def login_form():
#     """ 获取用户登录页面 """
#     return render_template('/auth/login.html')

# @auth.route('/user', methods=['POST'])
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

# @auth.route('/session', methods=['POST'])
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

# @auth.route('/session', methods=['DELETE'])
# def logout():
#     """" logout view """
#     userinfo = request.get_json(silent='True')
#     user = User.query.filter_by(email=userinfo.get("email")).first()
#     if user is not None:
#         logout_user(user)
#         return {
#             "code": 204
#         }

# @auth.route('/users/<int:id>', methods=['GET'])
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
