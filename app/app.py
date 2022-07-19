from app import app


@app.route("/")
def hello():
    return "<h1> Homepage</h2>"

if __name__== '__main__':
    app.run()