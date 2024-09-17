#!/usr/bin/env python

import requests
import os
import argparse
from rich.console import Console
from rich.progress import track

parser = argparse.ArgumentParser(prog="Ben", description="Command line tool to download files. Made to be used in Timot's software", epilog="For more detailed help look at github. :)")
parser.add_argument('-l' '--link', nargs='?', help='Download links', required=True)
parser.add_argument('-o', '--output', nargs='?', help='Download Output', required=True)


def main_function():
    NotImplemented


if __name__ == '__main__':

    main_function()