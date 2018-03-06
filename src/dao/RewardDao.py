import pymysql
from injector import inject
from src.dao.mainDao import DataSource


class RewardDao:

    @inject
    def __init__(self, dataSources: DataSource):
        self.ds = dataSources
