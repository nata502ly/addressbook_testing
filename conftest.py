import pytest
import json
from fixtures.addressbook_app import AddressbookApp
from models.group import Group


@pytest.fixture(scope="session")
def app():
    app = AddressbookApp()
    yield app
    app.close()


@pytest.fixture()
def init_login(app):
    app.login(username="admin", password="secret")
    yield
    app.logout()


with open("group_data.json", encoding="utf8") as f:
    group_list = json.load(f)


@pytest.fixture(params=group_list, ids=[str(group) for group in group_list])
def group(request):
    return Group(**request.param)
