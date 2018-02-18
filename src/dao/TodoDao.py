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
            todos.append(todo)

        print('Todos size: %s' % len(todos))
        return todos

    def insertTodo(self, todo):
        print("Insert todo for user id %s " % todo.userId)
        sql = "insert into todo (content, date,  user_id, caption) " \
              " values (%s,now(),%s,%s)" % todo.content, todo.userId, todo.caption

        cur = self.ds.getCursor()
        cur.execute(sql)
