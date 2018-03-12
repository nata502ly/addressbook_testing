def test_create_group(app, init_login):
    app.open_group_page()
    app.create_group("new name", "new header", "new footer")
    assert app.message_page.is_this_page()
    assert "A new group has been entered into the address book." in app.message_page.message_box.text
    app.return_to_group_page()
