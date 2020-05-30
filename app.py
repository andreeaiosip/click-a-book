import os
from flask import Flask
from flask_pymongo import PyMongo, pymongo
from os import path
if path.exists("env.py"):
  import env 

  
app = Flask(__name__)

# configuration of Database
MONGO_URI = os.environ.get(“mongodb%2Bsrv%3A%2F%2Fandreea%3A%3CandreeaDB%3E%40cluster1-2cndy.mongodb.net%2Ftest%3FretryWrites%3Dtrue%26w%3Dmajority”)

SECRET_KEY = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)



if __name__ == '__main__':    
    app.run(host=os.environ.get('IP'),        
    port=int(os.environ.get('PORT')),        
    debug=True)