import pymysql
from src.dao.mainDao import DataSource
from src.model.User import User


class UserDao:

    def __init__(self, ds: DataSource):
        print('Init UserDao')
        self.ds = ds

    def isExistUser(self, name):
        sql = "select count(*) from users where username = '%s'" % name
        cur = self.ds.execute(sql)
        return cur.fetchone()[0] == 1

    def getUser(self, name, password):
        sql = "select * from users where username = '%s' and password = '%s'" % \
              (name, password)

        cur = self.ds.execute(sql)

        return User(10, 'Test', 'Test')

    def getUserById(self, userId):
        sql = "select * from users where id = '%s'" % userId

        self.ds.execute(sql)

        return User(10, 'Test', 'Test')

    def isCorrectLogin(self, name, password):
        sql = "select count(*) from users where username = '%s' and password = '%s'" % \
              (name, password)
        cur = self.ds.execute(sql)
        return cur.fetchone()['count(*)'] == 1
