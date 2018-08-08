from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
	def tearDown(self):
		self.browser.quit()
	def test_can_open_site_and_find_titles(self):
		self.browser.get('http://localhost:5000')
		self.assertIn('Манга сайт', self.browser.title)

if __name__=='__main__':
	unittest.main()