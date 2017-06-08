#coding=utf-8

class RRET:
    SUCCESS = 2000
    USER_NOT_LOGIN = 4041
    USER_NOT_EXIST = 4042
    RES_NOT_EXIST = 4043
    USER_NOT_SELF = 4044


MES = {
    2000: 'SUCCESS',
    4041: 'USER_NOT_LOGIN',
    4042: 'USER_NOT_EXIST',
    4043: 'RES_NOT_EXIST',
}



class config:
    SECRET_KEY = '123'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    pass

class DevelopConfig(config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1111@127.0.0.1:3306/readingdev'

class ProductConfig(config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:vanshin1111@127.0.0.1:3306/readingdev'

config = {
    'development':DevelopConfig,
    'product':ProductConfig,
    'default':DevelopConfig
}
