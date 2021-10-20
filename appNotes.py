# 1 open terminal and create a virtual environment (virtualenv -p python3 env )
  # a env file is created in our directory, to activate it (source env/bin/activate). (env) will show up on terminal
# 2 (pip install flask pymongo passlib) to install the required packages
# 3 create our (app.py) file, import (from flask import Flask) and create our app instance 
  # we then create our route for the app (@app.route("/"))
"""""
from flask import Flask

app = Flask(__name__)
@app.route("/")
def home():
  return 'home'
"""
# 4 in order to run our app, we create a script file in our directory (run) no extension
  # (FLASK_APP=app.py FLASK_ENV=development flask run) we can run script files by (./<filename>)==(./run) after making it executeable
# 5 excute file (sudo chmod +x run) x resembles execute. 
# 6 we set up two templates, home page, dashboard page. create folder (templates) home.html, dashboard.html then a base template as well
# 7 within base.html we create the basic html structure. 
  # within the body we create a block location for templates
"""""
<body>
  
  {% block content %}
    {# template inserted here #}
  {% endblock %}

</body>

"""
# 8 we then create extensions inside our two other files {% extends "base.html" %} {% block content %}<h1><filename></h1>{% endblock %}
# 9 we create a separate route for our dashboard in our (app.py) file and add an import (render_template) which we used as our returns
  # and from our (http://127.0.0.1:5000/) local host we can add the route at the end to view our changes
# 10 copy and pasted example css
# 11 create new folder (user) and add a file (__init__.py)
  # this will let us use the user folder as a python module that we can import into other python files. the init file doesnt have to have content
# 12 create another file within the user folder (routes.py)
  # import flask. this file will contain all the routes related to the user like (user/signup)(user/login)
# 13 inside the user folder we create our third file (models.py)
# 14 within models.py we import flask. 
  # create a user class and a sign up method

"""
class User:

  def signup(self):
    user = {
      "_id": "",
      "name": "",
      "email": "",
      "password": ""
    }
    return jsonify(user), 200

"""

# 15 we created parameters for the user
# 16 in our return we used jsonify so that the browser can display the python code. we also add a status code (200=success)(400=fail)
  # jsonify is a flask function so we add it to the imports
# 17 to run the code we just created we switch to (routes.py). 
  # we import our app.py in order to use our variable app as an instance to call Flask (app.py)
# 18 we create a route (@app.route()) with a function signup
  # what we want when they use that route is to run our User class and its method, so we import that file
  # the class is located within a folder so we traverse into it (from user.models import User)

"""
from app import app
from user.models import User

@app.route('/user/signup', methods=["POST"])
def signup():
  (optional)- here we could insert: user = User() and have our return be: user.signup()
  return User().signup()

"""

# 19 import our routes into our app.py file. since we only need the routes, not methods we import the routes itself
  # (from user import routes)
    ##### 
      # it is paramount to understand where to place the imports 
      # if we import routes at the top of the file where
      # flask is located, an error will occur. this is because we are asking a file that is imported to perform a task
      # that relies on code written in our current file, but we are doing so before the code is processed/read. 
        # so if (routes.py) needs the import of our variable app, and in turn, to run (routes.py) we need it imported to (app.py)
        # we need to import routes after the code (app= Flask(__file__)) is sent to (routes.py)
    #####
"""
from flask import Flask, render_template

app = Flask(__name__)

from user import routes

"""
# 20 switching over to our home file, we replace the placeholder text and add elements to create a form
  # the style has been provided to us by github

"""
  <div class="card-wrapper">
    <div class="card">
      <h1 class="center">Create an Account</h1>
      <form name="signup_form">
        <label for="name">Name</label>
        <input type="text" name="name" class="field" required>

        <label for="email">Email</label>
        <input type="email" name="email" class="field" required>

        <label for="password">Password</label>
        <input type="password" name="password" class="field" required>

        <p class="error error--hidden">
          
        </p>

        <input type="submit" value="Sign Up" class="btn">
      </form>
    </div>
  </div>

"""

