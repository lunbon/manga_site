from . import users
from app import db
from .models import User, Group
from app.titles.models import Chapter
from .forms import RegisterForm, LoginForm, EditProfileForm, CreateGroupForm
from flask import render_template
from flask import redirect, url_for, flash
from flask_login import login_user, current_user, login_required, logout_user

@users.route('/<name>')
def profile(name):
	user = User.query.filter_by(name=name).first_or_404()
	return render_template('user/profile.html', user=user)

@users.route('/edit_profile', methods=['GET','POST'])
@login_required
def edit_profile():
	form = EditProfileForm()
	if form.validate_on_submit():
		current_user.about = form.about.data
		current_user.avatar = form.avatar.data
		db.session.commit()
		return redirect(url_for('user.profile', name=current_user.name))
	form.about.data = current_user.about
	form.avatar.data = current_user.avatar
	return render_template('user/edit_profile.html',form=form)	

@users.route('/register', methods=['GET','POST'])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		new_user = User(name=form.username.data)
		new_user.set_password(form.password.data)
		db.session.add(new_user)
		db.session.commit()
		login_user(new_user)
		return redirect(url_for('users.profile', name=new_user.name))
	return render_template('user/register.html', form=form)

@users.route('/login',methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(name=form.username.data).first()
		if user and user.check_password(form.password.data):
			login_user(user)
			return redirect('/')
		else:
			flash('Неправильный пароль')
	return render_template('user/login.html', form=form)
@users.route('/logout')
def logout():
	logout_user()
	return redirect('/')

@users.route('/create_group',methods=['GET','POST'])
@login_required
def create_group():
	form = CreateGroupForm()
	if form.validate_on_submit():
		group = Group(name=form.name.data, boss_id=current_user.id)
		current_user.group = group
		db.session.add(group)
		db.session.commit()
		return redirect('/')
	return render_template('user/create_group.html', form=form)