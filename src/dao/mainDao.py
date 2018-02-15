import pymysql


class DataSource:

    def __init__(self):
        print('Init DS')
        self.con = pymysql.connect('localhost', 'root', 'root', 'tm')

    def getCursor(self):
        return self.con.cursor(pymysql.cursors.DictCursor)
