#coding=utf-8

import sys
import os

from app import create_app, db
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from app.models import Reading, Sentence, Word, Word_Note, Sentence_Note, User

reload(sys)
sys.setdefaultencoding("utf-8")

app = create_app('default')
manager = Manager(app)
migrate = Migrate(app, db)
def make_shell_context():
    """ 设置上下文 """
    return dict(db=db, app=app, Sentence=Sentence,
                Reading=Reading, Word=Word, User=User,
                Word_Note=Word_Note, Sentence_Note=Sentence_Note)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
    
