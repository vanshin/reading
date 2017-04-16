# coding=utf-8

import json
import logging
logging.basicConfig(level=logging.INFO)

from . import share
from flask import render_template, jsonify, request
from flask_login import current_user, login_required
from ..output import output
from ..decorator import check_user
from ..models import Reading, Sentence, Sentence_Note, Word, Word_Note, User
from .. import db

@share.route('/user/<int:id>/edit_list', methods=['POST'])
def post_edit_list(id):
    """
    分享文章给其他用户
    """
    # 根据reading id和user id存入数据库
    # reading_json = request.get_json(force=True, silent=True)
    # r_id = reading_json.get('reading_id')
    # user = Edit_User(e_userid=id, reading_id=r_id)
    # db.session.add(user)
    # db.session.commit()
    # return output(user)
    pass