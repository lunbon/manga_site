from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

from app.user.models import User
login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
	return User.query.get(user_id)

def init_db():
	db.create_all()

from app.home_page import home_page
from app.title import title
from app.user import user

app.register_blueprint(home_page, url_prefix='/')
app.register_blueprint(title,url_prefix='/title')
app.register_blueprint(user,url_prefix='/user')