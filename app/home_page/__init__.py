from flask import Blueprint

home_page = Blueprint('home_page',__name__,
		template_folder='templates')

from app.home_page import routes