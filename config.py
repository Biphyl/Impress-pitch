import os


class Config():
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://biron:Biron4745@localhost/impress'


class ProdConfig(Config):



class DevConfig(Config):
    DEBUG = True


