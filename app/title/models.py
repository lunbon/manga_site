from app import db

class Chapter(db.Model):
	id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.String(), unique=True)
	img = db.Column(db.String())