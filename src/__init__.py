from flask import Flask, request
from config import Config
import os
from src.views.userView import user_view
from src.views.routesView import route_view

app = Flask(__name__)
app.config.from_object(Config)

mainDao = DataSource()
userDao = UserDao(mainDao)
todoDao = TodoDao(mainDao)
goalDao = GoalDao(mainDao)
utilsDao = UtilsDao(mainDao)


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


app.register_blueprint(user_view)
app.register_blueprint(route_view)
