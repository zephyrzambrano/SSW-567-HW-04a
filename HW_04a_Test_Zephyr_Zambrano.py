"""
Homework 04a - Develop with the Perspective of the Tester in mind
Zephyr Zambrano

"""


import unittest
import urllib.request
import json


from HW_04a_Zephyr_Zambrano import get_repo_data, get_commit_data


class Test_API_Data(unittest.TestCase):
    """ Tests that the methods in HW_04a_Zephyr_Zambrano work properly. """

    def test_get_repo_data(self):
        """ Tests get_repo_data """
        user = "zephyrzambrano"
        repo_list = ['567-HelloWorld', 'Advanced-Web-Design-Final-Project',
        'Advanced-Web-Design-Lab-1b', 'Advanced-Web-Design-Lab-3b', 'Advanced-Web-Design-Lab-4b',
        'Advanced-Web-Design-Lab-5', 'Advanced-Web-Design-Lab-6', 'Advanced-Web-Design-Lab-7',
        'Advanced-Web-Design-Lab-8', 'ApplePicker', 'FA18-MissionDemolition', 'GameDesign-FinalProject',
        'GameDesign-Terrain', 'OOP-GroupProject', 'Prospector', 'Roll-a-Ball', 'RU-Safe', 'Space-SHMUP',
        'SSW-567-HW-01', 'SSW-567-HW-02', 'SSW-567-HW-04a', 'SSW-810-Project', 'Web-Design-Project']

        self.assertEqual(repo_list, get_repo_data(user))

    def test_get_commit_data(self):
        """ Tests get_commit_data """
        user = "zephyrzambrano"
        
        repo1 = "SSW-567-HW-01"
        commits1 = 3

        repo2 = "SSW-567-HW-02"
        commits2 = 6

        self.assertEqual(commits1, get_commit_data(user, repo1))
        self.assertEqual(commits2, get_commit_data(user, repo2))


if __name__ == "__main__":
    unittest.main(exit=False)
