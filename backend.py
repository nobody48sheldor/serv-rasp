from flask import Flask, render_template, request
import os

path = ["home", "arnaud", "Desktop", "arnaud"]
PATH = ""

app = Flask(__name__)

@app.route("/")
def home():
    return(render_template("index.html"))

@app.route("/browse", methods=["POST", "GET"])
def browse():
    dir = []
    if request.method == "POST":
        dir = []
        folder = ""
        try:
            folder = request.form['files']
        except:
            None
        if folder == "" :
            folder = request.form['cliquedfile']
        if folder == "..":
            path.pop(len(path) - 1)
            #return(render_template("index.html"))
        else:
            path.append(folder)
        PATH = ""
        for i in path:
            PATH = PATH + "/" + i
        try:
            dir = os.listdir(PATH + "/")
        except FileNotFoundError:
            path.pop(len(path) - 1)
        except NotADirectoryError:
            path.pop(len(path) - 1)
            return(render_template("index.html"))
    else:
        PATH = ""
        for i in path:
            PATH = PATH + "/" + i
        dir = os.listdir(PATH + "/")
    dir.append("..")
    return(render_template("browse.html", files = dir, path = PATH))

@app.route("/file=<file>")
def search(file):
    return()

if __name__ == "__main__":
    app.run()
