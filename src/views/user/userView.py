from flask import Flask, flash, url_for, redirect, render_template, request, session, abort, Blueprint
from flask_login import login_user, logout_user, current_user, login_required
from src import userDao

user_view = Blueprint('user_view', __name__)


@user_view.route('/')
@login_required
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('index.html')


@user_view.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    password = request.form['password']
    login = request.form['username']

    user = userDao.getUser(login, password)

    if user is None:
        return redirect(url_for('user_view.login'))

    login_user(user)

    return redirect(request.args.get('next') or url_for('route_view.index'))


@user_view.route('/logout')
def logout():
    session['logged_in'] = False
    return home()


@user_view.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')
