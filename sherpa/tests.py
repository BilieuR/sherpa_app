# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create your tests here.


class AccountRegisterTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(AccountRegisterTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(AccountRegisterTestCase, self).tearDown()

    def test_register(self):
        selenium = self.selenium
        # Opening the application for testing
        selenium.get('localhost:8000/sherpa/register/')

        # find the form element
        first_name = selenium.find_element_by_id('id_first_name')
        last_name = selenium.find_element_by_id('id_last_name')
        email = selenium.find_element_by_id('id_email')
        phone = selenium.find_element_by_id('id_phone')
        user_type = selenium.find_element_by_id('id_user_type')
        username = selenium.find_element_by_id('id_username')
        password1 = selenium.find_element_by_id('id_password1')
        password2 = selenium.find_element_by_id('id_password2')

        submit = selenium.find_element_by_id('register')

        # Fill the form with data
        first_name.send_keys('Bilieu')
        last_name.send_keys('Reath')
        email.send_keys('user@example.com')
        phone.send_keys('0473555124')
        user_type.select_by_value('2')
        username.send_keys('user37')
        password1.send_keys('123456')
        password2.send_keys('123456')

        # submitting the form
        submit.send_keys(Keys.RETURN)
