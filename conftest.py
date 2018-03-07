import pytest
from fixtures.addressbook_app import AddressbookApp


@pytest.fixture()
def app():
    app = AddressbookApp()
    yield app
    app.close()


@pytest.fixture()
def init_login(app):
    app.login(username="admin", password="secret")
    yield
    app.logout()
