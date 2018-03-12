import pytest

group_names = ["new name", "1124", ")(&%$%", "Кирилица"]
group_headers = ["new header", "45636", "!@#@$", "РПСлтдлфыв"]
group_footers = ["new footer", "@$%%@%", "@$#%", "РПСлтдлфыв"]


@pytest.mark.parametrize("group_footer", group_footers)
@pytest.mark.parametrize("group_header", group_headers)
@pytest.mark.parametrize("group_name", group_names)
def test_create_group(app, init_login, group_name, group_header, group_footer):
    app.open_group_page()
    app.create_group(group_name, group_header, group_footer)
    assert app.message_page.is_this_page()
    assert "A new group has been entered into the address book." in app.message_page.message_box.text
    app.return_to_group_page()

