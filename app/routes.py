from flask import render_template
from app import app


@app.route("/")
def index():
    user = "CarlosViniMSouza"
<<<<<<< HEAD
    return """
    <html>
        <head>
            <title> blog Flask Tutorial </title>
        </head>
        <body>
            <h2> Hello """ + user + """! </h2>
        </body>
    </html>
    """
=======
    posts = [
        {
            "username": "Carlos",
            "title": "Intro the Flask Framework",
            "subtitle": "A simple tutorial about Flask",
            "posted": True
        },

        {
            "username": "Vinicius",
            "title": "Intro the Django Ecossystem",
            "subtitle": "A tutorial about Django and DjangoRest",
            "posted": False
        },

        {
            "username": "De Souza",
            "title": "Intro the FastAPI",
            "subtitle": "A simple tutorial about RestAPIs with FastAPI",
            "posted": True
        },
    ]

    return render_template("base.html", title="blog Flask", user=user, posts=posts)
>>>>>>> 5e094a6c20fc7010642c55950bc16e977d38bea5
