from app.home_page import home_page

@home_page.route('/')
def home_page():
	return "<html><head><title>manga-site</title></head></html>"