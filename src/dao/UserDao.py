import pymysql
from injector import inject
from src.dao.mainDao import DataSource


class UserDao:

    @inject
    def __init__(self, ds: DataSource):
        print('Init UserDao')
        self.ds = ds.con

    def isExistUser(self, name):
        db_cursor = self.ds.cursor()
        sql = "select count(*) from users where username = '%s'" % name
        db_cursor.execute(sql)
        return db_cursor.fetchone()[0] == 1

    def isCorrectLogin(self, name, password):
        db_cursor = self.ds.cursor()
        sql = "select count(*) from users where username = '%s' and password = '%s'" % \
              (name, password)
        db_cursor.execute(sql)
        return db_cursor.fetchone()[0] == 1