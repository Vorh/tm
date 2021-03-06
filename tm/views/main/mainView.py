from flask import Flask, flash, redirect, render_template, request, session, abort, Blueprint
from flask_login import login_required, current_user
from tm.models import User, Todo, Goal, Reward
import json


route_view = Blueprint('route_view', __name__)


@route_view.route('/deleteTodo', methods=['POST'])
@login_required
def deleteTodo():
    # todoDao.deleteTodo(current_user.id, request.form['id'])
    return 'Ok'


@route_view.route('/completeTodo', methods=['POST'])
@login_required
def completeTodo():
    # todoDao.completeTodo(current_user.id, request.form['id'])
    return 'Ok'


@route_view.route('/createTodo', methods=['GET', 'POST'])
@login_required
def createTodo():
    if request.method == 'GET':
        # goals = goalDao.getListGoal(current_user.id)
        goal = None
        return render_template('create/createTodo.html', goals=goals)
    else:
        todo = Todo()
        todo.caption = request.form['caption']
        todo.content = request.form['content']
        todo.userId = current_user.id
        todo.goalId = request.form['gId']
        todoId = utilsDao.nextval('todo')
        todo.id = todoId
        # todoDao.insertTodo(todo)

        # if todo.goalId != 0:
        # todoDao.insertGoalTodo(todoId, todo.goalId)

        return "Ok"


@route_view.route('/todos')
@login_required
def getTodos():
    todos = Todo.query.filter_by(user_id=current_user.id).all()
    countTodo = sum(True == todo.complete for todo in todos)

    return render_template('items/todos.html', todos=todos, countTodo=countTodo)


@route_view.route('/index')
@login_required
def index():
    return getTodos()


@route_view.route('/goals', methods=['GET'])
@login_required
def getGoals():
    goals = Goal.query.filter_by(user_id=current_user.id)
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
        if int(rewardId) == 0:
            rewardError = True

        if captionError | rewardError:
            return json.dumps({'captionError': captionError, 'rewardError': rewardError})

        if not rewardDao.userIsOwnReward(current_user.id, rewardId):
            return json.dumps({'userOwnError': True})

        goal = Goal()
        goal.caption = caption
        goal.user_id = current_user.id
        goal.reward = rewardId
        goalDao.insertGoal(goal)
        return "OK"


@route_view.route('/rewards', methods=['GET'])
@login_required
def getRewards():
    rewards = Reward.query.filter_by(user_id=current_user.id)
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
    id = request.form['id']

    if rewardDao.rewardIsTied(id):
        return json.dumps({'rewardIsTied': True})

    rewardDao.deleteReward(current_user.id, id)
    return json.dumps({'result': 'Ok'})
