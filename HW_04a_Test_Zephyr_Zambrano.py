"""
Homework 05a - Isolate External Dependencies
Zephyr Zambrano

Code from:
https://stackoverflow.com/questions/32043035/python-3-urlopen-context-manager-mocking

"""


import unittest
import urllib.request
import json

from unittest.mock import patch, MagicMock

from HW_04a_Zephyr_Zambrano import get_repo_data, get_commit_data


class Test_API_Data(unittest.TestCase):
    """ Tests that the methods in HW_04a_Zephyr_Zambrano work properly. """

    @patch("urllib.request.urlopen")
    def test_get_repo_data(self, mock_urlopen):
        cm = MagicMock()
        cm.read.return_value = ["SSW-567-HW-01"]
        mock_urlopen.return_value = cm

        response = urllib.request.urlopen("https://api.github.com/users/zephyrzambrano/repos")
        self.assertEqual(response.read(), ["SSW-567-HW-01"])
        response.close()
    
    @patch("urllib.request.urlopen")
    def test_get_commit_data(self, mock_urlopen):
        cm = MagicMock()
        cm.read.return_value = 3
        mock_urlopen.return_value = cm

        response = urllib.request.urlopen("https://api.github.com/repos/zephyrzambrano/SSW-567-HW-01/commits")
        self.assertEqual(response.read(), 3)
        response.close()


if __name__ == "__main__":
    unittest.main(exit=False)
