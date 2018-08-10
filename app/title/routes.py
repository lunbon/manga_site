from . import title
from .forms import AddChapterForm
from .models import Chapter
from app import db
from flask import redirect

@title.route('/add_chapter', methods=['GET','POST'])
def add_chapter():
	form = AddChapterForm()
	if form.validate_on_submit():
		new_chapter = Chapter(name=form.name.data, img=form.img.data)
		db.session.add(new_chapter)
		db.session.commit()
	return redirect('/')