from flask import Flask, Config
from config import Config
import pymysql


app = Flask(__name__)
app.config.from_object(Config)



from src import routes
