from . import moder
from app.titles.models import Title
from flask import render_template

@moder.route('/')
def view_new_requests():
	titles = Title.query.filter_by(is_active=False).all()
	return render_template('admin/new_requests.html',titles=titles)	