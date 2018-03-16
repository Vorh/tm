import pymysql
from injector import inject
from src.dao.mainDao import DataSource
from src.model.Reward import Reward


class RewardDao:

    @inject
    def __init__(self, dataSources: DataSource):
        self.ds = dataSources

    def insertReward(self, reward: Reward):
        sql = """insert into reward (caption, reward, user_id) VALUES  
            (%s, %s ,%s)""" % (reward.caption, reward.reward, reward.user_id)
        self.ds.execute(sql)

    def getRewards(self, userId):
        sql = "select * from reward where user_id = %s" % userId

        cur = self.ds.execute(sql)
        result = cur.fetchall()

        rewards = []
        for row in result:
            reward = Reward()
            reward.id = row['id']
            reward.caption = row['caption']
            reward.reward = row['reward']
            reward.create_date = row['create_date']
            rewards.append(reward)

        return rewards
