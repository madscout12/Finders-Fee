import argparse
import json
from collections import defaultdict
import os


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

def handle_match(args):
    print("match")

def handle_explode(args):
    print("explode")

def handle_collapse(args):
    print('collapse')

def handle_delete(args):
    print('delete')

def handle_perc_match(args):
    print('perc_match')

class Arguments:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.subparsers = self.parser.add_subparsers(help='sub-command help')
        self.make_parser()

    def get_parser(self):
        return self.parser

    def make_parser(self):
        self.add_match()
        self.add_explode()
        self.add_collapse()
        self.add_delete()
        self.add_perc_match()

    def add_match(self):
        match_args = self.subparsers.add_parser('match', help='match help')
        match_args.set_defaults(func=handle_match)

    def add_explode(self):
        explode_args = self.subparsers.add_parser('explode', help='explode help')
        explode_args.set_defaults(func=handle_explode)

    def add_collapse(self):
        collapse_args = self.subparsers.add_parser('collapse', help='collapse help')
        collapse_args.set_defaults(func=handle_collapse)

    def add_delete(self):
        delete_args = self.subparsers.add_parser('delete', help='delete help')
        delete_args.set_defaults(func=handle_delete)

    def add_perc_match(self):
        perc_match = self.subparsers.add_parser('perc_match', help='percentage match help')
        perc_match.set_defaults(func=handle_perc_match)

if __name__ == "__main__":
    parser = Arguments().get_parser()
    args = parser.parse_args()
    args.func(args)

    '''    parser = argparse.ArgumentParser()
    parser.add_argument('path', nargs='+', type=str, help='path to filename')
    parser.add_argument('match', nargs='+', type=str, help='json fields to match')
    parser.add_argument('-o', '--out', nargs=1, type=str, default="ff_out",
                        help="path for head directory for output. defaults to home directory")
    kwargs = vars(parser.parse_args())
    data = open_json_read(**kwargs)
    organize_data(data, **kwargs)
'''