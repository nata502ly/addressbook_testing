from pages.base_pages import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    @property
    def username_field(self):
        return self.driver.find_element_by_name("user")

    @property
    def password_field(self):
        return self.driver.find_element_by_name("pass")

    @property
    def submit_button(self):
        return self.driver.find_element_by_css_selector('#LoginForm > input[type="submit"]')

    def is_this_page(self):
        return self.is_element_present(By.ID, "LoginForm")


if __name__ == "__main__":
    from selenium import webdriver
    dr = webdriver.Chrome()
    dr.get("http://localhost/addressbook/")
    lg = LoginPage(driver=dr)
    lg.username_field.send_keys("admin")
    lg.password_field.send_keys("secret")
    lg.submit_button.click()
    dr.quit()
