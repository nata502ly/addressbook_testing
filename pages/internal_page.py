from pages.base_pages import BasePage
from selenium.webdriver.common.by import By


class InternalPage(BasePage):
    @property
    def main_menu(self):
        # TODO
        return

    @property
    def add_contact_menu(self):
        # TODO
        return

    @property
    def group_menu(self):
        return self.driver.find_element_by_css_selector('#nav > ul > li.admin > a')

    # TODO: all other menus elements

    @property
    def logout_button(self):
        return self.driver.find_element_by_css_selector("form[name=logout] > a")

    def is_this_page(self):
        return self.is_element_present(By.CSS_SELECTOR, "#nav > ul")
