from flask import Flask
from config import Config

#initialize app

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(Config)

from app import views




