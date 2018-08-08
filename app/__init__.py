from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

def init_db():
	db.create_all()

from app.home_page import home_page

app.register_blueprint(home_page, url_prefix='/')
