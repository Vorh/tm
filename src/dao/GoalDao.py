import pymysql
from src.dao.mainDao import DataSource
from src.dao.TodoDao import TodoDao
from src.dao.RewardDao import RewardDao
from src.model.Goal import Goal
from src.model.Todo import Todo
from src import app


class GoalDao:

    def __init__(self, dataSources: DataSource):
        self.ds = dataSources
        self.rewardDao = None
        self.todoDao = None

    def insertGoal(self, goal: Goal):
        sql = """INSERT INTO goal (caption, reward, user_id) VALUE
  ('%s','%s',%s)""" % (goal.caption, goal.reward, goal.user_id)
        self.ds.execute(sql)

        app.logger.info('%s Insert goal %s' % (goal.user_id, goal.caption))

    def getListGoal(self, userId):
        sql = """ select * from goal where user_id = '%s'; """ % userId

        cur = self.ds.execute(sql)

        result = cur.fetchall()

        goals = {}
        listGoalsIds = []
        listRewardsIds = []
        for row in result:
            gId = row['id']
            goal = Goal()
            goal.caption = row['caption']
            goal.create_date = row['create_date']
            goal.id = gId
            goal.reward = row['reward']
            goals[gId] = goal
            listGoalsIds.append(gId)
            listRewardsIds.append(goal.reward)

        for todo in self.todoDao.getListByGoals(listGoalsIds):
            goals[todo.goalId].listTodo.append(todo)

        rewardMap = self.rewardDao.getRewardByIds(listRewardsIds)

        for goal in goals.values():
            goal.reward = rewardMap[goal.reward]


        app.logger.info('%s Get goals , size: %s' % (userId, len(goals)))

        return goals.values()

    def setTodoDao(self, todoDao: TodoDao):
        self.todoDao = todoDao

    def setRewardDao(self, rewardDao: RewardDao):
        self.rewardDao = rewardDao
