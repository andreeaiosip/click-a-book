import os

from flask import Flask, render_template, redirect, request, url_for, \
    session, flash, Markup
from flask_pymongo import pymongo, PyMongo
from os import path

if path.exists('env.py'):
    import env

app = Flask(__name__)

# MONGO_URI = os.environ.get('MONGO_URI')
# SECRET_KEY = os.environ.get('SECRET_KEY')

# mongo = PyMongo(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/register')
def register():
    return render_template('register.html')
    

@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
