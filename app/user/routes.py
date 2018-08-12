from . import user
from app import db
from .models import User
from .forms import RegisterForm
from flask import render_template
from flask import redirect
from flask_login import login_user

@user.route('/<name>')
def profile(name):
	user = User.query.filter_by(name=name).first_or_404()
	return render_template('user/profile.html', user=user)

@user.route('/register', methods=['GET','POST'])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		new_user = User(name=form.username.data)
		new_user.set_password(form.password.data)
		db.session.add(new_user)
		db.session.commit()
		login_user(user)
		return redirect(url_for('login'))
	return render_template('user/register.html', form=form)