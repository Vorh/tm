from flask import Flask, Config
from config import Config
from flask_injector import FlaskInjector
from injector import inject
import pymysql
from src.dao import UserDao


app = Flask(__name__)
app.config.from_object(Config)


def configure(binder):
    db = pymysql.connect('localhost', 'root', 'root', 'tm')
    cursor = db.cursor()
    print(cursor)
    userDao = UserDao(cursor)
    binder.bind(
        UserDao,
        to=userDao,
        scope=singleton,
    )


FlaskInjector(app=app, modules=[configure])

from src import routes
