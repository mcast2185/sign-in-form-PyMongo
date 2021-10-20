from flask import Flask, render_template, session, redirect
from functools import wraps
import pymongo
from pymongo import collection


app = Flask(__name__)
app.secret_key = 'asdfghjkl'


# client = pymongo.MongoClient('mongodb+srv://dbAdmin:Ozymandias@login.umno5.mongodb.net/Login?retryWrites=true&w=majority')
# db = client['Login']
# collection = db['user_login']



client = pymongo.MongoClient('127.0.0.1', 27017)
db = client.user_login
collection = db['login']

def login_required(el):
  @wraps(el)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
      return el(*args, **kwargs)
    else:
      return redirect('/')
  return wrap


from user import routes

@app.route("/")
def home():
  return render_template('home.html')



@app.route("/dashboard/")
@login_required
def dashboard():
  return render_template('dashboard.html')
