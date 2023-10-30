import argparse
from warn import warn

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--text', '-t', required = False, default = 'This is a text!')

    args = parser.parse_args()

    warn(args.text)

