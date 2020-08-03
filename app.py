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

# REGISTER
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

         # put the user in session cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration sucessfull")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")

# LOGIN-----------------------------------------------------


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # password match check
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Nice to see you again, {}!".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                    # invalid password
                flash("Incorrect credentials.")
                return redirect(url_for("login"))

        else:
                # the username is not registered
            flash("Incorrect credentials")
            return redirect(url_for("login"))
    return render_template('login.html')


# USER'S PROFILE
@app.route("/profile/<username>", methods=['GET', 'POST'])
def profile(username):
    # get the session username from db
    username = mongo.db.users.find_one(
       {"username": session["user"]})["username"]

    if session["user"]:
         return render_template("profile.html", username=username)

    return redirect(url_for("profile"))


@app.route("/logout")
def logout():
# remove user from current session cookie
    flash("You have been logged out. See you soon!")
    session.pop("user")
    return redirect(url_for("login"))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
