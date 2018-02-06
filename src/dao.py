import pymysql


class UserDao:
    def __init__(self, cursor):
        self.cursor = cursor

    def isExistUser(self, name):
        sql = "select count(*) from users where username = '%s'" % name
        cursor.execute(sql)
        return self.cursor.fetchone()[0] == 1

    def isCorrectLogin(self, name, password):
        sql = "select count(*) from users where username = '%s' and password = '%s'" % \
              (name, password)
        cursor.execute(sql)
        return self.cursor.fetchone()[0] == 1

# userDao = UserDao(cursor)
#
# print(userDao.isExistUser('Vorh'))
# print(userDao.isExistUser('Vorh122312'))
# print(userDao.isExistUser('Vorh122323112'))
# print(userDao.isCorrectLogin('Vorh', '12'))
