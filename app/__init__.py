from flask import Flask


#initialize app

app = Flask(__name__, instance_relative_config=True)


from app import views




