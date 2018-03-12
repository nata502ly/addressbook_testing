import pytest
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


group_list = [Group("new name", "new header", "new footer"),
              Group("132214", "12423", "1234325"),
              Group("@$#%&", "^$#%^&&", "%^&&*(&"),
              Group("Кирилица", "РПСлтдлфыв", "Два слова")]


@pytest.fixture(params=group_list, ids=[str(group) for group in group_list])
def group(request):
    return request.param
