from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/action",methods=["POST"])
def Action():
    return