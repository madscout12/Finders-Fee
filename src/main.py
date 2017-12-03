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
        with open(path) as file:
            file = json.load(file)
            for record in file:
                test = record[match]
                data[record[match]].append(record)
    except FileNotFoundError as error:
        print("Error while loading {}: {}".format(path, error))
    except json.decoder.JSONDecodeError as error:
        print("Error: Not a valid JSON file {}".format(error))
    except KeyError as error:
        print("Error: {} is not a field".format(match))

    return data


def sort_data(data):
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('path', nargs=1, type=str, help='path to filename')
    parser.add_argument('match', nargs=1, type=str, help='json fields to match')
    args = vars(parser.parse_args())
    data = open_json_read(args)
