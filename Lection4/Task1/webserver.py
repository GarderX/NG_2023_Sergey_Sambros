from flask import Flask, render_template, request
import os

directory = 'C:\\NG_2023_Sergey_Sambros\\Lection4\\Task1'
os.chdir(directory)

webserver = Flask("Lesson_4, Task1")

@webserver.route("/")
def index():
    return render_template("index.html", data="TEST")

@webserver.route("/ask")
def ask():
    return render_template("ask.html")

@webserver.route("/calculate")
def calculate():
    firstValue = float(request.args.get("valuea"))
    secondValue = float(request.args.get("valueb"))
    operation = request.args.get("operation")
    if operation == "Add":
        return str(firstValue + secondValue)
    elif operation == "Divide":
        return str(firstValue / secondValue)
    elif operation == "Multiply":
        return str(firstValue * secondValue)
    elif operation == "Difference":
        return str(firstValue - secondValue)
webserver.run(host="0.0.0.0", port=8080)