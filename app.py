import os
from flask import Flask, render_template, redirect, request, url_for, \
    session, flash, Markup
from flask_pymongo import pymongo, PyMongo
from os import path

if path.exists("env.py"):
    import env


MONGO_URI = os.environ.get('MONGO_URI')
SECRET_KEY = os.environ.get('SECRET_KEY')
# mongo = PyMongo(app)

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index(): 

    return render_template('index.html')
    

if __name__ == '__main__':

    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)