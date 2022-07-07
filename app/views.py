try:
    from flask import Flask, render_template, redirect,url_for, request, make_response
    from itsdangerous import Signer, BadSignature

except ImportError:
    pass

app = Flask(__name__)
#@app.route("Path") 

@app.route("/")
def index():
    signer = Signer("secret key")
    signed_name = request.cookies.get('name')

    try:
        name = signer.unsign(signed_name).decode()
        print('name', name)

    except BadSignature:
        print("Bad Signature")

    signed_name = signer.sign("Burak")
    response = make_response("<html><body><h1>Try Flask</h1></body></html>")
    response.set_cookie('name',signed_name)

    return response

@app.route("/hello")
def hello():
    return render_template("hello.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/hello-user/<name>")
def hello_user(name):
    if name.lower() =="admin":
        #return render_template("hello_user.html", username = "Yonetici")
        return redirect(url_for("admin"))
    else:
        return render_template("hello_user.html", username = name.title())

"""
@app.route("/add/<int:num1>/<int:num2>")
def add(num1,num2):
    calc = num1+ num2
    return render_template("add.html", num1 = num1, num2 = num2, result = calc)
"""

@app.route("/add") #http://localhost:PORT/add?number1=1&number2=3
def add():
    num1 = int(request.args["number1"])
    num2 = int(request.args["number2"])
    calc = num1+ num2
    return render_template("add.html", num1 = num1, num2 = num2, result = calc)

@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if "login_name" in request.form:
            username = request.form["login_name"]
            return redirect(url_for("hello_user", name = username))
    else:
        return render_template("login.html")

@app.route("/student")
def student():
    return render_template("student.html")

@app.route("/result", methods=['POST'])
def result():
    ContextData = {
    'name' : request.form["name"],
    'algo' : request.form["algo"],
    'lineer' : request.form["lineer"],
    'fizik' : request.form["fzk"]
    }
    #return render_template("student_result.html", name=name, algo=algo, lineer=lineer ,fizik = fizik)
    return render_template("student_result.html", **ContextData)