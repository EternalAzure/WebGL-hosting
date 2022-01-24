from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Navigate games by adding '/<int>' to this web address eg. eternalazure-web-hosting.herokuapp.com/01"

@app.route("/01")
def first():
    return render_template("index01.html")

@app.route("/02")
def second():
    return render_template("index02.html")