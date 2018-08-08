import os
import tempfile

import pytest

from app import app 
from app import init_db
from app.title.models import Chapter
from flask_sqlalchemy import SQLAlchemy

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

def test_db_chapter_model(client):
	
	with app.app_context():
		db=SQLAlchemy(app)
		init_db()
	
	old_chapter = Chapter()
	old_chapter.name = "Lili"
	db.session.add(old_chapter)
	db.session.commit()
	new_chapter = Chapter.query.get(1)
	assert new_chapter != old_chapter
 