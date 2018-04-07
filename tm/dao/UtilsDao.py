from tm.dao.mainDao import DataSource


class UtilsDao:

    def __init__(self, dataSource: DataSource):
        self.ds = dataSource

    def nextval(self, sequence):
        sql = """SELECT AUTO_INCREMENT
              FROM information_schema.TABLES
              WHERE TABLE_SCHEMA = 'tm'
              AND TABLE_NAME = '%s'""" % sequence

        cur = self.ds.execute(sql)
        id = cur.fetchone()['AUTO_INCREMENT']
        return id

    @staticmethod
    def toSqlList(list):
        return ",".join(map(str, list))
