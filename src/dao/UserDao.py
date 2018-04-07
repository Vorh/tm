import pymysql
from src.dao.mainDao import DataSource
from src.model.User import User, userMapper


class UserDao:

    def __init__(self, ds: DataSource):
        print('Init UserDao')
        self.ds = ds

    def isExistUser(self, name):
        sql = "select count(*) from user where username = '%s'" % name
        cur = self.ds.execute(sql)
        return cur.fetchone()[0] == 1

    def getUser(self, name, password):
        sql = "select * from user where username = '%s' and password = '%s'" % \
              (name, password)

        cur = self.ds.execute(sql)
        row = cur.fetchone()

        if row is None:
            return None
        return userMapper(row)

    def getUserById(self, userId):
        sql = "select * from user where id = '%s'" % userId

        cur = self.ds.execute(sql)
        return userMapper(cur.fetchone())

    def isCorrectLogin(self, name, password):
        sql = "select count(*) from user where username = '%s' and password = '%s'" % \
              (name, password)
        cur = self.ds.execute(sql)
        return cur.fetchone()['count(*)'] == 1
