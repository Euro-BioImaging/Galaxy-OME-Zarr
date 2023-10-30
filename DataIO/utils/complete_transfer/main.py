import argparse

from complete_transfer2html import _complete_transfer2html


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--destination', '-d')

    args = parser.parse_args()

    _complete_transfer2html(args.destination)

