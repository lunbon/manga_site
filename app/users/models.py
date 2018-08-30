from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, \
	check_password_hash

roles = db.Table('roles',
	db.Column('role_id', db.Integer, db.ForeignKey('role.id'), primary_key=True),
	db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
	)

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100, collation='NOCASE'),
			nullable=False,server_default='')
	password_hash = db.Column(db.String)
	about = db.Column(db.String(250), default='')
	group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
	avatar = db.Column(db.String, default='none')
	roles = db.relationship('Role', secondary=roles, lazy='subquery',
		backref=db.backref('users',lazy=True))

	def set_password(self,password):
		self.password_hash = generate_password_hash(password)
	def check_password(self, password):
		return check_password_hash(self.password_hash,password)
	def __repr__(self):
		return f"{self.name}({self.id})"

class Role(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), nullable=False,unique=True)
	def __repr__(self):
		return str(self.name)
		
class Group(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	members = db.relationship('User', backref='group', lazy=True)
	name = db.Column(db.String(50), nullable=False)
	boss_id = db.Column(db.Integer, nullable=False)
	def __repr__(self):
		return self.name