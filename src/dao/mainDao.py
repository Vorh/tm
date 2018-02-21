import pymysql


class DataSource:

    def __init__(self):
        print('Init DS')
        self.con = pymysql.connect('localhost', 'root', 'root', 'tm')

    def getCursor(self):
        return self.con.cursor(pymysql.cursors.DictCursor)

    def commit(self):
        self.con.commit()

    def execute(self, sql):
        print(sql)
        self.con.cursor().execute(sql)
        self.con.commit()
