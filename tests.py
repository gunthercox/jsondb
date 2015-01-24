from unittest import TestCase
from jsondb.db import Database


class BaseTestCase(TestCase):

    def setUp(self):
        import json

        content = {
            "url": "http://sky.net",
            "ip": "http://10.0.1.337",
        }

        with open("test.db", "w+") as test:
            json.dump(content, test)

        self.database = Database("test.db")

    def tearDown(self):
        import os

        os.remove("test.db")


class Tests(BaseTestCase):

    def test_get_key(self):
        key = self.database.data(key="url")

        self.assertEqual(key, "http://sky.net")

    def test_get_key_not_in_database(self):
        key = self.database.data(key="bogus")

        self.assertEqual(key, None)

    def test_assign_key_value_pair(self):
        self.database.data(key="cool", value="robot")

        self.assertEqual(self.database.data(key="cool"), "robot")

    def test_assign_dictionary(self):
        d = {
            "id": "123456",
            "arduino_ip": "xxxxxx"
        }
        self.database.data(dictionary=d)

        self.assertTrue("id" in self.database.data())
        self.assertEqual(self.database.data(key="arduino_ip"), "xxxxxx")

    def test_delete_key(self):
        self.database.data(key="id", value="13")
        self.database.delete("id")

        self.assertFalse("id" in self.database.data())


class DictCompatibleTests(BaseTestCase):

    def test_get_data(self):
        data = self.database["url"]

        self.assertEqual(data, "http://sky.net")

    def test_get_unset_data(self):
        data = self.database["invalid"]

        self.assertEqual(data, None)

    def test_set_data(self):
        self.database["new"] = "test"

        self.assertEqual(self.database["new"], "test")

    def test_key_exists(self):
        self.assertTrue("url" in self.database)
        self.assertFalse("invalid" in self.database)

    def test_delete_data(self):
        del self.database["url"]

        self.assertEqual(self.database["url"], None)
