from flask import Flask, flash, redirect, render_template, request, session, abort, Blueprint
from flask_login import login_required, current_user
from src import todoDao, userDao, goalDao, rewardDao, utilsDao
import json

from src.model.Todo import Todo
from src.model.Goal import Goal
from src.model.Reward import Reward

route_view = Blueprint('route_view', __name__)


@route_view.route('/deleteTodo', methods=['POST'])
@login_required
def deleteTodo():
    todoDao.deleteTodo(current_user.id, request.form['id'])
    return 'Ok'


@route_view.route('/completeTodo', methods=['POST'])
@login_required
def completeTodo():
    todoDao.completeTodo(current_user.id, request.form['id'])
    return 'Ok'


@route_view.route('/createTodo', methods=['GET', 'POST'])
@login_required
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
@login_required
def index():
    return getTodos()


@route_view.route('/goals', methods=['GET'])
@login_required
def getGoals():
    goals = goalDao.getListGoal(current_user.id)
    return render_template('items/goals.html', goals=goals)


@route_view.route('/createGoal', methods=['GET', 'POST'])
@login_required
def createGoal():
    if request.method == 'GET':
        rewards = rewardDao.getRewards(current_user.id)
        return render_template('create/createGoal.html', rewards=rewards)
    else:

        caption = request.form['caption']
        rewardId = request.form['rewardId']

        captionError = False
        rewardError = False
        if not caption:
            captionError = True
        if rewardId == 0:
            rewardError = True

        if captionError | rewardError:
            return json.dumps({'captionError': captionError, 'rewardError': rewardError})

        if not rewardDao.userIsOwnReward(current_user.id, rewardId):
            return json.dump('userOwnError', True)

        goal = Goal()
        goal.caption = caption
        goal.user_id = current_user.id
        goal.reward = rewardId
        goalDao.insertGoal(goal)
        return "OK"


@route_view.route('/rewards', methods=['GET'])
@login_required
def getRewards():
    rewards = rewardDao.getRewards(current_user.id)
    return render_template('items/rewards.html', rewards=rewards)


@route_view.route('/createReward', methods=['GET', 'POST'])
@login_required
def createReward():
    if request.method == 'GET':
        return render_template('create/createReward.html')
    else:

        caption = request.form['caption']
        reward = request.form['reward']

        captionError = False
        rewardError = False
        if not caption:
            captionError = True
        if not reward:
            rewardError = True

        if captionError | rewardError:
            return json.dumps({'captionError': captionError, 'rewardError': rewardError})

        reward = Reward()
        reward.caption = request.form['caption']
        reward.reward = request.form['reward']
        reward.user_id = current_user.id
        rewardDao.insertReward(reward)

    return 'OK'


@route_view.route('/deleteReward', methods=['POST'])
@login_required
def deleteReward():
    rewardDao.deleteReward(current_user.id, request.form['id'])
    return 'Ok'
