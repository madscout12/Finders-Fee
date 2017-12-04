import argparse
import json
from collections import defaultdict


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


def sort_data(data):
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('path', nargs=1, type=str, help='path to filename')
    parser.add_argument('match', nargs=1, type=str, help='json fields to match')
    args = vars(parser.parse_args())
    data = open_json_read(args)
