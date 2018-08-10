from flask import Blueprint

title = Blueprint('title',__name__,
		template_folder='templates')

from app.title import models, routes


