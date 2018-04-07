import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'test'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/tm'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
