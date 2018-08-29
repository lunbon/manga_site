from flask import Blueprint

titles = Blueprint('titles',__name__,
		template_folder='templates')

from app.titles import models, routes


