from flask import Flask 

servak = Flask ("Lesson_5")

@servak.route("/")
def index():
    cities = ["Hg", "adaw", 3215, "aw"]
    return cities


@servak.route("/sup")
def index2():
    return "sup"

servak.run(host = "0.0.0.0", port=8080)