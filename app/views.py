import re


try:
    from flask import Flask, render_template

except ImportError:
    pass

app = Flask(__name__)

#@app.route("Path") 

@app.route("/")
def index():
    return "Hi"

@app.route("/hello")
def hello():
    return render_template("hello.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/hello-user/<name>")
def hello_user(name):
    return render_template("hello_user.html", username = name.title())

@app.route("/add/<int:num1>/<int:num2>")
def add(num1,num2):
    calc = num1+ num2
    return render_template("add.html", num1 = num1, num2 = num2, result = calc)