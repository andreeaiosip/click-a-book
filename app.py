from flask_pymongo import PyMongo
from flask import Flask, flash, render_template, redirect, request, url_for, \
    session, flash, Markup
from forms import RegistrationForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
import os
from os import path
if path.exists("env.py"):
    import env


# MONGO_URI = os.environ.get("MONGO_URI")
# SECRET_KEY = os.environ.get('SECRET_KEY')

app = Flask(__name__)
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
# print("I'm a db", os.environ.get("MONGO_URI"))
app.config['SECRET_KEY'] = os.urandom(32)
# Variables for database
mongo = PyMongo(app)

# Collections

# usersDB = mongo.db.users
# bookInfoDB = mongo.db.bookInfo


@app.route('/')
def index():
    ''' function to display all books on the home page'''
    bookInfoDB = list(mongo.db.bookInfo.find())
    print(bookInfoDB)
    return render_template(
        'index.html',
        bookInfoDB=bookInfoDB,
    )


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already taken")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")) 
        }
        mongo.db.users.insert_one(register)

         #put the user in session cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration sucessful")
    return render_template("index.html")


@app.route("/login", methods=['GET', 'POST'])
def login():

    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get("password")
        existing_user = find_user(username)
        if existing_user and check_password_hash(existing_user["password"], password):
            # Welcome message
            flash(Markup(
                "Nice to see you again "
                + username.capitalize()
                ))
            session["username"] = username
            return redirect(url_for('index', username=session["username"]))

        else:

            flash(Markup(
                "Credentials not valid. Please try again."))
        return redirect(url_for('login'))

    return render_template('login.html')

    # Hardcoded login
    # form = LoginForm()
    # if form.validate_on_submit():
    #     if form.username.data == 'admin' and form.password.data == 'admin':
    #         flash('You have been logged in!', 'success')
    #         return redirect(url_for('index'))
    #     else:
    #         flash('Login Unsuccessful. Please check your credentials!', 'danger')
    # return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
