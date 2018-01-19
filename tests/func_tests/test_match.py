import sys
import unittest
import os
import shutil
import subprocess

os.chdir("../..")
sys.path.insert(0, "src")

from modules.json_handler import JSONHandler

tests = [{"script":"python3 src/main.py match -k first_name -f tests/test_data/match_data.json -o match_test",\
                    "expected_matches":["Jeanette", "Giavani", "Noell", "Willard"],\
                    "match_name":['first_name']},\
        {"script":"python3 src/main.py match -k first_name -f tests/test_data/match_data.json tests/test_data/test2.json -o match_test",\
                    "expected_matches":["Jeanette", "Giavani", "Noell", "Willard"],\
                    "match_name":['first_name']},\
        {"script":"python3 src/main.py match -k first_name last_name -f tests/test_data/match_data.json -o match_test",\
                    "expected_matches":["Jeanette:Penddreth", "Giavani:Frediani", "Noell:Bea", "Willard:Valek"],\
                    "match_name":['first_name','last_name']},\
        {"script":"python3 src/main.py match -k first_name id -f tests/test_data/match_data.json -o match_test",\
                    "expected_matches":["Jeanette:1", "Jeanette:5", "Giavani:2", "Noell:3", "Willard:4"],\
                    "match_name":['first_name','last_name']}\
                 ]


test_dir = "match_test"



class TestMatch(unittest.TestCase):

    def set_up(self):

        try:
            os.mkdir(test_dir)
        except OSError:
            pass

    def tear_down(self):
        shutil.rmtree(test_dir)

    def test_match(self):
        for test in tests:
            self.set_up()
            self.check_match(test)
            self.tear_down()

    def check_match(self, test):
        script = test["script"]
        matches = test["expected_matches"]
        match_name = test["match_name"]

        proc = subprocess.Popen(script, shell=True)
        proc.wait()
        self.assertEqual(0, proc.returncode, msg=proc.stderr)

        for match in matches:
            self.assertTrue(os.path.exists("{dir}/{name}".format(dir=test_dir, name=match)))

            file = "{dir}/{name}/{name}.json".format(dir=test_dir, name=match)
            self.assertTrue(os.path.exists(file))

            data = JSONHandler([file]).get_data(match_name)

            for entry in data[match]:
                for name in match_name:
                    self.assertTrue(entry[name] in match)

if __name__ == "__main__":
    unittest.main()
