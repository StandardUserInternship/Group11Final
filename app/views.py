from app import app

user = {'username': 'Philip'}

@app.route('/')
@app.route('/index')
# @login_required
def index():
    user = {'username': 'Philip'}
    return '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''