from flask_pymongo import PyMongo
from flask import Flask, flash, render_template, redirect, request, url_for, \
    session, flash, Markup
# from forms import RegistrationForm, LoginForm
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import os
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config['SECRET_KEY'] = os.urandom(32)

mongo = PyMongo(app)

# Display all books and comments on home page
@app.route('/')
def index():
    ''' function to display all books on the home page'''
    books = list(mongo.db.bookInfo.find())
    comments = list(mongo.db.comments.find())
    return render_template('index.html', books=books, comments=comments)

# Register ------------------------------------
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
        return redirect(url_for("index", username=session["user"]))
    return render_template("register.html")

# Login -----------------------------------------------------

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
                        "index", username=session["user"]))
            else:
                # invalid password
                flash("Incorrect credentials.")
                return redirect(url_for("login"))

        else:
            # the username is not registered
            flash("Incorrect credentials")
            return redirect(url_for("login"))
    return render_template('login.html')


# Userțs Profile -----------------------
@app.route("/profile/<username>", methods=['GET', 'POST'])
def profile(username):
    # get the session username from db
    username = mongo.db.users.find_one(
       {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("profile"))


# Logout -----------------------------------

@app.route("/logout")
def logout():
    # remove user from current session cookie

    flash("You have been logged out. See you soon!")
    session.pop("user")
    return redirect(url_for("login"))


# DELETE PROFILE ------------------------------

@app.route("/delete_profile/<user_id>", methods=["GET", "POST"])
def delete_profile(user_id):
    mongo.db.users.remove({"username": session["user"]})
    session.clear()
    flash("Your profile has been deleted.")
    return redirect(url_for("index"))


# Add comment -------------------------
@app.route("/add_comment/<book_id>", methods=["GET", "POST"])
def add_comment(book_id):
    book = mongo.db.bookInfo.find_one({"_id": ObjectId(book_id)})
    if request.method == "POST":
        new_comment = {
            "title": book["title"],
            "comment": request.form.get("comment"),
            "username": session["user"]
        }

        mongo.db.comments.insert_one(new_comment)
        flash("Comment added")
        return redirect(url_for("index"))

    return render_template("add_comment.html", book=book)


# DELETE COMMENT -----------------
@app.route("/delete_comment/<comment_id>", methods=["GET", "POST"])
def delete_comment(comment_id):
    mongo.db.comments.remove({"_id": ObjectId(comment_id)})
    flash("Comment deleted")
    return redirect(url_for("index"))


# Update comment  -------------------------
@app.route("/update_comment/<comment_id>", methods=["GET", "POST"])
def update_comment(comment_id):
    comments = mongo.db.comments.find_one({"_id": ObjectId(comment_id)})
    if request.method == "POST":
        mongo.db.comments.update({'_id': ObjectId(comment_id)}, {
            "title": comments["title"],
            "comment": request.form.get("comment"),
            "username": session["user"]
        })
        flash("Comment updated")
        return redirect(url_for("index"))
    return render_template("update_comment.html", comments=comments)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
