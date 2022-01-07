from flask import Flask, render_template, request

PATH = ""

app = Flask(__name__)

@app.route("/")
def home():
    return(render_template("index.html"))

@app.route("/browse", methods=["POST", "GET"])
def browse():
    if request.method == "POST":
        path = request.form['files']
        print(path)
    return(render_template("browse.html"))

@app.route("/file=<file>")
def search(file):
    return()

if __name__ == "__main__":
    app.run()
