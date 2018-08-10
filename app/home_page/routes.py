from . import home_page
from flask import render_template
from app.title.models import Chapter
from app.title.forms import AddChapterForm

@home_page.route('/', methods=['GET'])
def view_home_page():
	form=AddChapterForm()
	chapters = Chapter.query.order_by(Chapter.add_date.desc()).all()
	return render_template('home_page/home_page.html', chapters=chapters, form=form)