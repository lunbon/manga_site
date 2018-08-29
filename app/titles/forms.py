from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, TextAreaField
from wtforms.validators import DataRequired

class AddChapterForm(FlaskForm):
	name = StringField('name', validators=[DataRequired()])
	img = StringField('img',validators=[DataRequired()])
	submit = SubmitField()

class AddTitleForm(FlaskForm):
	name = StringField('name', validators=[DataRequired()])
	img = StringField('img',validators=[DataRequired()])
	desc = StringField('desc')
	submit = SubmitField()