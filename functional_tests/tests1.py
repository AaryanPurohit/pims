# from selenium import webdriver
# from django.test import LiveServerTestCase
# from dashboard.models import Portfolio
# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# from django.urls import reverse
# import time
from selenium.webdriver.common.by import By
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
import time

import unittest

class TestFunctionalTests(StaticLiveServerTestCase):
    def setUp(self):
        self.browser =  webdriver.Chrome("functional_tests/chromedriver.exe")

    def tearDown(self) :
        self.browser.close()

    # def test_start(self):
    #     self.browser.get(self.live_server_url)
    #     time.sleep(20)


    # def test_login_button(self):
    #     # current_url= self.browser.current_url
    #     idElement = self.browser.find_elements(By.CLASS_NAME ,'login_button') # Locating element with ID
    #     idElement.click()
    #     self.assertEquals(self.browser.current_url,"http://localhost:53481//accounts/login/")

    # def test_location_element_by_id(self):
    #     # idElement = self.browser.find_element(By.ID, 'idElement') # Locating element with ID
    #     classElement = self.browser.find_elements(By.CLASS_NAME, 'login_button')
    #     classElement.click() # Invoking click event on an element.
    #     # self.assertEqual(classElement.text, "") #Making an assertion for an expected text.

    # def test_redirect(self):
    # #    self.browser = webdriver.Chrome("driver_path.exe")
    #    new_url = "https://alwaysdjango.com"
    #    self.browser.get(new_url)

    def test_redirect(self):
        self.browser = webdriver.Chrome("functional_tests/chromedriver.exe")
        current_url= self.browser.live_server_url
        self.assertEquals(current_url,"http://127.0.0.1:8000/dashboard")

# if __name__ == '__main__':
#     unittest.main()