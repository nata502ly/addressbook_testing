import allure

@allure.feature("Group feature")
@allure.story("Group creation story")
def test_create_group(app, init_login, group, db):
    old_group_list = db.get_groups()
    app.open_group_page()
    app.create_group(group)
    message = "A new group has been entered into the address book."

    with allure.step('THEN a message "{}" appears'.format(message)):
        assert app.message_page.is_this_page()
        assert message in app.message_page.message_box.text

    app.return_to_group_page()
    # Full verification new group existing in database
    with allure.step("THEN a new group in group list"):
        new_group_list = db.get_groups()
        assert len(old_group_list) + 1 == len(new_group_list)
        assert old_group_list == new_group_list[:-1]
        assert new_group_list[-1]["group_name"] == group.name
        assert new_group_list[-1]["group_header"] == group.header
        assert new_group_list[-1]["group_footer"] == group.footer
