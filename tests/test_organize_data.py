import sys
import unittest
import os
import shutil

sys.path.append("../src")

from main import organize_data


class TestFileStructure(unittest.TestCase):

    def setUp(self):
        self.data = {"directory1": "data", "directory2": "data"}
        self.path = "temp"

    def test_valid_path(self):
        organize_data(self.data, self.path)
        self.assertTrue(os.path.exists(self.path))
        for key in self.data.keys():
            self.assertTrue(os.path.exists("{0}/{1}/{1}.json".format(self.path, key)))
        shutil.rmtree(self.path, ignore_errors=True)

    def test_top_dir_exists(self):
        os.mkdir(self.path)
        organize_data(self.data, self.path)
        self.assertTrue(os.path.exists(self.path))
        for key in self.data.keys():
            self.assertTrue(os.path.exists("{0}/{1}/{1}.json".format(self.path, key)))
        shutil.rmtree(self.path, ignore_errors=True)

    def test_all_dirs_exist(self):
        os.mkdir(self.path)
        for key in self.data.keys():
            os.mkdir(self.path + "/" + key)
        organize_data(self.data, self.path)
        self.assertTrue(os.path.exists(self.path))
        for key in self.data.keys():
            self.assertTrue(os.path.exists("{0}/{1}/{1}.json".format(self.path, key)))
        shutil.rmtree(self.path, ignore_errors=True)

    def test_invalid_path(self):
        path = "//"
        try:
            organize_data(self.data, path)
        except OSError as e:
            self.assertEqual("[Errno 13] Permission denied: '///directory1'", str(e))

    def test_no_data(self):
        data = {}
        organize_data(data, self.path)

    def test_integer_data(self):
        self.data = {1: "data", 1: "data"}
        organize_data(self.data, self.path)
        self.assertTrue(os.path.exists(self.path))
        for key in self.data.keys():
            self.assertTrue(os.path.exists("{0}/{1}/{1}.json".format(self.path, key)))
        shutil.rmtree(self.path, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()
