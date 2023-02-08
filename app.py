from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("home.html")


@app.route("/gallery/")
def gallery():
    return render_template("gallery.html")


@app.route("/contact/")
def contact():
    return render_template("contact.html")


@app.route("/name/")
@app.route("/name/<username>")
def name(username="Friend!"):
    return render_template("name.html", username=username)
