import argparse
import json
import os

from modules.json_handler import JSONHandler


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
    data = JSONHandler(args.file).get_data(args.match)
    organize_data(args.output, data)


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
        match_args.add_argument('-k', "--key", type=str, nargs='*', help="field(s) to match")
        match_args.add_argument('-f', "--file", type=str, nargs='*', help="paths to input file(s)")
        match_args.add_argument('-o', "--output", type=str, nargs='?', help="path to place output tree", default='.')
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
    try:
        args.func(args)
    except AttributeError:
        parser.parse_args('--help'.split())
