import pytest
from models.group import Group

group_list = [Group("new name", "new header", "new footer"),
              Group("132214", "12423", "1234325"),
              Group("@$#%&", "^$#%^&&", "%^&&*(&"),
              Group("Кирилица", "РПСлтдлфыв", "Два слова")]


@pytest.mark.parametrize("group", group_list)
def test_create_group(app, init_login, group):
    app.open_group_page()
    app.create_group(group)
    assert app.message_page.is_this_page()
    assert "A new group has been entered into the address book." in app.message_page.message_box.text
    app.return_to_group_page()

