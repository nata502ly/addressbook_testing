import pytest
import json
import random
import string
import os.path
from fixtures.addressbook_app import AddressbookApp
from fixtures.addressbook_db import AddressbookDB
from models.group import Group


@pytest.fixture(scope="session")
def config():
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")
    with open(filename) as f:
        result = json.load(f)
    return result


@pytest.fixture()
def app(selenium, config, request):
    base_url = request.config.getoption("--base-url")
    app = AddressbookApp(selenium, base_url=base_url)
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

filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "group_data.json")
with open(filename, encoding="utf8") as f:
    group_list = json.load(f)

group_list += [{"name": random_string(25),
                "header": random_string(25),
                "footer": random_string(25)} for _ in range(3)]


@pytest.fixture(params=group_list, ids=[str(group) for group in group_list])
def group(request):
    return Group(**request.param)
