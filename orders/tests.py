import unittest
from selenium import webdriver


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.driver.set_window_size(1120, 550)

    def test_login_page(self):
        self.driver.get("https://fdxsalesuat.foliodx.com/")
        self.driver.find_element_by_id(
            'LoginName').send_keys("todd.kovalsky")
        self.driver.find_element_by_name(
            'LoginPwd').send_keys("Fdx12345")
        self.driver.find_element_by_class_name('login_butt_new').click()
        self.driver.get("https://qa8.foliodx.com/brokerage/AControlServlet")


        #self.driver.find_element_by_id("Login").click()
        #self.assertIn(
        #    "https://fdxsalesuat.foliodx.com/brokerage/AControlServlet", self.driver.current_url
        #)

    def tearDown(self):
        self.driver.quit()

'''
class TestFail(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.driver.set_window_size(1120, 550)

    def test_logged_in_home(self):
        self.driver.get("https://fdxsalesuat.foliodx.com/")
        self.driver.find_element_by_id(
            'LoginName').send_keys("todd.kovalsky")
        self.driver.find_element_by_name(
            'LoginPwd').send_keys("Fdx12345")
        self.driver.find_element_by_class_name('login_butt_new').click()
        self.driver.get("https://qa8.foliodx.com/brokerage/AControlServlet")
        self.driver.find_element_by_id(
            'component-1fsdfasdfasdf128')

    def tearDown(self):
        self.driver.quit()


class TestTitle(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.driver.set_window_size(1120, 550)

    def test_page_title(self):
        self.assertEqual(self.driver.title,'Folio Dynamix Sponsor')

    def tearDown(self):
        self.driver.quit()

'''

if __name__ == '__main__':
    unittest.main()
