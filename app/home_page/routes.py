from . import home_page
from flask import render_template

@home_page.route('/')
def view_home_page():
	return render_template('home_page/home_page.html')