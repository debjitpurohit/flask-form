## integrate html with flask have to import render templates /////and the file must be named as template
##its bacially jinja2 template engine
#### http verb get and put
from flask import Flask , redirect , url_for , render_template , request # request help to read posted values
from flask_pymongo import PyMongo
# mongodb://localhost:27017/myDatabase
# mongodb+srv://debjitshilpi:J2kYSRKCj6QFO6e8@cluster0.i3cf4f5.mongodb.net/debjitdata?retryWrites=true&w=majority
app= Flask(__name__)

app.config["MONGO_URI"] = "mongodb+srv://debjitshilpi:J2kYSRKCj6QFO6e8@cluster0.i3cf4f5.mongodb.net/debjitdata?retryWrites=true&w=majority"

# app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"

mongo = PyMongo(app)

@app.route('/') 
def home():
    return render_template("index.html") # must be have folder named as <<<   templates  >>>

# @app.route('/success/<int:score>')
# def success(score):
#     res=""
#     if score>=50:
#         res="pass"
#     else:
#         res="fail"
#     return render_template("result.html" , result = res) # here we pass the variable result to result.html page

# @app.route('/fail/<int:score>') 
# def fail(score):
#     return "you failed" 



##result checker

@app.route('/results/<int:marks>') 
def results(marks):
    res = ""
    if marks<50:
        res = "Fail"
    else:
        res = "Pass"   
    return render_template("result.html",result=res) # here we pass the variable result to result.html page

#result chcecker html page
@app.route('/submit',methods=['POST' , 'GET'])
def submit():
    totalscore = 0
    if request.method == 'POST': ## bcz we given method as post in html
        science = float(request.form['science']) # we given name="science" in html ...bydefault we get string so we have to convert it into float
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
        totalscore = (science + maths + c + data_science)/4
        mongo.db.inventory.insert_one(
            {'science':science,
             'maths':maths,
             'c':c,
             'data_science':data_science,
             'totalscore':totalscore}
             )
        
        a = mongo.db.inventory.find({})
        print(a ,type(a))
        for i in a:
            print(i['science'])
    # res = ""
    # if totalscore<50:
    #     res = "fail"
    # else:
    #     res = "success"    
    return redirect(url_for('results',marks=totalscore))           


# if __name__ == "__main__": 
app.run(debug=True, port=8001)
