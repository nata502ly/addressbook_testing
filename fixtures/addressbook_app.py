import allure
from pages.login_page import LoginPage
from pages.internal_page import InternalPage
from pages.groups_pages.groups_view_page import GroupViewPage
from pages.message_page import MessagePage


class AddressbookApp:
    def __init__(self, driver, base_url="http://localhost/addressbook"):
        self.driver = driver
        self.driver.implicitly_wait(5)
        self.base_url = base_url
        self.driver.get(self.base_url)
        # Pages:
        self.login_page = LoginPage(self.driver)
        self.internal_page = InternalPage(self.driver)
        self.group_view_page = GroupViewPage(self.driver)
        self.message_page = MessagePage(self.driver)

    @allure.step("I log as {username}")
    def login(self, username, password):
        self.login_page.username_field.clear()
        self.login_page.username_field.send_keys(username)
        self.login_page.password_field.clear()
        self.login_page.password_field.send_keys(password)
        self.login_page.submit_button.click()

    @allure.step("I logout")
    def logout(self):
        self.internal_page.logout_button.click()

    @allure.step("WHEN I open a group page")
    def open_group_page(self):
        self.internal_page.group_menu.click()

    @allure.step("WHEN I return to group page")
    def return_to_group_page(self):
        self.driver.find_element_by_link_text("group page").click()

    @allure.step("WHEN I add a new group {1}")
    def create_group(self, group):
        driver = self.driver
        # 1. Initialization group create
        driver.find_element_by_name("new").click()
        # 2. Fill form
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").click()
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys(group.header)
        driver.find_element_by_name("group_footer").click()
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys(group.footer)
        # 3. Submit group
        driver.find_element_by_name("submit").click()

    @allure.step("WHEN I delete {number} group")
    def delete_group(self, number):
        checkboxes = self.group_view_page.group_checkboxes
        if not checkboxes[number].is_selected():
            checkboxes[number].click()
        self.group_view_page.delete_group_button_upper.click()

    def close(self):
        self.driver.quit()
