from flask import Flask
<<<<<<< .merge_file_a18712
import os
=======
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
>>>>>>> .merge_file_a06644

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
#initialize app

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

from app import views, models



<<<<<<< .merge_file_a18712
#load the config file
app.config['SECRET_KEY'] = 'you-will-never-guess'
#app.config.from_object('config')
=======

>>>>>>> .merge_file_a06644
