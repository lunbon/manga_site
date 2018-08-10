from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
	def tearDown(self):
		self.browser.quit()
	def test_can_open_site_and_find_titles(self):
		self.browser.get('http://localhost:5000')
		self.assertIn('Манга сайт', self.browser.title)
	def test_can_add_a_new_chapter(self):
		self.browser.get('http://localhost:5000')
		inputbox = self.browser.find_element_by_id('add_new_chapter')
		inputbox.send_keys('New Chapter')
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)
		last_chapter = self.browser.find_element_by_tag_name('h1')
		self.assertEqual(last_chapter.text, "New Chapter")
		
if __name__=='__main__':
	unittest.main()