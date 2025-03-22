#Using HTTP verbs: Get and Post

from flask import Flask,render_template,request
#render_template is used to redirect to the html page linked here

app=Flask(__name__)

#Basic route creation
@app.route("/")    
def welcome():
    return render_template("home.html")

@app.route("/index", methods=['GET'])    
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/form",methods=['GET','POST'])
def form():
    if request.method == 'POST':        #Using POST method to fulfil a particular request made by user in the server
        name = request.form['name']     #Getting the name from the form
        return f"Hello {name}! Your form has been submitted"
    return render_template("form.html")         #Here GET method is used to hit the form page directly

@app.route("/submit",methods=['GET','POST'])
def submit():
    if request.method == 'POST':        #Using POST method to fulfil a particular request made by user in the server
        name = request.form['name']     #Getting the name from the form
        return f"Hello {name}! Your form has been submitted"
    return render_template("form.html")

#My code execution starts from here
if __name__ == "__main__":
    app.run(debug=True) 