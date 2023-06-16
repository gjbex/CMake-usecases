#!/usr/bin/env pyhon

import argparse
import utils.messages


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description='say bye')
    arg_parser.add_argument('name', help='name to say bye to')
    options = arg_parser.parse_args()
    utils.messages.message('bye', options.name)
