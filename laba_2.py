from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/test")
def test():
    return "<p>Test</p>"

@app.route("/name/<user>")
def name(user):
    print(user)
    return "<p>Привет, {}</p>".format(user)

@app.route("/calc/sum/<a>/<b>")
def calc_sum(a, b):
    a=int(a)
    b=int(b)
    c = a + b
    return "<p>Сумма, {}</p>".format(c)

@app.route("/calc/sub")
def calc_sub():
    args_dict = request.args
    print(args_dict)
    a = float(args_dict["a"])
    b = float(args_dict["b"])
    c = a - b
    return "<p>Вычитание, {}</p>".format(c)

@app.route("/calc/multiple/<a>/<b>")
def calc_mult(a, b):
    a=int(a)
    b=int(b)
    c = a * b
    return "<p>Умножение, {}</p>".format(c)

@app.route("/calc/division/<a>/<b>")
def calc_div(a, b):
    a=int(a)
    b=int(b)
    c = a / b
    return "<p>Деление, {}</p>".format(c)

@app.route("/test/aboba")
def aboba_test():
    return "<p>Test na abobu uteryan</p>"

@app.route("/food")
def food():
    args_dict = request.args
    p = args_dict["первое"]
    v = args_dict["второе"]
    c = 0
    q = 0
    if p == "суп":
        c = 100
    elif p == "борщ":
        c = 150
    elif p == "щи":
        c = 50

    if v == "греча":
        q = 100
    elif v == "рыс":
        q = 150
    elif v == "пюрешка":
        q = 50
    f = q + c
    return "Стоимость за {} и {}: {}".format(p, v, f)

@app.route("/father/<name>")
def whoyourfather(name):
    return '<img src="http://localhost:5000/static/{}.jpg" width = "500" high = "600" >'.format(name)
        