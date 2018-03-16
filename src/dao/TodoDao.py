import pymysql
from injector import inject
from src.dao.mainDao import DataSource
from src.model.Todo import Todo


class TodoDao:

    @inject
    def __init__(self, dataSource: DataSource):
        self.ds = dataSource

    def getListTodo(self, userId):
        print('Get todos for user %s' % userId)
        cur = self.ds.getCursor()
        sql = "select * from todo where user_id = '%s' ORDER by date DESC" % userId
        cur.execute(sql)
        result = cur.fetchall()

        todos = []
        for row in result:
            todo = Todo()
            todo.id = row['id']
            todo.content = row['content']
            todo.caption = row['caption']
            todo.complete = row['complete']
            todo.date = row['date']
            todos.append(todo)

        print('Todos size: %s' % len(todos))

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
