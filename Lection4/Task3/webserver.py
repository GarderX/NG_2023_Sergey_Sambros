from flask import Flask, render_template, request
import os

directory = 'C:\\NG_2023_Sergey_Sambros\\Lection4\\Task3'
os.chdir(directory)

app = Flask("Lection4_Task3")

def images_gallery():
    images = []

    for file in os.listdir("static/images/"):
        if file.endswith(('.jpg')):
            images.append(file)

    return images

pictures = images_gallery()
images_list = 0

@app.route("/")
def index():
 return render_template("index.html", images = pictures, images_list=images_list)

@app.route("/previous")
def previous():
    global images_list
    if images_list > 0:
        images_list -= 1
    return index()

@app.route("/next")
def next():
    global images_list
    if images_list < len(pictures) - 1:
        images_list += 1
    return index()

app.run(host="0.0.0.0", port=8080)