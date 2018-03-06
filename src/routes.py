from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from src import app
from src.model.Todo import Todo
from src.model.Goal import Goal
from src.forms import LoginForm
from src.dao.UserDao import UserDao
from src.dao.TodoDao import TodoDao
from src.dao.GoalDao import GoalDao
from injector import Injector, inject
from src.dao.UtilsDao import UtilsDao

injector = Injector()
userDao = injector.get(UserDao)
todoDao = injector.get(TodoDao)
goalDao = injector.get(GoalDao)
utilsDao = injector.get(UtilsDao)


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('index.html')


@app.route('/listTodo')
def listTodo():
    todos = todoDao.getListTodo(10)
    return render_template('listTodo.html', todos=todos)


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


@app.route('/deleteTodo', methods=['POST'])
def deleteTodo():
    todoDao.deleteTodo(10, request.form['id'])
    return 'Ok'


@app.route('/completeTodo', methods=['POST'])
def completeTodo():
    todoDao.completeTodo(10, request.form['id'])
    return 'Ok'


@app.route('/createTodo', methods=['GET', 'POST'])
def createTodo():
    if request.method == 'GET':
        goals = goalDao.getListGoal(10)
        return render_template('createTodo.html', goals=goals)
    else:
        todo = Todo()
        todo.caption = request.form['caption']
        todo.content = request.form['content']
        todo.userId = 10
        todo.goalId = request.form['gId']
        todoId = utilsDao.nextval('todo')
        todo.id = todoId
        todoDao.insertTodo(todo)

        if todo.goalId != 0:
            todoDao.insertGoalTodo(todoId, todo.goalId)

        return "Ok"


@app.route('/createGoal', methods=['GET', 'POST'])
def createGoal():
    if request.method == 'GET':
        return render_template('createGoal.html')
    else:
        goal = Goal()
        goal.caption = request.form['caption']
        goal.reward = request.form['reward']
        goal.user_id = 10
        goalDao.insertGoal(goal)
        return "Ok"


@app.route('/goals', methods=['GET'])
def getGoals():
    goals = goalDao.getListGoal(10)
    return render_template('goals.html', goals=goals)


@app.route('/rewards', methods=['GET'])
def getRewards():
    return render_template('rewards.html')
