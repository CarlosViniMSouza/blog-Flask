from flask import render_template
from app import app

@app.route("/")
@app.route("/index")
def index():
    user = "CarlosViniMSouza"
    return render_template("index.html", title="blog Flask", user=user)