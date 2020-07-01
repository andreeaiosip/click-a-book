import os
from os import path
from flask import Flask, render_template, redirect, request, url_for, \
    session, flash, Markup
from flask_pymongo import PyMongo

# MONGO_URI = os.environ.get("MONGO_URI")
# SECRET_KEY = os.environ.get('SECRET_KEY')

import env
app = Flask(__name__)
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
print("I'm a db", os.environ.get("MONGO_URI"))
app.config['SECRET_KEY'] = os.urandom(32)
# Variables for database
mongo = PyMongo(app)


@app.route('/')
def index():
    ''' function to display all records on the landing page'''
    authorsDB = list(mongo.db.authors.find())
    print(authorsDB)
    return render_template(
        'index.html',
        authorsDB=authorsDB,
        )


@app.route("/")
def register():
    return render_template("/register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('index'))
    return render_template('login.html', error=error)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

