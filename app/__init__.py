from flask import Flask
import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
#initialize app

app = Flask(__name__, instance_relative_config=True)

from app import views

#load the config file
app.config['SECRET_KEY'] = 'you-will-never-guess'
#app.config.from_object('config')
