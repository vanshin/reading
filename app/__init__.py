#coding=utf-8
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from config import config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
bootstrap = Bootstrap()
moment = Moment()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    # 初始化组件
    bootstrap.init_app(app)
    db.init_app(app)
    moment.init_app(app)
    # 蓝图
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app
