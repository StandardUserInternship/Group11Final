from app import app

@app.views('/')
@app.views('/index')
def index():
    return "<h1>Hello, World!</h1>"