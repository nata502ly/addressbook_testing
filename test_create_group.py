from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest


class TestCreateGroup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.base_url = "http://localhost/addressbook/"
        self.driver.get(self.base_url)

    def test_create_group(self):
        driver = self.driver
        # Login (precondition)
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_css_selector('#LoginForm > input[type="submit"]').click()
        # Open group page
        driver.find_element_by_css_selector('#nav > ul > li.admin > a').click()
        # Creating group:
        # 1. Initialization group create
        driver.find_element_by_name("new").click()
        # 2. Fill form
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys("new name")
        driver.find_element_by_name("group_header").click()
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys("new header")
        driver.find_element_by_name("group_footer").click()
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys("new footer")
        # 3. Submit group
        driver.find_element_by_name("submit").click()
        # Return to group page
        driver.find_element_by_link_text("group page").click()
        # Logout (postcondition)
        driver.find_element_by_css_selector("form[name=logout] > a").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
