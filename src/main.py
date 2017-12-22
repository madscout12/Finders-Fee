import argparse
import json
from collections import defaultdict
import os

from modules.arguments import Arguments

def open_json_read(path, match):
    data = defaultdict(list)
    for file in path:
        data = open_correct_type(file, match, data)
    return data


def open_correct_type(path, match, data):
    try:
        return open_line_valid_json(path, match, data)
    except json.decoder.JSONDecodeError:
        return open_valid_json(path, match, data)


def open_valid_json(file_path, match, data):
    with open(file_path) as file:
        for json_data in json.load(file):
            keys = []
            for key in match:
                keys.append(str(json_data[key]))
            data[':'.join(keys)].append(json_data)
    return data


def open_line_valid_json(file_path, match, data):
    with open(file_path) as file:
        for line in file.readlines():
            json_data = json.loads(line)
            keys = []
            for key in match:
                keys.append(str(json_data[key]))
            data[':'.join(keys)].append(json_data)
    return data


def organize_data(json_data, path):
    for key in json_data.keys():
        dir_path = path + "/" + str(key)
        make_directory(dir_path)
        write_json(dir_path + "/{}.json".format(key), json_data[key])


def write_json(path, json_data):
    file = open(path, 'w')
    file.write(json.dumps(json_data))
    file.close()


def make_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)


if __name__ == "__main__":
    parser = Arguments().get_parser()
    parser.parse_args()

    '''    parser = argparse.ArgumentParser()
    parser.add_argument('path', nargs='+', type=str, help='path to filename')
    parser.add_argument('match', nargs='+', type=str, help='json fields to match')
    parser.add_argument('-o', '--out', nargs=1, type=str, default="ff_out",
                        help="path for head directory for output. defaults to home directory")
    kwargs = vars(parser.parse_args())
    data = open_json_read(**kwargs)
    organize_data(data, **kwargs)
'''