from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from src import app
from src.forms import LoginForm
from src.dao import UserDao
from injector import Injector, inject

injector = Injector()
userDao = injector.get(UserDao)




@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return 'Hello boss'

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
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password')
    return home()
    # return render_template('login.html', title='Sign In', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')