# 21 next we switch to our script file where we create the logic that takes the submissions of the form and connects
  # to our signup route.
  # we do this by leveraging jquery and specifically targeting the form element and adding an event function
  # (submit) which takes a function with a single value as its argument, the value being the process of filling out
  # the form and initializing it with the button, and instead of clearing out the boxes and refreshing the page on the click
  # we attach the prevent default method to our variable to impede that process from occuring
  # its important to note that sense we are solely working with the form in this project, all the code thats written out
  # will be under the same jquery element we are manipulating
# 22 we create variables within the function. we create a form variable and set it equal to this, taking the value of users input
  # we create an error element and set it equal to the dom element error using the find method
  # we create a data variable, and set it equal to all the fields from the form and serializes
  # them so to be interpreted by the backend. 
# 23 (changed get to post in routes.py) inside the same function we utilize the ajax call method
  # ajax (Asynchronous JavaScript and XML) is the art of exchanging data with a server, and update parts of a web page 
  # without reloadng the whole page
  # ajax serves as a request tool, a really fast one
  # the parameters to the request is:
    # the url its sending info to is user signup
    # the type that its requesting to send is a post
    # the data being sent is the value of our variable data (obtains value from instantiated form input)
    # the data type that it is expected to send is json (text is transferred into json with .serialize())
    # then functions to inform us of whether the request was successful or not

"""
$("form[name=signup_form]").submit(function(e){
  let $form = $(this);
  let $error = $form.find(".error");
  let data = $form.serialize();
  $.ajax({
    url: "/user/signup",
    type: "POST",
    data: data,
    dataType: "json",
    success: function(resp){
      console.log(resp);
    },
    error: function(resp){
      console.log(resp);
    }
  });
  e.preventDefault();
});

"""

# 24 what we receive on the chrome console when we enter our form info is
  # is an object with id, name, email, and password
  # this occurs because we our sending our input to the user/signup url with post
  # since we are utilizing the user/signup route, it follows the parameters set for that route in (route.py)
  # which has us return our data, instantiated as the User class (models.py) with the method
  # signup, which applies the information to the appropriate key/values
  # which then, finally, gets returned back into a json form of our processed data, 
  # organized by the parameters of our signup method

"""
step 1 (filtered through routes):
  @app.route('/user/signup', methods=["POST"])
  def signup():
    return User().signup();

step 2 (filtered through models from our return):
  class User:
    def signup(self):
      user = {
        "_id": "",
        "name": "",
        "email": "",
        "password": ""
      }
    return jsonify(user), 200

"""

# 25 (models.py)(add request import) we update the object placeholder values, previously ""
  # the key, name, has its value set to request.form.get('name')
    # this grabs the "name" value, from input element, for that parameter 
      # (<input type="text" name="name" class="field" required>)
  # the same code structure is followed for email and password, replacing 
  # .get('name') with its respective parameters (email, password)
  # (note) dont use arrow functions with jquery, arrow functions is a newer feature
# 26 (models.py) we imported a new package (uuid).
  # by calling the object then the method ("_id": uuid.uuid4().hex) adding another method (hex)
  # to convert the id into a string in hexidecimal form
# 27 (models) if we want to see it on the console as a form of managing/ debugging 
  # above our user object, (print(request.form))
# 28 we dont want anyone being able to see the password inside the database in plain text
  # so we encrypt it by executing this (from passlib.hash import pbkdf2_sha256) first, under our flask import
  # then we select and set the value of our password to the function imported from passlib with the encrypt method
  # user['password'] = pbkdf2_sha256.encrypt(user['password'])
# 29 (app.py) we now begin to establish our connection to the mongo database by first importing
  # pymongo, below the flask import
# 30 we then create a pymongo client instance, setting it equal to pymongo which then allows for
  # the MongoClient class to be called from its module.
  # ( client = pymongo.MongoClient('127.0.0.1', 27017) )
  # MongoClient takes two arguments, the first being the value of our host, which is (127.0.0.1)
  # and we know this because we can see the host returning data in our terminal after each save
  # then we pass in the port which, by default is 27017
    # under the documentation of mongodb it reads that for mongod and mongos, that is the port
    # and if we are using mongo's database, mongod will be used
# 31 we then create our database variable (db = client.user_login)
  # this is were we place/create the name of our database