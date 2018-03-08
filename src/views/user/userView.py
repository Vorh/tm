from flask import Flask, flash, redirect, render_template, request, session, abort, Blueprint
from src import userDao

user_view = Blueprint('user_view', __name__)


@user_view.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('index.html')


@user_view.route('/login', methods=['GET', 'POST'])
def login():
    password = request.form['password']
    login = request.form['username']

    if userDao.isCorrectLogin(login, password):
        session['logged_in'] = True
    else:
        flash('wrong password')
    return home()


@user_view.route('/logout')
def logout():
    session['logged_in'] = False
    return home()


@user_view.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')
