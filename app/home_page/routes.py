from . import home_page
from flask import render_template
from app.title.models import Chapter

@home_page.route('/')
def view_home_page():
	chapters = Chapter.query.all()
	return render_template('home_page/home_page.html', chapters=chapters)