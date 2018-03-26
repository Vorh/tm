from flask import Flask, flash, redirect, render_template, request, session, abort, Blueprint
from flask_login import login_required, current_user
from src import todoDao, userDao, goalDao, rewardDao, utilsDao

from src.model.Todo import Todo
from src.model.Goal import Goal
from src.model.Reward import Reward

route_view = Blueprint('route_view', __name__)


@route_view.route('/deleteTodo', methods=['POST'])
def deleteTodo():
    todoDao.deleteTodo(current_user.id, request.form['id'])
    return 'Ok'


@route_view.route('/completeTodo', methods=['POST'])
def completeTodo():
    todoDao.completeTodo(current_user.id, request.form['id'])
    return 'Ok'


@route_view.route('/createTodo', methods=['GET', 'POST'])
def createTodo():
    if request.method == 'GET':
        goals = goalDao.getListGoal(current_user.id)
        return render_template('create/createTodo.html', goals=goals)
    else:
        todo = Todo()
        todo.caption = request.form['caption']
        todo.content = request.form['content']
        todo.userId = current_user.id
        todo.goalId = request.form['gId']
        todoId = utilsDao.nextval('todo')
        todo.id = todoId
        todoDao.insertTodo(todo)

        if todo.goalId != 0:
            todoDao.insertGoalTodo(todoId, todo.goalId)

        return "Ok"


@route_view.route('/todos')
@login_required
def getTodos():
    todos = todoDao.getListTodo(current_user.id)
    return render_template('items/todos.html', todos=todos)


@route_view.route('/index')
def index():
    return getTodos()


@route_view.route('/goals', methods=['GET'])
def getGoals():
    goals = goalDao.getListGoal(current_user.id)
    return render_template('items/goals.html', goals=goals)


@route_view.route('/createGoal', methods=['GET', 'POST'])
def createGoal():
    if request.method == 'GET':
        rewards = rewardDao.getRewards(current_user.id)
        return render_template('create/createGoal.html', rewards=rewards)
    else:
        goal = Goal()
        goal.caption = request.form['caption']
        goal.user_id = current_user.id
        goal.reward = request.form['rewardId']
        goalDao.insertGoal(goal)
        return "Ok"


@route_view.route('/rewards', methods=['GET'])
def getRewards():
    rewards = rewardDao.getRewards(current_user.id)
    return render_template('items/rewards.html', rewards=rewards)


@route_view.route('/createReward', methods=['GET', 'POST'])
def createReward():
    if request.method == 'GET':
        return render_template('create/createReward.html')
    else:

        reward = Reward()
        reward.caption = request.form['caption']
        reward.reward = request.form['reward']
        reward.user_id = current_user.id
        rewardDao.insertReward(reward)

    return 'OK'


@route_view.route('/deleteReward', methods=['POST'])
def deleteReward():
    rewardDao.deleteReward(current_user.id, request.form['id'])
    return 'Ok'
