from flask import Flask, render_template, request

webserver = Flask("Lesson_4, Task1")

@webserver.route("/")
def index():
    return render_template("index.html")

@webserver.route("/calculate", methods=['POST'])
def calculate():
    firstValue = float(request.form.get("valuea"))
    secondValue = float(request.form.get("valueb"))
    operation = request.form.get("operation")
    if operation == "Add":
        return str(firstValue + secondValue)
    elif operation == "Divide":
        return str(firstValue / secondValue)
    elif operation == "Multiply":
        return str(firstValue * secondValue)
    elif operation == "Difference":
        return str(firstValue - secondValue)

webserver.run(host="0.0.0.0", port=8080)
