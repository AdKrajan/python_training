# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from contact import Contact

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_contact (unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette":False})
        self.wd.implicitly_wait(60)
    
    def test_add_contact(self):
        self.login("admin", "secret")
        self.fill_contact_form(Contact(first_name="FirstName", last_name="LastName", nick="nick", home_phone="999-000-111", mobile_phone="888-000-222", email="test@test.pl"))
        self.logout()


    def test_add_empty_contact(self):
        self.login("admin", "secret")
        self.fill_contact_form(Contact(first_name="", last_name="", nick="", home_phone="", mobile_phone="", email=""))
        self.logout()

    def back_to_contacts_list(self):
        wd = self.wd
        wd.find_element_by_link_text("home").click()

    def logout(self):
        # logout
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def fill_contact_form(self, contact):
        # fill contacts form
        wd = self.wd
        self.open_add_contact_page()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nick)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_phone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile_phone)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.back_to_contacts_list()

    def open_add_contact_page(self):
        # open add creation new contact
        wd = self.wd
        wd.find_element_by_link_text("add new").click()

    def login(self, username, password):
        # login
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_home_page(self):
        # open home page
        wd = self.wd
        wd.get("http://localhost:8080/addressbook/")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
