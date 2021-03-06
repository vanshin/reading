#encoding=utf-8

import logging
import functools
import config
from config import *
logging.basicConfig(level=logging.INFO)

from flask_login import current_user

from models import User, Reading, Sentence, Word
from output import output, output2



def check_user(level):
    """
    确保请求资源的用户是资源的拥有者
    level : 资源类型
    """
    logging.info("the checked type is %s" % level)
    def _(func):
        @functools.wraps(func)
        def __(*args, **kwargs):
            func_id = kwargs.get('id', 0)
            # 验证用户是否登陆
            if current_user.is_anonymous:
                return output(code=RRET.USER_NOT_LOGIN)

            # 验证用户是否是当前登陆用户
            if level == 'user' and current_user.u_id != func_id:
                return output(code=RRET.USER_NOT_SELF)

            # 验证用户是否拥有资源
            if level == 'word':
                word = Word.query.filter_by(w_id=func_id).first()
                if not word:
                    output2(code=RRET.RES_NOT_EXIST)
                user_id = word.user_id
                if user_id == current_user.id:
                    return func(*args, **kwargs)
                else:
                    return output(RRET.RES_NOT_EXIST)
            if level == "sentence":
                sentence = Sentence.query.filter_by(s_id=func_id).first()
                user_id = sentence.user_id
                if user_id == current_user.id:
                    return func(*args, **kwargs)
                else:
                    return output(RRET.RES_NOT_EXIST)
            if level == "reading":
                reading = Reading.query.filter_by(r_id=func_id).first()
                user_ids = [user.user_id for user in reading.users]
                if current_user.u_id in user_ids:
                    return func(*args, **kwargs)
                else:
                    return output(RRET.RES_NOT_EXIST)
        return __
    return _


def check_edit(type):
    def _(func):
        @functools.wraps(func)
        def __(*args, **kwargs):
            reading_json = request.get_json(force=True, silent=True)
            logging.debug('reading_json type=%s' % type(reading_json))
            r_id = reading_json.get('reading_id')
            edit_user_id = kwargs.get('id', 0)
            user_list = Reading.query.filter_by(id=r_id).all()
            if edit_user_id in user_list:
                return func(*args, **kwargs)
            else:
                return output()
        return __
    return _

def check_same_user():
    pass
