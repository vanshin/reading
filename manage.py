#coding=utf-8
from app import create_app,db
from flask_script import Manager,Shell
from flask_migrate import Migrate,MigrateCommand
from app.models import Reading,Sentence

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

app = create_app('default')
manager = Manager(app)
migrate = Migrate(app)
def make_shell_context():
    return dict(db=db,app=app,Sentence=Sentence,Reading=Reading)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()