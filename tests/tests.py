# -*- coding: utf-8 -*-
from unittest import TestCase
from jsondb.db import Database
from jsondb.compat import u


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

    def test_create_none_exists(self):
        """
        A file should be created if none exists
        and an empty {} is placed in the file.
        """
        from os import path
        import os

        database = Database("new.db")

        data = ""
        with open ("new.db", "r") as db:
            data = db.read()

        self.assertTrue(path.exists("new.db"))
        self.assertTrue("{}" in data)

        os.remove("new.db")

    def test_empty_file_initialized(self):
        """
        Test that when a file exists but is empty,
        a {} is added.
        """
        import os

        # Create an new empty file
        open("empty.db", 'a').close()

        database = Database("empty.db")

        data = ""
        with open ("empty.db", "r") as db:
            data = db.read()

        self.assertTrue("{}" in data)

        os.remove("empty.db")

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


class UnicodeTests(BaseTestCase):

    def test_data_with_unicode_key(self):

        unicode_text = u("∰ ∱ ∲ ∳ ⨋ ⨌⨔ ⨕ ⨖ ⨗ ⨘ ⨙ ⨚ ∫ ∬ ∭ ∮ ∯  ⨍ ⨎ ⨏ ⨐ ⨑ ⨒ ⨓  ⨛ ⨜")

        self.database.data(key=unicode_text, value=13)

        self.assertTrue(unicode_text in self.database.data())
        self.assertEqual(self.database.data(key=unicode_text), 13)

    def test_data_with_unicode_value(self):

        unicode_text = u("∠ ∡ ⦛ ⦞ ⦟ ⦢ ⦣ ⦤ ⦥ ⦦ ⦧ ⦨ ⦩ ⦪ ⦫ ⦬ ⦭ ⦮ ⦯ ⦓ ⦔ ⦕ ⦖ ⟀")

        self.database.data(key="unicode", value=unicode_text)

        self.assertEqual(unicode_text, self.database.data(key="unicode"))


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


class UtilityTests(TestCase):

    def test_nonexistant_database_is_invalid(self):
        from jsondb.file_writer import is_valid

        self.assertFalse(is_valid("some_nonexistant_file.db"))
