from flask import Flask, flash, redirect, render_template, request, session, abort, Blueprint
from src import todoDao, userDao, goalDao, rewardDao

from src.model.Todo import Todo
from src.model.Goal import Goal
from src.model.Reward import Reward

route_view = Blueprint('route_view', __name__)


@route_view.route('/deleteTodo', methods=['POST'])
def deleteTodo():
    todoDao.deleteTodo(10, request.form['id'])
    return 'Ok'


@route_view.route('/completeTodo', methods=['POST'])
def completeTodo():
    todoDao.completeTodo(10, request.form['id'])
    return 'Ok'


@route_view.route('/createTodo', methods=['GET', 'POST'])
def createTodo():
    if request.method == 'GET':
        goals = goalDao.getListGoal(10)
        return render_template('create/createTodo.html', goals=goals)
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


@route_view.route('/todos')
def getTodos():
    todos = todoDao.getListTodo(10)
    return render_template('items/todos.html', todos=todos)


@route_view.route('/goals', methods=['GET'])
def getGoals():
    goals = goalDao.getListGoal(10)
    return render_template('items/goals.html', goals=goals)


@route_view.route('/createGoal', methods=['GET', 'POST'])
def createGoal():
    if request.method == 'GET':
        return render_template('create/createGoal.html')
    else:
        goal = Goal()
        goal.caption = request.form['caption']
        goal.reward = request.form['reward']
        goal.user_id = 10
        goalDao.insertGoal(goal)
        return "Ok"


@route_view.route('/rewards', methods=['GET'])
def getRewards():
    rewards = rewardDao.getRewards(10)
    return render_template('items/rewards.html', rewards=rewards)


@route_view.route('/createReward', methods=['GET', 'POST'])
def createReward():
    if request.method == 'GET':
        return render_template('create/createReward.html')
    else:

        reward = Reward()
        reward.caption = request.form['caption']
        reward.reward = request.form['reward']
        reward.user_id = 10
        rewardDao.insertReward(reward)

    return 'OK'


@route_view.route('/deleteReward', methods=['POST'])
def deleteReward():
    rewardDao.deleteReward(10, request.form['id'])
    return 'Ok'
