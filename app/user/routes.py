from . import user
from .models import User
from flask import render_template

@user.route('/<name>')
def profile(name):
	user = User.query.filter_by(name=name).first_or_404()
	return render_template('user/profile.html', user=user)
