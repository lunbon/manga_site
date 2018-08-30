from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app,db)
admin = Admin(app)

from app.users.models import User

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view="users.login"
@login_manager.user_loader
def load_user(user_id):
	return User.query.get(user_id)

def init_db():
	db.create_all()

from app.home_page import home_page
from app.users import users
from app.titles import titles
from app.moder import moder

app.register_blueprint(home_page, url_prefix='/')
app.register_blueprint(users,url_prefix='/user')
app.register_blueprint(titles,url_prefix='/catalog')
app.register_blueprint(moder,url_prefix='/moder')

from app.titles.models import Title,Translation,Chapter

admin.add_view(ModelView(Title,db.session))
admin.add_view(ModelView(Translation,db.session))
admin.add_view(ModelView(Chapter,db.session))

from app.users.models import Role, Group

admin.add_view(ModelView(User,db.session))
admin.add_view(ModelView(Role,db.session))
admin.add_view(ModelView(Group,db.session))

from app.moder.models import Changes

admin.add_view(ModelView(Changes,db.session))