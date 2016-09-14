# -*- coding: utf-8 -*-
from .file_writer import read_data, write_data, is_valid
from .compat import iteritems


class Database(object):

    def __init__(self, file_path):
        """
        This class manages a json-formatted file database.
        Constructor takes the file path of the database as a parameter.
        """
        self.path = None
        self.set_path(file_path)

    def set_path(self, file_path):
        """
        Set the path of the database.
        Create the file if it does not exist.
        """
        if not is_valid(file_path):
            write_data(file_path, {})

        self.path = file_path

    def _get_content(self, key=None):
        obj = read_data(self.path)

        if key or key == "":
            if key in obj.keys():
                return obj[key]
            else:
                return None

        return obj

    def _set_content(self, key, value):
        obj = self._get_content()
        obj[key] = value

        data = write_data(self.path, obj)

    def delete(self, key):
        """
        Removes the specified key from the database.
        """
        obj = self._get_content()
        obj.pop(key, None)

        data = write_data(self.path, obj)

    def data(self, **kwargs):
        """
        If a key is passed in, a corresponding value will be returned.
        If a key-value pair is passed in then the corresponding key in
        the database will be set to the specified value.
        A dictionary can be passed in as well.
        If a key does not exist and a value is provided then an entry
        will be created in the database.
        """

        key = kwargs.pop('key', None)
        value = kwargs.pop('value', None)
        dictionary = kwargs.pop('dictionary', None)

        # Fail if a key and a dictionary or a value and a dictionary are given
        if (key is not None and dictionary is not None) or \
           (value is not None and dictionary is not None):
            raise ValueError

        # If only a key was provided return the corresponding value
        if key is not None and value is None:
            return self._get_content(key)

        # if a key and a value are passed in
        if key is not None and value is not None:
            self._set_content(key, value)

        if dictionary is not None:
            for key in dictionary.keys():
                value = dictionary[key]
                self._set_content(key, value)

        return self._get_content()

    def _contains_value(self, obj, keys, find_value):
        key = keys.pop(0)

        # If there are no keys left
        if not len(keys):
            if obj[key] == find_value:
                return True
            else:
                return False

        if isinstance(obj, dict):
            if key in obj:
                return self._contains_value(obj[key], keys, find_value)

    def filter(self, filter_arguments):
        """
        Takes a dictionary of filter parameters.
        Return a list of objects based on a list of parameters.
        """
        results = self._get_content()

        # Filter based on a dictionary of search parameters
        if type(filter_arguments) is dict:
            for item, content in iteritems(self._get_content()):
                for key, value in iteritems(filter_arguments):
                    keys = key.split('.')
                    value = filter_arguments[key]

                    if not self._contains_value({item: content}, keys, value):
                        del(results[item])

        # Filter based on an input string that should match database key
        if type(filter_arguments) is str:
            if filter_arguments in results:
                return [{filter_arguments: results[filter_arguments]}]
            else:
                return []

        return results

    # Iterator methods

    def __len__(self):
        return len(self._get_content())

    def __iter__(self):
        return iter(self._get_content().keys())

    def __list__(self):
        return list(self._get_content().keys())

    # Dictionary compatibility methods

    def __getitem__(self, key):
        return self.data(key=key)

    def __setitem__(self, key, value):
        return self.data(key=key, value=value)

    def __delitem__(self, key):
        return self.delete(key=key)

    def __contains__(self, key):
        return key in self._get_content()
