#!/usr/bin/python
#coding=utf-8

from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/CN')
def cn_index():
	return render_template('cn_index.html')

if __name__ == '__main__':
	app.debug = True
	app.run('0.0.0.0')
