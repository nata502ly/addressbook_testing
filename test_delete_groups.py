def test_delete_first_group(app, init_login):
    app.open_group_page()
    app.delete_group(number=0)
    assert app.message_page.is_this_page()
    assert "Group has been removed." in app.message_page.message_box.text
    app.return_to_group_page()
