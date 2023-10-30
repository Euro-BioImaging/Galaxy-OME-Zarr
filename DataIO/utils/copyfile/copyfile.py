import os, shutil

def copyfile(fpath, target_dir, new_name = None):
    try:
        shutil.copy(fpath, target_dir)
    except:
        raise ValueError('Copy attempt failed.')
    try:
        if new_name is not None:
            fname = fpath.split('/')[-1]
            newpath = os.path.join(target_dir, fname)
            chgname = os.path.join(target_dir, new_name)
            os.rename(newpath, chgname)
        return True
    except:
        raise ValueError('Renaming attempt failed.')
        return False

