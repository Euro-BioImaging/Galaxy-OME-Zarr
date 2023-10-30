import os, argparse
import shutil

# def list_paths(directory):
#     """ List all filepaths in a directory tree. If the directory input is a single file, simply return it within a list. """
#     if os.path.isfile(directory):
#         filepaths = [directory]
#     elif os.path.isdir(directory):
#         walked = list(os.walk(directory))
#         filepaths = []
#         for walk in walked:
#             basepath = walk[0]
#             filenames = walk[-1]
#             fpaths = [os.path.join(basepath, item) for item in filenames]
#             filepaths += fpaths
#     return filepaths

# def _write(f, fpath):
#     """ Save a file f to a path and create the path if it does not exist. """
#     truncated_path = os.path.join(*os.path.split(fpath)[:-1])
#     if not os.path.exists(truncated_path):
#         os.makedirs(truncated_path)
#     print(f)
#     print(truncated_path)
#     shutil.copy(f, truncated_path)

# def _write(f, fpath):
#     """ Save a file f to a path and create the path if it does not exist. """
#     truncated_path = os.path.join(*os.path.split(fpath)[:-1])
#     with open(truncated_path, 'w') as textfile:
#         textfile.write('random file.')
#     # if not os.path.exists(truncated_path):
#     #     os.makedirs(truncated_path)
#     # print(f)
#     # print(truncated_path)
#     # shutil.copy(f, truncated_path)


def _complete_transfer2html(fpath):
    """ Save a file f to a path and create the path if it does not exist. """
    # truncated_path = os.path.join(*os.path.split(fpath)[:-1])
    with open(fpath, 'w') as textfile:
        textfile.write('random file.')
    # if not os.path.exists(truncated_path):
    #     os.makedirs(truncated_path)
    # print(f)
    # print(truncated_path)
    # shutil.copy(f, truncated_path)

# def transfer_tree(directory, newdir = 'newdir', path_contains = None, path_excludes = None):
#     """ Transfer a whole tree to a directory called newdir.
#         If directory is just a single file, transfer it to newdir.
#         Select files based on filters applied to the filenames. """
#     # directory = '/home/oezdemir/PycharmProjects/clients/newdownload/fourth_download/190417_WT_tapA_sipW_tasA_SP8_48h/WT_tapA_sipW_tasA_SP8_48h.lif'
#     spaths = list_paths(directory)
#     if path_contains is not None:
#         spaths = list(filter(lambda f: path_contains in f, spaths))
#     if path_excludes is not None:
#         spaths = list(filter(lambda f: path_contains not in f, spaths))


    ### here is Galaxy code
    # coredir = newdir#.replace('.dat', '_files')
    ###

    # for f in spaths[:1]: #TODO UNDERSTAND HOW THIS WORKS. COPYING A SINGLE FILE BASICALLY COPIES EVERYTHING.
    #     extensions = f[len(directory):]
    #     if coredir.startswith('/'):
    #         coredir = coredir[1:]
    #     dpath = '/' + coredir + extensions
    #     _write(f, dpath)

parser = argparse.ArgumentParser()
# parser.add_argument('--source', '-s')
parser.add_argument('--destination', '-d')

args = parser.parse_args()

if __name__ == '__main__':
    _complete_transfer2html(args.destination)

