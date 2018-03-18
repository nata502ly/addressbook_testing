import pytest
import json
import random
import string
from fixtures.addressbook_app import AddressbookApp
from fixtures.addressbook_db import AddressbookDB
from models.group import Group


@pytest.fixture(scope="session")
def config():
    with open("config.json") as f:
        result = json.load(f)
    return result


@pytest.fixture()
def app(selenium, config):
    app = AddressbookApp(selenium, base_url=config["web"]["base_url"])
    yield app
    app.close()


@pytest.fixture(scope="session")
def db(config):
    db = AddressbookDB(**config["db"])
    yield db
    db.close()


@pytest.fixture()
def init_login(app, config):
    app.login(username=config["web"]["username"], password=config["web"]["password"])
    yield
    app.logout()


def random_string(max_len):
    length = random.randrange(1, max_len)
    symbols = string.ascii_letters + string.digits + string.punctuation + ' '*10
    result = ""
    for _ in range(length):
        symbol = random.choice(symbols)
        result += symbol
    return result


with open("group_data.json", encoding="utf8") as f:
    group_list = json.load(f)

group_list += [{"name": random_string(25),
                "header": random_string(25),
                "footer": random_string(25)} for _ in range(3)]


@pytest.fixture(params=group_list, ids=[str(group) for group in group_list])
def group(request):
    return Group(**request.param)
