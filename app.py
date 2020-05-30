import os
from flask import Flask
from flask_pymongo import PyMongo, pymongo
from os import path

if path.exists("env.py"):
    import env

app = Flask(__name__)
MONGO_URI = os.environ.get('MONGO_URI')
SECRET_KEY = os.environ.get('SECRET_KEY')
mongo = PyMongo(app)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')), 
            debug=True)
