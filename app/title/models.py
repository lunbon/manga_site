from app import db
from datetime import datetime

class Chapter(db.Model):
	id = db.Column(db.Integer(), primary_key=True)
	add_date = db.Column(db.DateTime(), default=datetime.utcnow)
	name = db.Column(db.String(), unique=True)
	img = db.Column(db.String())