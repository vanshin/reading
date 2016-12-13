#coding=utf-8

import random

from flask import render_template, redirect, request, url_for, flash, jsonify
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from . import auth
from .forms import userForm
from ..models import User
from .. import db


@auth.route('/session/new', methods=['GET'])
def regi_form():
    """ regi_form """
    return render_template('auth/regi.html')


@auth.route('/users/new' ,methods=['GET'])
def login_form():
    """ 获取用户登录页面 """
    return render_template('/auth/login.html')

@auth.route('/user', methods=['POST'])
def regi():
    """ 用户注册 """
    userid = random.randint(000000, 999999)
    userinfo = request.get_json(silent='True')
    username = userinfo.get("username")
    password = userinfo.get("password")
    password2 = userinfo.get("password2")
    if password == password2:
        user = User(userid=userid, username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return render_template('auth/login.html')
    else:
        flash("password is not same")
        return render_template('auth/regi.html')

@auth.route('/session', methods=['POST'])
def login():
    """ login view """
    userinfo = request.get_json(silent='True')
    user = User.query.filter_by(email=userinfo.get("email")).first()
    if user is not None and user.verify_password(userinfo.get("password")):
        login_user(user)
        return {
            "code": 201,
            "data": jsonify(user.to_json()),
            "location": url_for('auth.get_user', id=user.id, _external=True)
        }
    else:
        return {
            "code": 400,
            "data": "invaild username or password",

        }

@auth.route('/session', methods=['DELETE'])
def logout():
    """" logout view """
    userinfo = request.get_json(silent='True')
    user = User.query.filter_by(email=userinfo.get("email")).first()
    if user is not None:
        logout_user(user)
        return {
            "code": 204
        }

@auth.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    """ get user view """
    user = User.query.filter_by(id=id).first()
    if user is not None:
        return {
            "code": 200,
            "data": jsonify(user.to_json())
        }
    else:
        return {
            "code": 404,
            "data": "NOT FOUND"
        }

# @auth.route('/users/<int:id>', methods=['POST'])
# def update_user(id):
#     user = User.query.filter_by(id=id).first()
#     user_info = request.get_json(siltent=True)
    