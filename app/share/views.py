# coding=utf-8

import json
import logging
logging.basicConfig(level=logging.INFO)

from . import share
from flask import render_template, jsonify, request
from flask_login import current_user, login_required
from ..output import output
from ..decorator import check_user
from ..models import (
    Reading, Sentence, Sentence_Note,
    Word, Word_Note, User, User_Reading_Map
)
from .. import db

@share.route('/user/<int:id>/edit_list', methods=['POST'])
def post_edit_list(id):
    """ 分享文章给其他用户 """
    # 根据reading id和user id存入数据库
    reading_json = request.get_json(force=True, silent=True)
    r_id = reading_json.get('reading_id', 0)
    reading_id = Reading.query.filter_by(r_id=r_id).first().id
    user = User.query.filter_by(u_id=id).first()
    user_id = user.id
    ur_map = User_Reading_Map(reading_id=reading_id, user_id=user_id)
    db.session.add(ur_map)
    return output(user)