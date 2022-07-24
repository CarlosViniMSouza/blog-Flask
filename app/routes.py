from app import app

@app.route("/")
@app.route("/index")
def index():
    return "<h4> Hello World! (by: Flask) </h4>"