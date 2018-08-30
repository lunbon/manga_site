from app import db

class Changes(db.Model):
	id = db.Column(db.Integer(), primary_key=True)
	desc = db.Column(db.String(100))
	model = db.Column(db.String(50)) #title/user/chapter
	def __repr__(self):
		return self.desc