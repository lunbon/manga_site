from . import titles
from .forms import AddChapterForm, AddTitleForm
from .models import Chapter,Title, Translation
from app.users.models import User, Group, Role
from app import db
from flask import redirect, render_template, url_for,flash
from flask_login import login_required, current_user

@titles.route('/')
def catalog():
	titles=Title.query.filter_by(is_active=True).order_by(Title.add_date.desc()).all()
	return render_template('title/titles.html', titles=titles)

@titles.route('title/<title_id>/trans/<trans_id>/chapter/upload', methods=['GET','POST'])
@login_required
def add_chapter(title_id,trans_id):
	form = AddChapterForm()
	title = Title.query.filter_by(id=title_id).first_or_404()
	trans = Translation.query.filter_by(id=trans_id).first_or_404()
	group = trans.group
	if current_user.id != group.boss_id:
		return redirect('/')
	if form.validate_on_submit():
		new_chapter = Chapter(name=form.name.data,img=form.img.data, 
			uploader_id=current_user.id,translation=trans)
		db.session.add(new_chapter)
		db.session.commit()
		return redirect('/')
	return render_template('title/upload_chapter.html', form=form)

@titles.route('/title/<title_id>/add_translation',methods=['GET','POST'])
@login_required
def add_translation(title_id):
	group = Group.query.filter_by(boss_id=current_user.id).first()
	form = AddChapterForm()
	if group is None:
		flash('Вы должны возглавлять группу, чтобы добавлять главы')
		return redirect(url_for('users.create_group'))
	if Translation.query.filter_by(group=group).first():
		flash('Вы не можете добавить больше однонго перевода от команды')
		return redirect(url_for('titles.title_view',id=title_id))
	if form.validate_on_submit():
		new_chapter = Chapter(name=form.name.data,img=form.img.data, 
			uploader_id=current_user.id)
		title = Title.query.get(title_id)
		trans = Translation(title=title,group=group)
		new_chapter.translation = trans
		db.session.add(trans)
		db.session.add(new_chapter)
		db.session.commit()
		return redirect(url_for('titles.translation_view',title_id=title_id,trans_id=trans.id))
	return render_template('title/create_translation.html',form=form)

@titles.route('/title/create', methods=['GET', 'POST'])
@login_required
def add_title():
	form = AddTitleForm()
	if form.validate_on_submit():
		new_title = Title(name=form.name.data, img=form.img.data)
		new_title.uploaded_by = current_user
		new_title.desccription = form.desc.data
		db.session.add(new_title)
		db.session.commit()
		return redirect(url_for('titles.catalog'))
	return render_template('title/add_title.html', form=form)

@titles.route('/title/<id>/set_active')
def set_active(id):
	title = Title.query.filter_by(id=id).first_or_404()
	title.is_active=True
	db.session.add(title)
	db.session.commit()
	return redirect(url_for('moder.view_new_requests'))

@titles.route('title/delete/<id>')
@login_required
def delete_title(id):
	admin = Role.query.filter_by(name='admin').first_or_404()
	if admin in current_user.roles:
		title = Title.query.get(id)
		db.session.delete(title)
		db.session.commit()
		return redirect(url_for('admin.view_new_requests'))
	return redirect('/')

@titles.route('/title/<id>')
def title_view(id):
	title = Title.query.get(id)
	trans = title.translations
	groups = [trans.group for trans in trans]
	trans_and_groups = zip(trans,groups)
	return render_template('title/title.html', title=title, trans_and_groups=trans_and_groups)

@titles.route('/title/<title_id>/translation/<trans_id>')
def translation_view(title_id,trans_id):
	title = Title.query.get(title_id)
	trans = Translation.query.get(trans_id)
	group = trans.group
	return render_template('title/trans.html',title=title,trans=trans, group=group)