import argparse
from write_ssh import write

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath')

    args = parser.parse_args()

    write(args.filepath)


