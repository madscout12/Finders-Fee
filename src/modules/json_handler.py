import json
from collections import defaultdict


class JSONHandler:

    def __init__(self, paths):
        self.data = defaultdict(list)
        self.paths = paths

    def get_data(self, matches):
        self._process_data(matches)
        return self.data

    def set_paths(self, paths):
        self.paths = paths

    def _process_data(self, matches):
        for file_path in self.paths:
            self._open_correct_type(file_path, matches)

    def _open_correct_type(self, file_path, matches):
        try:
            self._open_line_valid_json(file_path, matches)
        except ValueError:
            self._open_valid_json(file_path, matches)

    def _open_valid_json(self, file_path, matches):
        with open(file_path) as file:
            for json_data in json.load(file):
                keys = []
                for key in matches:
                    keys.append(str(json_data[key]))
                self.data[':'.join(keys)].append(json_data)

    def _open_line_valid_json(self, file_path, matches):
        with open(file_path) as file:
            for line in file.readlines():
                json_data = json.loads(line)
                keys = []
                for key in matches:
                    keys.append(str(json_data[key]))
                self.data[':'.join(keys)].append(json_data)
