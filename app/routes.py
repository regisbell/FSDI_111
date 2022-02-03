from flask import Flask                 #from the flask module import the Flask class


app = Flask(__name__)                   #Instantiate the Flask class into the app variable.
                                        #Variables that contain class instances are called 'objects'.


@app.route("/")                         #This is a decorator
def index():                            #This is a function; In the context of flask it is a "view function"
    return"<h1>Hello, world!</h1>"      #Return statement; This is returning a string.


@app.get("/home")
def home():
    return "Welcome home!"


@app.route("/about")
def about_me():
    me = {
        "first_name": "Regis",
        "last_name": "Bell",
        "hobbies": "Reading",
        "active": True
    }
    return me 