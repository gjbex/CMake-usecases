#!/usr/bin/env pyhon

import argparse
import utils.messages


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description='say hello')
    arg_parser.add_argument('name', help='name to say hello to')
    options = arg_parser.parse_args()
    utils.messages.message('hello', options.name)
