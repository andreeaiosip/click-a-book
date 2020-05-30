from flask import Flask
from os import path
if path.exists("env.py"):
  import env 
  

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello!</h1>'

    if __name__ == '__main__':
        app.debug = True