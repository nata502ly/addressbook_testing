def test_create_group(app, init_login):
    app.open_group_page()
    app.create_group("new name", "new header", "new footer")
    app.return_to_group_page()


def test_delete_first_group(app, init_login):
    app.open_group_page()
    app.delete_group(number=0)
    app.return_to_group_page()
