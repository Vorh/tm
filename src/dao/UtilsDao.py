from src.dao.mainDao import DataSource


class UtilsDao:

    def __init__(self, dataSource: DataSource):
        self.ds = dataSource

    def nextval(self, sequence):
        cursor = self.ds.getCursor()
        sql = """SELECT AUTO_INCREMENT
              FROM information_schema.TABLES
              WHERE TABLE_SCHEMA = 'tm'
              AND TABLE_NAME = '%s'""" % sequence

        print(sql)
        cursor.execute(sql)
        id = cursor.fetchone()['AUTO_INCREMENT']
        print("Generated id %s for %s" % (id, sequence))
        return id
