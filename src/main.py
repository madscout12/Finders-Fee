import argparse
import json
from collections import defaultdict
import os


def open_json_read(args):
    path = args["path"][0]
    match = args["match"][0]

    i = 0
    data = defaultdict(list)
    try:
        file = iterable_json(path)
        for record in file:
            data[record[match]].append(record)
    except FileNotFoundError as error:
        print("Error while loading {}: {}".format(path, error))
    except json.decoder.JSONDecodeError as error:
        print("Error: Not a valid JSON file {}".format(error))
    except KeyError as error:
        print("Error: {} is not a field".format(match))

    return data


def iterable_json(file_path):
    with open(file_path) as file:
        try:
            data = json.load(file)
            if isinstance(data, list):
                return data
        except json.decoder.JSONDecodeError:
            data = []
            with open(file_path) as file:
                for line in file:
                    data.append(json.loads(line))
            return data


def organize_data(data, path):
    if not isinstance(data, dict) or not isinstance(path, str):
        raise ValueError('Expected dict, str got: {}, {}'.format(type(data), type(path)))
    for key in data.keys():
        dir_path = path + "/" + str(key)
        make_directory(dir_path)
        write_json(dir_path + "/{}.json".format(key), data[key])


def write_json(path, json_data):
    file = open(path, 'w')
    file.write(json.dumps(json_data))
    file.close()


def make_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('path', nargs=1, type=str, help='path to filename')
    parser.add_argument('match', nargs=1, type=str, help='json fields to match')
    parser.add_argument('--out', nargs=1, type=str, default="ff_out",
                        help="path for head directory for output. defaults to home directory")
    args = vars(parser.parse_args())
    data = open_json_read(args)
    organize_data(data, args["out"][0])
