"""
Module containing the tests for the bot's database
"""
import json
import os
import unittest
from random import random
from typing import List

from bot.database.gifs import GifDatabase

__author__ = "Ignacio Slater Muñoz <islaterm@gmail.com>"
__version__ = "v0.1b1"
__since__ = "v0.1b1"


def test_db_create() -> None:
    """
    Checks if the database can be created correctly
    """
    missing_db_path = "MissingDB.json"
    test_db = GifDatabase(missing_db_path)
    assert test_db.gif_list == []
    os.remove(missing_db_path)


class GifDatabaseTest(unittest.TestCase):
    """
    Test set for the database
    """
    _expected_gif_list: List[str]
    _test_db_path: str

    def setUp(self) -> None:
        """
        Initializes the fields to be used in the tests
        """
        self._test_db_path = "TestDB.json"
        self._expected_gif_list = [str(random()), str(random()), str(random()),
                                   str(random())]

    def tearDown(self) -> None:
        """
        Deletes the files created in the tests
        """
        os.remove(self._test_db_path)

    def test_db_load(self) -> None:
        """
        Checks if the database can be loaded correctly from a json file.
        """
        with open(self._test_db_path, 'w+') as json_file:
            json.dump(self._expected_gif_list, json_file)
        test_db = GifDatabase(self._test_db_path)
        assert test_db.gif_list == self._expected_gif_list

    def test_add_gif(self) -> None:
        """
        Tests that gifs can be added correctly to the database
        """
        test_db = GifDatabase(self._test_db_path)  # Creates an empty database
        for index, gif in enumerate(self._expected_gif_list, start=1):
            # Adds each element of the expected list to the database and checks that the
            # results match through every insertion
            test_db.add_gif(gif)
            assert test_db.gif_list == self._expected_gif_list[:index]
            with open(self._test_db_path, 'r') as json_file:
                assert json.load(json_file) == self._expected_gif_list[:index]
        for gif in self._expected_gif_list:
            # Tries to add repeated gifs to the database and checks that they're not added
            test_db.add_gif(gif)
        assert test_db.gif_list == self._expected_gif_list


if __name__ == '__main__':
    unittest.main()
