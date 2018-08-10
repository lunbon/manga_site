from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class AddChapterForm(FlaskForm):
	name = StringField('name', validators=[DataRequired()])
	img = StringField('img',validators=[DataRequired()])
	submit = SubmitField()