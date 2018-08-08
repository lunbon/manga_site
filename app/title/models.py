from app import db

class Chapter(db.Model):
	id = db.Column(db.Integer(), primary_key=True)