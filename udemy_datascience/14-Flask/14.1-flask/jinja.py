# Building URL Dynamically
# Variable rule

# Jinja 2 template engine
'''
{{..}} expressions to print output in html
{%..%} for control statements like if, for loops
{#..#} for comments
'''

from flask import Flask,render_template,request,redirect,url_for
#redirect is used to redirect to the url into some other route
#url_for is used to provide the other url to which we r re directing

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

@app.route("/submit",methods=['GET','POST'])
def submit():
    if request.method == 'POST':        #Using POST method to fulfil a particular request made by user in the server
        name = request.form['name']     #Getting the name from the form
        return f"Hello {name}! Your form has been submitted"
    return render_template("form.html")

#Variable Rule is basically restricting the data type of the parameter passed to the route
@app.route('/success/<int:score>')      #Score is tha parameter whose data type can be int only
def success(score):                     #parameter score is passed to the function
    
    if score>=50:
        res = 'PASSED'
    else:
        res = 'FAILED'
    
    return render_template('result.html',result=res,sc=score)    #result.html is rendered with the result and score

#expression and for loop and comment use in jinja
@app.route('/successres/<int:score>')      
def successres(score):                     
    
    if score>=50:
        res = 'PASSED'
    else:
        res = 'FAILED'
    
    exp = {'SCORE':score,'RESULT':res}
    return render_template('result1.html',result=exp)    

#if condition
@app.route('/successif/<int:score>')      
def successif(score):                     
    return render_template('result.html',result = score)   

## "/success" and "/successif" both doing same thing , just the  


@app.route('/fail/<int:score>')      
def fail(score):                     
    return render_template('result.html',result=res,sc=score)    

@app.route('/getresults',methods=['GET','POST'])
def getresults():
    total = 0
    if request.method == 'POST':        #POST is activated when we clk the submit, but at first click of url else part is executed
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        datascience = float(request.form['datascience'])
        total = science + maths + c + datascience
        avg = total/4
    else:
        return render_template('getresult.html')
    return redirect(url_for('successres',score=avg))
    

#My code execution starts from here
if __name__ == "__main__":
    app.run(debug=True) 