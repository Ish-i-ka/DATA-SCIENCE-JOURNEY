from flask import Flask

# Create an instance of Flask class,
# which will be our WSGI application

app=Flask(__name__)

#Basic route creation
@app.route("/")     #This is a decorator by which we can define the route of the web server
#This is the function which is called when the user hits the back slash in the web server
def welcome():
    return "Welcome to my Flask application.This is gonna be the best one."

@app.route("/index")    
def index():
    return "Welcome to index page."

#My code execution starts from here
if __name__ == "__main__":
    app.run(debug=True) #This automqatically reflects the changes in the server without re-running the server.
    