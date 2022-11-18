from flask import Flask,request,render_template,url_for,make_response

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
@app.route("/login",methods=["GET","POST"])
def login():
    username=""
    password=""
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username=request.form["username"]
        password=request.form["password"]
    if username=="admin" and password=="admin":
        response=make_response(render_template("home.html",user=username))
        response.set_cookie("username",username)
        response.set_cookie("password",password)
        return response
    else:
        return render_template("login.html")+"Invalid Username and/or Password"
@app.route("/home",methods=["GET","POST"])
def home():
    if request.method=="GET":
        username=request.cookies.get("username")
        password=request.cookies.get("password")
        if username=="admin" and password=="admin":
            return render_template("home.html",user=username)
        else:
            return render_template("login.html")+"Invalid Username and/or Password"

if __name__=="main":
    app.run(debug=True)