from fixtures.addressbook_app import AddressbookApp
import unittest


class TestCreateGroup(unittest.TestCase):
    def setUp(self):
        self.app = AddressbookApp()
        self.app.login(username="admin", password="secret")

    def test_create_group(self):
        self.app.open_group_page()
        self.app.create_group("new name", "new header", "new footer")
        self.app.return_to_group_page()

    def test_delete_first_group(self):
        self.app.open_group_page()
        self.app.delete_group(number=0)
        self.app.return_to_group_page()

    def tearDown(self):
        self.app.logout()
        self.app.close()


if __name__ == "__main__":
    unittest.main()
