class config:
    SECRET_KEY = '123'
    pass

class DevelopConfig(config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:0000@127.0.0.1:3306/readingdev'

config = {
    'development':DevelopConfig,
    'default':DevelopConfig
}