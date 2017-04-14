#endcoding=utf-8

import logging
import functools
logging.basicConfig(level=logging.INFO)

from flask_login import current_user
from models import User, Reading, Sentence, Word
from output import output


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
            logging.info("request_id is %d" % func_id)
            logging.info("current_user is %s" % current_user.id)
            if level == "word":
                word = Word.query.filter_by(id=func_id).first()
                user_id = word.user_id
                if user_id == current_user.id:
                    return func(*args, **kwargs)
                else:
                    return output()
            if level == "sentence":
                sentence = Sentence.query.filter_by(id=func_id).first()
                user_id = sentence.user_id
                if user_id == current_user.id:
                    return func(args, **kwargs)
                else:
                    return output()
            if level == "reading":
                reading = Reading.query.filter_by(id=func_id).first()
                user_id = reading.user_id
                if user_id == current_user.id:
                    return func(*args, **kwargs)
                else:
                    return output()
        return __
    return _




def check_same_user():
    pass