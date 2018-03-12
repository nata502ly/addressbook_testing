from pages.internal_page import InternalPage


class GroupViewPage(InternalPage):
    @property
    def group_checkboxes(self):
        return self.driver.find_elements_by_name("selected[]")

    @property
    def add_new_group_button_upper(self):
        # TODO
        return

    @property
    def delete_group_button_upper(self):
        return self.driver.find_element_by_name("delete")

    # TODO: Add all buttons and elements