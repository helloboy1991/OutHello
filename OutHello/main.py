#!/usr/bin/python
#coding=utf-8

import os
import sys

import hashlib
import time
import datetime

from flask import *
from flask_sqlalchemy import SQLAlchemy
import model

app = Flask(__name__)
base_path = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = os.urandom(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_path, 'data.sqlite')
db = SQLAlchemy(app)

def get_login_token(uname, login_time):
	return hashlib.md5(uname+login_time+'$$$').hexdigest()

def check_login_token(uname, login_time, login_token):
	real_token = get_login_token(uname, login_time)
	if real_token==login_token:
		return True
	return False

@app.route('/')
def index():
	uname = request.cookies.get('name')
	login_time = request.cookies.get('login_time')
	login_token = request.cookies.get('login_token')

	if login_time is None:
		login_time = ''
	if login_token is None:
		login_token = ''

	if not uname is None:
		if not check_login_token(uname, login_time, login_token):
			response = make_response(render_template('cn_index.html'))
			response.delete_cookie('name')
			return response

	return render_template('cn_index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method=='GET':
		return render_template('cn_login.html')
	elif request.method=='POST':
		uname = request.form.get('user-name')
		password = request.form.get('password')
		password = hashlib.md5(password).hexdigest()
		print uname, password
		u = model.User.query.filter_by(uname=uname).first()
		if u is None:
			return redirect('/logup')
		if u.password==password:
			login_time = str(int(time.time()))
			response = make_response(redirect('/'))
			login_token = get_login_token(uname, login_time)
			
			response.set_cookie('name', uname)
			response.set_cookie('login_time', login_time)
			response.set_cookie('login_token', login_token)
			
			return response

		return redirect('/login')

@app.route('/logup', methods=['GET', 'POST'])
def logup():
	if request.method=='GET':
		return render_template('cn_logup.html')
	elif request.method=='POST':
		uname = request.form.get('user-name')
		password = request.form.get('password')
		password = hashlib.md5(password).hexdigest()
		print uname, password
		u = model.User.query.filter_by(uname=uname).first()
		if u is None:
			u = model.User(uname, password)
			db.session.add(u)
			db.session.commit()
		else:
			return redirect('/login')

		return redirect('/')

@app.route('/CN')
def cn_index():
	return render_template('cn_index.html')

if __name__ == '__main__':
	app.debug = True
	app.run('0.0.0.0')
