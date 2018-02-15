from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from src import app
from src.forms import LoginForm
from src.dao.UserDao import UserDao
from src.dao.TodoDao import TodoDao
from injector import Injector, inject

injector = Injector()
userDao = injector.get(UserDao)
todoDao = injector.get(TodoDao)


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('index.html')


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

    todos = todoDao.getListTodo(10)

    print(todos)
    return render_template('index.html', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    password = request.form['password']
    login = request.form['username']

    if userDao.isCorrectLogin(login, password):
        session['logged_in'] = True
    else:
        flash('wrong password')
    return home()
    # return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    session['logged_in'] = False
    return home()


@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')
