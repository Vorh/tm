import pymysql
from src.dao.mainDao import DataSource
from src.model.Reward import Reward
from src import app


class RewardDao:

    def __init__(self, dataSources: DataSource):
        self.ds = dataSources

    def insertReward(self, reward: Reward):
        sql = """insert into reward (caption, reward, user_id) VALUES  
            ('%s', '%s' ,%s)""" % (reward.caption, reward.reward, reward.user_id)
        self.ds.execute(sql)

    def userIsOwnReward(self, userId, rewardId):
        sql = """select count(*) as c from reward where user_id = '%s' and id = '%s'""" % \
              (userId, rewardId)

        return self.ds.execute(sql).fetchone()['c'] >= 1

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

    def rewardIsTied(self, rewardId):
        sql = "select count(*) as c from goal where reward = '%s'" % rewardId
        return self.ds.execute(sql).fetchone()['c'] >= 1


    def deleteReward(self, userId, rewardId):
        sql = "delete from reward where user_id = %s and id = %s" % \
              (userId, rewardId)

        self.ds.execute(sql)

        app.logger.info('%s Delete reward %s' % (userId, rewardId))
