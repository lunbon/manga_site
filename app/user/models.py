from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, \
	check_password_hash

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100, collation='NOCASE'),
			nullable=False,server_default='')
	password_hash = db.Column(db.String)

	def set_password(self,password):
		self.password_hash = generate_password_hash(password)
	def check_password(self, password):
		return check_password_hash(self.password_hash,password)