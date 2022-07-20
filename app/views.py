from app import app


@app.route('/')
@app.route('/index')


def index():  # sourcery skip: remove-unreachable-code
    return "<h1>Hello, World!</h1>"

