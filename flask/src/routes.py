from flask import render_template
from src import app
from src.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'YARIK'}

    posts = [
        {
            'author': {'username': 'Arik'},
            'body': 'Test'
        },
        {
            'author': {'username': 'Test'},
            'body': 'Max'
        }
    ]
    return render_template('index.html', user=user, posts=posts)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
