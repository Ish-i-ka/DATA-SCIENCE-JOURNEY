from flask import Flask,render_template
#render_template is used to redirect to the html page linked here

app=Flask(__name__)

#Basic route creation
@app.route("/")    
def welcome():
    return render_template("home.html")

@app.route("/index")    
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

#My code execution starts from here
if __name__ == "__main__":
    app.run(debug=True) 