from flask import Flask,request,render_template,url_for

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    if request.method=="POST":
        username=request.form["name"]
        email=request.form["email"]
        phoneno=request.form["phoneno"]
        return render_template("home.html",user=username,email=email,phoneno=phoneno)
if __name__=="main":
    app.run(debug=True)