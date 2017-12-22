import sys
import unittest
from collections import defaultdict

sys.path.append("../src")

from modules.json_handler import JSONHandler


class TestInvalidFile(unittest.TestCase):

    def test_invalid_file(self):
        path = ['test.json']
        match = [""]
        handler = JSONHandler(path)

        try:
            data = handler.get_data(match)
            self.assertTrue(data == defaultdict(list))
        except IOError as e:
            self.assertEqual("[Errno 2] No such file or directory: 'test.json'", str(e))

        try:
            handler.set_paths(["test_data/false_data.txt"])
            data = handler.get_data(match)
            self.assertTrue(data == defaultdict(list))
        except ValueError as e:
            self.assertEqual("No JSON object could be decoded", str(e))


class TestInvalidMultipleFile(unittest.TestCase):

    def test_invalid_multiple_file(self):

        try:
            paths = ["test_data/test2.json", "test.json"]
            match = ["gender"]
            handler = JSONHandler(paths)

            data = handler.get_data(match)
            self.assertTrue(data == defaultdict(list))
        except IOError as e:
            self.assertEqual("[Errno 2] No such file or directory: 'test.json'", str(e))


class TestMultipleFiles(unittest.TestCase):
    def test_mulitple_files(self):
        paths = ["test_data/test.json", "test_data/test2.json"]
        match = ["gender"]

        handler = JSONHandler(paths)
        data = handler.get_data(match)

        self.assertEqual(2, len(data.keys()))
        for key in data.keys():
            self.assertEqual(4, len(data[key]))
            self.assertIsInstance(data[key], list)
            self.assertFalse(data[key] is [])
            self.assertIsInstance(data[key][0], dict)


class TestMultipleMatch(unittest.TestCase):
    def test_mulitple_files(self):
        paths = ["test_data/test.json", "test_data/test2.json"]
        match = ["gender", "id"]

        handler = JSONHandler(paths)
        data = handler.get_data(match)

        self.assertEqual(4, len(data.keys()))
        for key in data.keys():
            self.assertEqual(2, len(data[key]))
            self.assertIsInstance(data[key], list)
            self.assertFalse(data[key] is [])
            self.assertIsInstance(data[key][0], dict)


class TestInvalidMatch(unittest.TestCase):

    def test_invalid_match(self):
        paths = ["test_data/test.json", "test_data/test2.json"]
        match = ["not_a_field"]

        handler = JSONHandler(paths)
        try:
            data = handler.get_data(match)
        except KeyError:
            pass


class TestCorrctSort(unittest.TestCase):

    def test_correct_sort(self):
        paths = ["test_data/test.json"]
        match = ["gender"]

        handler = JSONHandler(paths)

        data = handler.get_data(match)
        self.assertEqual(2, len(data.keys()))
        for key in data.keys():
            self.assertEqual(2, len(data[key]))
            self.assertIsInstance(data[key], list)
            self.assertFalse(data[key] is [])
            self.assertIsInstance(data[key][0], dict)


class TestCorrctSort2(unittest.TestCase):

    def test_correct_sort2(self):
        paths = ["test_data/test2.json"]
        match = ["gender"]

        handler = JSONHandler(paths)
        data = handler.get_data(match)

        self.assertEqual(2, len(data.keys()))
        for key in data.keys():
            self.assertEqual(2, len(data[key]))
            self.assertIsInstance(data[key], list)
            self.assertFalse(data[key] is [])
            self.assertIsInstance(data[key][0], dict)


if __name__ == "__main__":
    unittest.main()
