#coding=utf-8
class config:
    SECRET_KEY = '123'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    pass

class DevelopConfig(config):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:0000@127.0.0.1:3306/readingdev'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:vanshin1111@127.0.0.1:3306/readingdev'
    

config = {
    'development':DevelopConfig,
    'default':DevelopConfig
}
