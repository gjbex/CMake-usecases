#!/usr/bin/env python

# This script reads a CSV file into a pandas dataframe, and then
# calculates the average of each column.  Columns that don't contain
# numbers are ignored.
# Command line arguments are handled using argparse. The script
# requires one argument: the name of the CSV file to read. It also
# accepts a flag to indicate whether a warning should be printed if
# there are any non-numeric columns in the CSV file.
# The script prints the average of each column to stdout.
# An error message should be printed when the file cannot be opened and
# the script should exit with a non-zero exit code.
# The print function should be used for all output, also error messages.
# Error messages should be printed to stderr.  Make sure the script runs
# correctly with Python 3 and uses modren Python idioms like f-strings.

import argparse
import pandas as pd
import sys

def main():
    parser = argparse.ArgumentParser(description='Calculate average of each column in a CSV file.')
    parser.add_argument('filename', help='CSV file to read')
    parser.add_argument('--warn', action='store_true', help='Print warning if non-numeric columns are found')
    args = parser.parse_args()

    try:
        df = pd.read_csv(args.filename)
    except IOError as e:
        print(f'Error opening {args.filename}: {e}', file=sys.stderr)
        sys.exit(1)

    for col in df.columns:
        if df[col].dtype.kind == 'f':
            print(f'{col}: {df[col].mean()}')
        elif args.warn:
            print(f'Warning: column {col} is not numeric', file=sys.stderr)

if __name__ == '__main__':
    main()
