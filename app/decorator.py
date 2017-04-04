#endcodin=utf-8

from flask_login import current_user
from models import User, Reading, Sentence, Word
from output import output
 

def check_login(level):
    def _(func):
        def wrapper(*args, **kwargs):
            id = args[0]
            if level == "word":
                check_word(id)
            return wrapper
            # user.id ? current_user.id
    return _

def check_word(id):
    word = Word.query.filter_by(id)
    user_id = word.user_id
    if user_id == current_user:
        return func(*args, **kwargs)
    else:
        output()

def check_same_user():
    pass