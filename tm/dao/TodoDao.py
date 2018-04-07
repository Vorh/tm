import pymysql
from tm.dao.mainDao import DataSource
from tm.dao.UtilsDao import UtilsDao
from tm.model.Todo import Todo


class TodoDao:

    def __init__(self, dataSource: DataSource):
        self.ds = dataSource

    def getListTodo(self, userId):
        print('Get todos for user %s' % userId)
        sql = "select * from todo where user_id = '%s' ORDER by date DESC" % userId
        cur = self.ds.execute(sql)
        result = cur.fetchall()

        todos = []
        for row in result:
            todos.append(TodoDao.todoRowMapper(row))

        return todos

    def getListByGoals(self, goalIds):
        sql = """select t.*,gt.goal_id as gId from todo t INNER JOIN goal_todo gt on t.id = gt.todo_id
where goal_id in (%s);""" % UtilsDao.toSqlList(goalIds)

        todos = []
        for row in self.ds.execute(sql).fetchall():
            todo = TodoDao.todoRowMapper(row)
            todo.goalId = row['gId']
            todos.append(todo)

        return todos

    def insertTodo(self, todo):
        sql = "insert into todo (content, date,  user_id, caption) " \
              " values ('%s',now(),%s,'%s')" % (todo.content, todo.userId, todo.caption)
        self.ds.execute(sql)

    def insertGoalTodo(self, todoId, goalId):
        sql = """INSERT into goal_todo (goal_id, todo_id) VALUE (%s,%s);
              """ % (goalId, todoId)
        self.ds.execute(sql)

    def deleteTodo(self, userId, todoId):
        sql = "delete from goal_todo where todo_id = %s" % todoId
        self.ds.execute(sql)
        sql = "delete from todo where id = %s and user_id = %s" % \
              (todoId, userId)
        self.ds.execute(sql)

    def completeTodo(self, userId, todoId):
        sql = "update todo set complete = true where id = %s and user_id = %s " % \
              (todoId, userId)
        self.ds.execute(sql)

    @staticmethod
    def todoRowMapper(row):
        todo = Todo()
        todo.id = row['id']
        todo.content = row['content']
        todo.caption = row['caption']
        todo.complete = row['complete']
        todo.date = row['date']

        return todo
