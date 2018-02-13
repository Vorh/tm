from flask import Flask, Config
from config import Config
import pymysql
from src.dao import UserDao, DataSource


app = Flask(__name__)
app.config.from_object(Config)



from src import routes
