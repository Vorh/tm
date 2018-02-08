import pymysql
from injector import Injector, inject


class DataSource:

    def __init__(self):
        print('Init DS')
        self.db = pymysql.connect('localhost', 'root', 'root', 'tm')


class UserDao:

    @inject
    def __init__(self, ds: DataSource):
        print('Init UserDao')
        self.ds = ds.db

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


injector = Injector()
print('Init injector')
outer = injector.get(UserDao)

print(outer.isExistUser('Vorh'))
