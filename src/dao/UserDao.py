import pymysql
from src.dao.mainDao import DataSource


class UserDao:

    def __init__(self, ds: DataSource):
        print('Init UserDao')
        self.ds = ds

    def isExistUser(self, name):
        sql = "select count(*) from users where username = '%s'" % name
        cur = self.ds.execute(sql)
        return cur.fetchone()[0] == 1

    def getUserId(self, name, password):
        sql = "select id from users where username = '%s' and password = '%s'" % \
              (name, password)

        cur = self.ds.execute(sql)

        return cur.fetchone()['id']

    def isCorrectLogin(self, name, password):
        sql = "select count(*) from users where username = '%s' and password = '%s'" % \
              (name, password)
        cur = self.ds.execute(sql)
        return cur.fetchone()['count(*)'] == 1
