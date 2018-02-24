import pymysql
from injector import inject
from src.dao.mainDao import DataSource
from src.model.Goal import Goal
from src.model.Todo import Todo


class GoalDao:

    @inject
    def __init__(self, dataSources: DataSource):
        self.ds = dataSources

    def getListGoal(self, userId):
        sql = """
              SELECT g.caption AS gCaption,
              g.id as gId,
              g.crete_date as gDate,
              t.*
              FROM goal g INNER JOIN goal_todo todo ON g.id = todo.goal_id
              INNER JOIN todo t ON todo.todo_id = t.id
              where g.user_id = %s
              """ % userId

        cur = self.ds.execute(sql)

        result = cur.fetchall()

        goals = {}
        for row in result:
            gId = row['gId']

            todo = Todo()
            todo.id = row['id']
            todo.content = row['content']
            todo.caption = row['caption']
            todo.complete = row['complete']
            todo.date = row['date']

            if gId in goals:
                goals[gId].listTodo.append(todo)
            else:
                goal = Goal()
                goal.caption = row['gCaption']
                goal.create_date = row['gDate']
                goal.id = gId
                goal.listTodo.append(todo)
                goals[gId] = goal

        listGoals = []
        for goal in goals:
            listGoals.append(goals[goal])

        print('Goals size : %s' % len(listGoals))
        return listGoals
