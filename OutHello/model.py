#!/usr/bin/python
#coding=utf-8

from main import db

class User(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(128), unique=True)
    email = db.Column(db.String(128))
    priority = db.Column(db.Integer)
    password = db.Column(db.String(32))

    def __init__(self, username, password='', email='', priority=0):
        self.uname = username
        self.email = email
        self.priority = priority
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username