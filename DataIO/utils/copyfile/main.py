
import argparse
from copyfile import copyfile

if __name__ == '__main__': ### The part after main is not imported!
    parser = argparse.ArgumentParser()
    parser.add_argument('input_filepath')
    parser.add_argument('target_directory')
    parser.add_argument('--newname', default=None)
    args = parser.parse_args()
    copyfile(args.input_filepath, args.target_directory, args.newname)








