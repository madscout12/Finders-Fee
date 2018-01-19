import sys
import unittest
import os
import shutil
import subprocess

os.chdir("../..")
sys.path.insert(0, "src")

from modules.json_handler import JSONHandler


tests = [{"script":"python3 src/main.py delete -k first_name -f tests/test_data/match_data.json",\
                    "deleteed":['first_name']},\
                 ]

class TestDelete(unittest.TestCase):


    def test_delete(self):
        for test in tests:
            self.check_match(test)

    def check_match(self, test):
        pass


if __name__ == "__main__":
    unittest.main()
