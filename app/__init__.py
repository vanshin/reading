#coding=utf-8
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()
bootstrap = Bootstrap()
moment = Moment()
login_manager = LoginManager()


#login_required fail return 
login_manager.login_view = 'auth.login'
login_manager.session_protection = 'strong'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    # 初始化组件
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    moment.init_app(app)
    # 蓝图
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .user import user as user_blueprint
    app.register_blueprint(user_blueprint)

    from .share import share as share_blueprint
    app.register_blueprint(share_blueprint)

    from .edit import edit as edit_blueprint
    app.register_blueprint(edit_blueprint)

    from .show import show as show_blueprint
    app.register_blueprint(show_blueprint)

    return app
