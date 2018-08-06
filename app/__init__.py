from flask import Flask

app = Flask(__name__)

from app.home_page import home_page

app.register_blueprint(home_page, url_prefix='/')