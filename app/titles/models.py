from app import db
from datetime import datetime
from app.users.models import User,Group

class Chapter(db.Model):
	id = db.Column(db.Integer(), primary_key=True)
	add_date = db.Column(db.DateTime(), default=datetime.utcnow)
	name = db.Column(db.String())
	img = db.Column(db.String())
	uploader_id = db.Column(db.Integer)
	translation_id = db.Column(db.Integer,db.ForeignKey('translation.id'))
	translation = db.relationship('Translation', 
			backref=db.backref('chapters', lazy=True,cascade="all, delete-orphan"))
	def __repr__(self):
		title = self.translation.title
		group = self.translation.group
		return "'{title.name}' - '{self.name}' - '{group.name}'"

class Translation(db.Model):
	id = db.Column(db.Integer(), primary_key=True)
	group_id = db.Column(db.Integer,db.ForeignKey('group.id'))
	group = db.relationship('Group', 
      backref=db.backref('translations', lazy=True))
	title_id = db.Column(db.Integer,db.ForeignKey('title.id'))
	title = db.relationship('Title', 
			backref=db.backref('translations', lazy=True))
	def __repr__(self):
		return f"'{self.title}' - '{self.group}'"

class Title(db.Model):
	id = db.Column(db.Integer(), primary_key=True)
	add_date = db.Column(db.DateTime(), default=datetime.utcnow)
	name = db.Column(db.String())
	img = db.Column(db.String())
	description = db.Column(db.String(),default='')
	is_active = db.Column(db.Boolean(),default=False)
	def __repr__(self):
		return f"'{self.name}'({self.id})"