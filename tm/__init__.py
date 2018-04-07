from flask import Flask, request
from config import Config
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
loginManager = LoginManager(app)
loginManager.init_app(app)
loginManager.login_view = 'user_view.login'





@app.url_defaults
def hashed_static_file(endpoint, values):
    if 'static' == endpoint or endpoint.endswith('.static'):
        filename = values.get('filename')
        if filename:
            blueprint = request.blueprint
            if '.' in endpoint:
                blueprint = endpoint.rsplit('.', 1)[0]

            static_folder = app.static_folder
            if blueprint and app.blueprints[blueprint].static_folder:
                static_folder = app.blueprints[blueprint].static_folder

            fp = os.path.join(static_folder, filename)
            if os.path.exists(fp):
                values['_'] = int(os.stat(fp).st_mtime)

# @loginManager.user_loader
# def load_user(id):
#     return userDao.getUserById(id)

# from tm.views.user.userView import user_view
# from tm.views.main.mainView import route_view
#
# app.register_blueprint(user_view)
# app.register_blueprint(route_view)
