import sys
import unittest
import os
import shutil
import subprocess

script = "python3 src/main.py match -k first_name -f tests/test_data/match_data.json -o match_test"

class TestMatch(unittest.TestCase):

    def setUp(self):
        os.chdir("../..")
        try:
            os.mkdir("match_test")
        except OSError:
            pass

    def tearDown(self):
        shutil.rmtree("match_test")

    def test_match(self):
        print(os.getcwd())
        proc = subprocess.Popen(script, shell=True)
        proc.wait()
        self.assertEqual(0, proc.returncode, msg=proc.stderr)






if __name__ == "__main__":
    unittest.main()
