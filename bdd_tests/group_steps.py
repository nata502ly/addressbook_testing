from pytest_bdd import  given, when, then
from models.group import Group


@given("a group list")
def old_group_list(db):
    return db.get_groups()


@given("data for new group with <name>, <header>, <footer>")
def new_group(name, header, footer):
    return Group(name, header, footer)


@when("I add a new group with this data")
def create_group(app, init_login, new_group):
    app.open_group_page()
    app.create_group(new_group)


@then("correct message is displayed")
def message_verification(app):
    assert app.message_page.is_this_page()
    assert "A new group has been entered into the address book." in app.message_page.message_box.text


@then("a new group list is equal to the old group with this new group")
def verification_new_group_exist(db, old_group_list, new_group):
    new_group_list = db.get_groups()
    assert len(old_group_list) + 1 == len(new_group_list)
    assert old_group_list == new_group_list[:-1]
    assert new_group_list[-1]["group_name"] == new_group.name
    assert new_group_list[-1]["group_header"] == new_group.header
    assert new_group_list[-1]["group_footer"] == new_group.footer
