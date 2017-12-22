import argparse
import json
import os


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
    try:
        args.func(args)
    except AttributeError:
        parser.parse_args('--help'.split())

