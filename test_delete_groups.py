def test_delete_first_group(app, init_login):
    app.open_group_page()
    app.delete_group(number=0)
    app.return_to_group_page()
