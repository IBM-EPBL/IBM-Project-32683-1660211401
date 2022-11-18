from this import d
from flask import Flask,render_template,request,url_for,send_from_directory,make_response
from flask import send_file
import os
app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
@app.route("/loginpage",methods=["GET","POST"])
def login():
    if(request.method=="GET"):
        return render_template("login.html")
    if(request.method=="POST"):
        username=request.form["username"]
        password=request.form["password"]
        if(username=="abdullah" and password=="abdullah"):
            path=os.getcwd()+"/"+username
            if(not(os.path.isdir(path))):
                os.mkdir(os.getcwd()+"/"+username)
            response=make_response(render_template("home.html",user=username))
            response.set_cookie("username",username)
            response.set_cookie("password",password)
            return response
        else:
            return render_template("login.html")+"Invalid Username and/or Password"
@app.route("/homepage",methods=["POST"])
def home():
    if(request.method=="POST"):
        username=request.cookies.get("username")
        password=request.cookies.get("password")
        if(username=="abdullah" and password=="abdullah"):
            req=request.files["file"].filename
            file=request.files["file"]
            file.save(str(file.filename))
            path=os.getcwd()+"/"+username+"/"
            if(os.path.isfile(path+"1.pdf")):
                os.remove(os.getcwd()+"/"+username+"/"+"1.pdf")
            os.rename(os.getcwd()+"/"+req,os.getcwd()+"/"+"1.pdf")
            os.rename(os.getcwd()+"/"+"1.pdf",os.getcwd()+"/"+username+"/1.pdf")
            file1=open(os.getcwd()+"/"+username+"/file.txt",mode="a")
            file1.write(req)
            file1.close()
            #path=os.getcwd()+"/"+username+"/"+"1.pdf"
            #path1=open(os.getcwd()+"/"+username+"/"+"file.txt",mode="r")
            #response=send_file(path)
            #response.headers["x-filename"]=path1.read()
            #response.headers["Access-Control-Expose-Headers"]="x-filename"
            return render_template("home.html",user=username)
        else:
            return render_template("login.html")+"Invalid Username and/or Password"
@app.route("/method")
def method():
    return "Saved Successfully"
@app.route("/pdf_site",methods=["GET"])
def pdf():
    if(request.method=="GET"):
        username=request.cookies.get("username")
        password=request.cookies.get("password")
        if(username=="abdullah" and password=="abdullah"):
            file=os.getcwd()+"/"+username+"/"+"1.pdf"
            ls1=open(os.getcwd()+"/"+username+"/1.pdf",mode="rb")
            ls2=open(os.getcwd()+"/"+username+"/file.txt",mode="r")
            ls5=ls2.read()
            ls3=open(os.getcwd()+"/"+username+"/"+ls5,mode="wb")
            ls3.write(ls1.read())
            ls1.close()
            ls2.close()
            ls3.close()
            path=open(os.getcwd()+"/"+username+"/"+ls5,mode="rb")
            return send_from_directory(os.getcwd()+"/"+username+"/",ls5)
        else:
            return render_template("login.html")+"Invalid Username and/or Password"
    return "memory"
@app.route("/",methods=["GET","PUT"])
@app.route("/login",methods=["GET","POST"])
def login_website():
    if(request.method=="GET"):
        return render_template("login.html")
    if(request.method=="POST"):
        username=request.form["username"]
        password=request.form["password"]
        if(username=="abdullah" and password=="abdullah"):
            if(not(os.path.exists(os.getcwd()+"/"+username))):
                os.mkdir(os.getcwd()+"/"+username)
            response=make_response(render_template("home.html",user=username))
            response.set_cookie("username",username)
            response.set_cookie("password",password)
            return response
        else:
            return render_template("login.html")+"Invalid username and/or password"
    return render_template("login.html")
@app.route("/home",methods=["GET","POST"])
def dashboard():
    if(request.method=="GET"):
        username=request.cookies.get("username")
        password=request.cookies.get("password")
        if(username=="abdullah" and password=="abdullah"):
            return render_template("home.html",user=username)
        else:
            return render_template("login.html")+"Invalid username and/or password"
    if(request.method=="POST"):
        username=request.cookies.get("username")
        password=request.cookies.get("password")
        if(username=="abdullah" and password=="abdullah"):
            filename=request.files["file"].filename
            file1=request.files["file"]
            if(os.path.exists(os.getcwd()+"/"+username+"/"+filename)):
                os.remove(os.getcwd()+"/"+username+"/"+filename)
            file1.save(str(file1.filename))
            path=str(file1.filename)
            os.rename(os.getcwd()+"/"+path,os.getcwd()+"/"+username+"/"+path)
            return render_template("home.html",user=username)+"Saved Successfully"
    return render_template("login.html")+"Invalid Username and/or Password"
@app.route("/pdf",methods=["GET"])
def pdf_get():
    if(request.method=="GET"):
        username=request.cookies.get("username")
        password=request.cookies.get("password")
        if(username=="abdullah" and password=="abdullah"):
            filename=os.listdir(os.getcwd()+"/"+username)
            ls=list(filename)
            filename=ls[0]
            return send_file(os.getcwd()+"/"+username+"/"+filename)
    return render_template("login.html")+"Invalid username and/or password"
if __name__=="__main__":
    app.run(dubug=True)