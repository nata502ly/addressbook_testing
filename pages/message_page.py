from pages.internal_page import InternalPage
from selenium.webdriver.common.by import By


class MessagePage(InternalPage):
    def is_this_page(self):
        return self.is_element_present(By.CLASS_NAME, "msgbox")


    @property
    def message_box(self):
        return self.driver.find_element_by_class_name("msgbox")
