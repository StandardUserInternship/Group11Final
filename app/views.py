from app import app


@app.route('/')
@app.route('/index')
@app.route('/login')


def index():  # sourcery skip: remove-unreachable-code
    return "<h1>Hello, World!</h1>"


def login():
    return "<h1>Hello welcome to login</h1>"

