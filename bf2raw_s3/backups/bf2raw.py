import os, subprocess
### Here, you can also use tifffile to obtain some metadata information directly from the tiff tag and find some defaults for the Galaxy parameters

class CMD:
    def __init__(self,
                 exe
                 ):
        self.cmd = exe + ' '
    def add_param(self,
                  param = None,
                  value = '',
                  is_flag = False
                  ):
        text = ''
        if is_flag:
            assert param is None
            text = '--%s' % value
        elif not is_flag:
            if param is None or (not param.startswith('-')) :
                text = '%s' % value
            else:
                text = '%s %s' % (param, value)
        self.cmd += ' %s' % text
        print('The command line is: %s' % self.cmd)
    def run(self):
        try:
            subprocess.run(self.cmd, shell=True
                           # ,stdout=subprocess.DEVNULL,
                           # stderr=subprocess.STDOUT
                           )
            print('The command line was successfully executed: %s' % self.cmd)
        except:
            print('The command line failed to be executed: %s' % self.cmd)
            
    def save(self, fpath):
        with open(fpath, 'w') as textwriter:
            textwriter.write(self.cmd)            
            
            

