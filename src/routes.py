from flask import render_template, flash, redirect, url_for
from src import app
from src.forms import LoginForm
from src.dao import UserDao
from injector import Injector, inject

injector = Injector()
userDao = injector.get(UserDao)




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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')
