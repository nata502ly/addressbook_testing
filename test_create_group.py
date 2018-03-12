import pytest

group_names = ["new name", "1124", ")(&%$%", "Кирилица"]


@pytest.mark.parametrize("group_name", group_names)
def test_create_group(app, init_login, group_name):
    group_header = "new header"
    group_footer = "new footer"
    app.open_group_page()
    app.create_group(group_name, group_header, group_footer)
    assert app.message_page.is_this_page()
    assert "A new group has been entered into the address book." in app.message_page.message_box.text
    app.return_to_group_page()

