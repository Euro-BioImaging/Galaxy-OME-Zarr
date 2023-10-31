""" Toolset to upload a local file or directory tree to Bioimage Archive server. """

import os
import subprocess

class ASCP:
    def __init__(self,
                 port = 'bsaspera_w@hx-fasp-1.ebi.ac.uk',
                 sshkey = 'asperaweb_id_dsa.openssh',
                 remote_location = ''
                 ):
        if '__at__' in port:
            port = port.replace('__at__', '@')
        self.__head = "ascp -P33001 -i %s" % sshkey
        self.__tail = '%s:%s' %(port, remote_location)
    def upload_tree(self, local_dir, remote_dir = '.'):
        self.cmd = self.__head + ' -d ' + local_dir + ' ' + os.path.join(self.__tail, remote_dir)
        print("here is cmd:          ")
        print(self.cmd)
        try:
            subprocess.run(self.cmd, shell=True)
                  #         stdout=subprocess.DEVNULL,
                  #         stderr=subprocess.STDOUT
                  #          )
            print('The command line was successfully executed: %s' % self.cmd)
        except:
            print('The command line failed to be executed: %s' % self.cmd)


class Uploader:
    def __init__(self,
                 port = 'bsaspera_w@hx-fasp-1.ebi.ac.uk',
                 sshkey = 'asperaweb_id_dsa.openssh',
                 remote_location = ''
                 ):
        self.ascp = ASCP(port, sshkey, remote_location)
    def upload(self, local_path, remote_path):
        if remote_path == '':
            remote_path = '.'
        elif remote_path is None:
            remote_path = '.'
        if os.path.exists(local_path):
            folders = os.listdir(local_path)
            for item in folders:
                if item == 'sshdir':
                    pass
                else:
                    fpath = os.path.join(local_path, item)
                    try:
                        self.ascp.upload_tree(fpath, remote_path)
                    except:
                        raise Warning('The transfer did not work.')
        else:
            raise ValueError('The following local path does not exist: %s' % local_path)


# ascp = ASCP()
#
# ascp.upload_tree('/local/path/to/data', '/remote/path')

