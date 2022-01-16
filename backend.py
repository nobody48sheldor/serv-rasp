from flask import Flask, render_template, request, send_from_directory, current_app
import os
from werkzeug.utils import secure_filename
import shutil

#path = ["home", "pi", "Desktop"]
path = ["home", "arnaud", "Desktop"]
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
            try:
                folder = request.form['cliquedfile']
            except:
                None
        if folder == "":
            try:
                savefile = request.files['upload']
                PATH = ""
                for i in path:
                    PATH = PATH + "/" + i
                savefile.save(secure_filename(savefile.filename))
                dest = shutil.move(savefile.filename, PATH, copy_function = shutil.copytree)
            except:
                None
        if folder == "":
            try:
                Dfile = request.form['download']
                PATH = ""
                for i in path:
                    PATH = PATH + "/" + i
                #send_from_directory(directory=PATH, path=Dfile)
                return(send_from_directory(directory=PATH, path=Dfile, as_attachment=True, max_age=0))
            except:
                None
        if folder == "":
            try:
                Delfile = request.form['delet']
                PATH = ""
                for i in path:
                    PATH = PATH + "/" + i
                #send_from_directory(directory=PATH, path=Dfile)
                os.remove(PATH + "/" + Delfile)
            except:
                None
        if folder == "":
            try:
                Deldir = request.form['deletdir']
                PATH = ""
                for i in path:
                    PATH = PATH + "/" + i
                os.rmdir(PATH + "/" + Deldir)
            except:
                None
        if folder == "":
            try:
                makedir = request.form['makedir']
                PATH = ""
                for i in path:
                    PATH = PATH + "/" + i
                os.mkdir(PATH + "/" + makedir)
            except:
                None
        if folder == "":
            try:
                file = request.form['renamefile']
                newname = request.form['rename']
                PATH = ""
                print(file, ", ", newname)
                for i in path:
                    PATH = PATH + "/" + i
                os.rename(PATH + "/" + file, PATH + "/" + newname)
            except:
                None
        if folder == "":
            try:
                file = request.form['movefile']
                newpath = request.form['movepath']
                PATH = ""
                for i in path:
                    PATH = PATH + "/" + i
                shutil.move(PATH + "/" + file, PATH + "/" + newpath)
            except:
                None
        if folder == "..":
            if len(path) > 3:
                path.pop(len(path) - 1)
            else:
                return(render_template("index.html"))
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
    print(PATH)
    return(render_template("browse.html", files = dir, path = PATH, d = False))

@app.route("/file=<file>")
def search(file):
    return()

if __name__ == "__main__":
    app.run(debug=True)
