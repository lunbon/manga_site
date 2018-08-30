from . import moder
from .models import Changes
from app.titles.models import Title
from app.users.models import Role
from flask import render_template, abort
from flask_login import current_user

@moder.route('/new_title')
def add_title_requests():
	moder = Role.query.filter_by(name='moder').first_or_404()
	if moder in current_user.roles:
		titles = Title.query.filter_by(is_active=False).all()
		return render_template('admin/new_requests.html',titles=titles)	
	else:
		abort(404)

@moder.route('/history')
def history():
	changes = Changes.query.all()
	return render_template('admin/history.html',history=changes)