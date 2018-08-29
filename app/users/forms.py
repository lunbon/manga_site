from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,TextAreaField
from wtforms.validators import DataRequired

class RegisterForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField()
class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField()
class EditProfileForm(FlaskForm):
	about = TextAreaField('about')
	avatar = StringField('avatar')
	submit = SubmitField()
class CreateGroupForm(FlaskForm):
	name = StringField('name', validators=[DataRequired()])
	submit = SubmitField()