from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

def init_db():
	db.create_all()

from app.home_page import home_page
from app.title import title
from app.user import user

app.register_blueprint(home_page, url_prefix='/')
app.register_blueprint(title,url_prefix='/title')
app.register_blueprint(user,url_prefix='/user')