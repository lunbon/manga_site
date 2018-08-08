import os
import tempfile

import pytest

from app import app 
from app import init_db
from app.title.models import Chapter
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

@pytest.fixture
def client():
	db_fd, app.config["DATABASE"] = tempfile.mkstemp()
	app.config["TESTING"] = True
	client = app.test_client()

	with app.app_context():
		init_db()
	yield client

	os.close(db_fd)
	os.unlink(app.config["DATABASE"])

def test_home_page(client):
	rv = client.get('/')
	assert b'<!DOCTYPE html>' in rv.data

def test_last_chapters_on_home_page(client):
	for chapter in Chapter.query.all():
		assert bytes(chapter.name, encoding='utf-8') in client.get('/').data
