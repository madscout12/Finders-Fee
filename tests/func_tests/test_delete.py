import unittest
import os
import subprocess
import json

os.chdir("../..")

tests = [{"script":"python3 src/main.py delete -k first_name -f tests/test_data/delete_data.json",\
                    "deleted":['first_name'],\
                    "out_file":['out.json']}#,\
#        {"script":"python3 src/main.py delete -k address['number'] -f tests/test_data/delete_data.json",\
#                    "deleted":["address['number']"],\
#                    "out_file":['out.json']}
                 ]

class TestDelete(unittest.TestCase):


    def test_delete(self):
        for test in tests:
            self.check_match(test)
            os.remove(test["out_file"][0])

    def check_match(self, test):
        script = test["script"]
        deleted = test["deleted"]

        proc = subprocess.Popen(script, shell=True)
        proc.wait()
        self.assertEqual(0, proc.returncode, msg=proc.stderr)

        self.assertTrue(os.path.exists(test["out_file"][0]))

        for key in deleted:
            with open(test["out_file"][0]) as json_file:
                data = json.load(json_file)
                for entry in data:
                    self.assertTrue(key not in entry.keys())

if __name__ == "__main__":
    unittest.main()
