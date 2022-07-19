from app import app

@app.views('/')
@app.views('/index')
def index():
    return "Hello, World!"