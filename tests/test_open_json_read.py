import sys
import unittest
from collections import defaultdict

sys.path.append("../src")

from main import open_json_read


class TestInvalidFile(unittest.TestCase):

    def test_invalid_file(self):
        args = {"path": ["test.json"], "match": [""]}
        data = open_json_read(args)
        self.assertTrue(data == defaultdict(list))

        args = {"path": ["test_data/false_data.txt"], "match": [""]}
        data = open_json_read(args)
        self.assertTrue(data == defaultdict(list))


class TestInvalidMatch(unittest.TestCase):

    def test_invalid_match(self):
        args = {"path": ["test_data/test.json"], "match": ["not_a_field"]}
        data = open_json_read(args)
        self.assertTrue(data == defaultdict(list))


class TestCorrctSort(unittest.TestCase):

    def test_correct_sort(self):
        args = {"path": ["test_data/test.json"], "match": ["gender"]}
        data = open_json_read(args)
        self.assertEqual(2, len(data.keys()))
        for key in data.keys():
            self.assertIsInstance(data[key], list)
            self.assertFalse(data[key] is [])
            self.assertIsInstance(data[key][0], dict)


class TestCorrctSort2(unittest.TestCase):

    def test_correct_sort2(self):
        args = {"path": ["test_data/test2.json"], "match": ["gender"]}
        data = open_json_read(args)
        self.assertEqual(2, len(data.keys()))
        for key in data.keys():
            self.assertIsInstance(data[key], list)
            self.assertFalse(data[key] is [])
            self.assertIsInstance(data[key][0], dict)


if __name__ == "__main__":
    unittest.main()
