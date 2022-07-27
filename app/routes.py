from app import app


@app.route("/")
def index():
    user = "CarlosViniMSouza"
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
