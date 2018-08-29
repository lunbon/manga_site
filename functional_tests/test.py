from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

site_url = 'http://localhost:5000/'

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
	def tearDown(self):
		self.browser.quit()
	def test_can_open_site_and_find_title(self):
		self.browser.get(site_url)
		self.assertIn('Манга сайт', self.browser.title)

def register(name, password):
	browser = webdriver.Firefox()
	browser.get(site_url+'user/register')
	inputbox = browser.find_element_by_id('username')
	inputbox.send_keys(name)
	inputbox = browser.find_element_by_id('password')
	inputbox.send_keys(password)
	inputbox.send_keys(Keys.ENTER)
	browser.quit()

class ProfileVisitor(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
	def tearDown(self):
		self.browser.quit()

	def test_visit_registred_pofile(self):
		register('Saske','password')
		time.sleep(1)
		self.browser.get(site_url+'user/Saske')
		owner=self.browser.find_element_by_tag_name('h1')
		self.assertEqual(owner.text,'Saske')

	def test_request_for_unregistred_user(self):
		self.browser.get(site_url+'user/@aske')
		owner=self.browser.find_element_by_tag_name('h1')
		self.assertEqual(owner.text,'Not Found')

class ChapterLoader(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
	def tearDown(self):
		self.browser.quit()

	def test_user_can_upload_a_chapter(self):
		self.browser.get(site_url+'title/upload')
		
		inputbox = self.browser.find_element_by_id('add_new_chapter_name')
		inputbox.send_keys('Lily')
		
		inputbox = self.browser.find_element_by_id('add_new_chapter_img')
		img_src='https://cdn.discordapp.com/attachments/461144491362091010/473745374025089024/img000003.png_res.jpg'
		inputbox.send_keys(img_src)
		inputbox.send_keys(Keys.ENTER)
		
		time.sleep(1)

		self.browser.get(site_url)
		last_chapter = self.browser.find_element_by_tag_name('p')
		last_poster = self.browser.find_element_by_tag_name('img')
		self.assertEqual(last_chapter.text, "Lily")
		self.assertEqual(last_poster.get_attribute('src'), img_src)


if __name__=='__main__':
	unittest.main()