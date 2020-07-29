import os
from os import path
if path.exists("env.py"):
    import env
from forms import RegistrationForm, LoginForm
from flask import Flask, flash, render_template, redirect, request, url_for, \
    session, flash, Markup
from flask_pymongo import PyMongo

# MONGO_URI = os.environ.get("MONGO_URI")
# SECRET_KEY = os.environ.get('SECRET_KEY')

app = Flask(__name__)
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
# print("I'm a db", os.environ.get("MONGO_URI"))
app.config['SECRET_KEY'] = os.urandom(32)
# Variables for database
mongo = PyMongo(app)

# Collections

usersDB = mongo.db.users
bookInfoDB = mongo.db.bookInfo


@app.route('/')
def index():
    ''' function to display all records on the landing page'''
    bookInfoDB = list(mongo.db.bookInfo.find())
    print(bookInfoDB)
    return render_template(
        'index.html',
        bookInfoDB=bookInfoDB,
        )


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("/login.html", title="Login", form=form)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

