import argparse

"""
        parser.add_argument('path', nargs='+', type=str, help='path to filename')
        parser.add_argument('match', nargs='+', type=str, help='json fields to match')
        parser.add_argument('-o', '--out', nargs=1, type=str, default="ff_out",
                            help="path for head directory for output. defaults to home directory")
"""


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

    def add_explode(self):
        explode_args = self.subparsers.add_parser('explode', help='explode help')

    def add_collapse(self):
        collapse_args = self.subparsers.add_parser('collapse', help='collapse help')

    def add_delete(self):
        delete_args = self.subparsers.add_parser('delete', help='delete help')

    def add_perc_match(self):
        perc_match = self.subparsers.add_parser('perc_match', help='percentage match help')
