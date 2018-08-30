from flask import Blueprint

moder = Blueprint('moder',__name__,
		template_folder='templates')

from . import routes, models