import argparse
import json
from collections import defaultdict


def open_json_read(args):
    path =  args["path"][0]
    match = args["match"][0]

    i = 0
    data = defaultdict(list)
    with open(path) as file:
        for line in file:
            record = json.loads(line)
            data[record[match]].append(record)

    return data

def sort_data(data):
c


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('path', nargs=1, type=str, help='path to filename')
    parser.add_argument('match', nargs=1, type=str, help='json fields to match')
    args = vars(parser.parse_args())
    data = open_json_read(args)
