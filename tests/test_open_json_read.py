import sys
import unittest
from collections import defaultdict
import json

sys.path.append("../src")

from main import open_json_read


class TestInvalidFile(unittest.TestCase):

    def test_invalid_file(self):
        try:
            kwargs = {"path": ["test.json"], "match": [""]}
            data = open_json_read(**kwargs)
            self.assertTrue(data == defaultdict(list))
        except FileNotFoundError as e:
            pass

        try:
            kwargs = {"path": ["test_data/false_data.txt"], "match": [""]}
            data = open_json_read(**kwargs)
            self.assertTrue(data == defaultdict(list))
        except json.decoder.JSONDecodeError as e:
            pass

class TestInvalidMultipleFile(unittest.TestCase):

    def test_invalid_multiple_file(self):

        try:
            kwargs = {"path": ["test_data/test2.json", "test.json"], "match": ["gender"]}
            data = open_json_read(**kwargs)
            self.assertTrue(data == defaultdict(list))
        except FileNotFoundError as e:
            pass

class TestMultipleFiles(unittest.TestCase):
    def test_mulitple_files(self):
        kwargs = {"path": ["test_data/test.json", "test_data/test2.json"], "match": ["gender"]}
        data = open_json_read(**kwargs)
        self.assertEqual(2, len(data.keys()))
        for key in data.keys():
            self.assertEqual(4, len(data[key]))
            self.assertIsInstance(data[key], list)
            self.assertFalse(data[key] is [])
            self.assertIsInstance(data[key][0], dict)

class TestMultipleMatch(unittest.TestCase):
    def test_mulitple_files(self):
        kwargs = {"path": ["test_data/test.json", "test_data/test2.json"], "match": ["gender", 'id']}
        data = open_json_read(**kwargs)
        self.assertEqual(4, len(data.keys()))
        for key in data.keys():
            self.assertEqual(2, len(data[key]))
            self.assertIsInstance(data[key], list)
            self.assertFalse(data[key] is [])
            self.assertIsInstance(data[key][0], dict)


class TestInvalidMatch(unittest.TestCase):

    def test_invalid_match(self):
        kwargs = {"path": ["test_data/test.json"], "match": ["not_a_field"]}
        try:
            data = open_json_read(**kwargs)
        except KeyError:
            pass

class TestCorrctSort(unittest.TestCase):

    def test_correct_sort(self):
        kwargs = {"path": ["test_data/test.json"], "match": ["gender"]}
        data = open_json_read(**kwargs)
        self.assertEqual(2, len(data.keys()))
        for key in data.keys():
            self.assertEqual(2, len(data[key]))
            self.assertIsInstance(data[key], list)
            self.assertFalse(data[key] is [])
            self.assertIsInstance(data[key][0], dict)


class TestCorrctSort2(unittest.TestCase):

    def test_correct_sort2(self):
        kwargs = {"path": ["test_data/test2.json"], "match": ["gender"]}
        data = open_json_read(**kwargs)
        self.assertEqual(2, len(data.keys()))
        for key in data.keys():
            self.assertEqual(2, len(data[key]))
            self.assertIsInstance(data[key], list)
            self.assertFalse(data[key] is [])
            self.assertIsInstance(data[key][0], dict)


if __name__ == "__main__":
    unittest.main()
