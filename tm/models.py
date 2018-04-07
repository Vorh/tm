from tm import db
from flask_login import UserMixin
from datetime import datetime


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(255))
    date_registered = db.Column(db.DateTime, default=datetime.utcnow)
    todos = db.relationship('Todo', backref='author', lazy='dynamic')
    goals = db.relationship('Goal', backref='author', lazy='dynamic')
    rewards = db.relationship('Reward', backref='author', lazy='dynamic')


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255))
    date = db.Column(db.DateTime)
    complete = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    reward_id = db.Column(db.Integer, db.ForeignKey('reward.id'))


class Reward(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.String(255))
    reward = db.Column(db.String(255))
    date_created = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
