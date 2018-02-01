
from flask import render_template
from src import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'YARIK'}
    return render_template('index.html', user=user)
