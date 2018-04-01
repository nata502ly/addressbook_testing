import random
import allure


@allure.feature("Group feature")
@allure.story("Group deletion story")
def test_delete_random_group(app, init_login):
    app.open_group_page()
    random_number = random.randrange(0, len(app.group_view_page.group_checkboxes))
    app.delete_group(number=random_number)
    message = "Group has been removed."

    with allure.step('THEN a message "{}" appears'.format(message)):
        assert app.message_page.is_this_page()
        assert "Group has been removed." in app.message_page.message_box.text

    app.return_to_group_page()

