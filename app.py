import os
from flask import Flask, render_template, redirect, request, url_for, \
    session, flash, Markup
from flask_pymongo import pymongo, PyMongo
from os import path
if path.exists("env.py"):
    import env


app = Flask(__name__)
MONGO_URI = os.environ.get("MONGO_URI")
# passing Secret key via environment
SECRET_KEY = os.environ.get("SECRET_KEY")

# creating mongo app
mongo = PyMongo(app)
@app.route('/')
def index():
    ''' function to display all records on the landing page'''
    authors = mongo.db.authors.find()
    return render_template(
        'index.html',
        authors=authors,
        )
