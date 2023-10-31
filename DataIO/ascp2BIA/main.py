from transfer import Uploader
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('local_path')
    parser.add_argument('remote_path', default='')
    parser.add_argument('--port', default='bsaspera_w@hx-fasp-1.ebi.ac.uk')
    parser.add_argument('--sshkey', default='asperaweb_id_dsa.openssh')
    parser.add_argument('--remote_location', default='')

    args = parser.parse_args()
    
    print(args)

    client = Uploader(port = args.port, sshkey = args.sshkey, remote_location = args.remote_location)

    client.upload(args.local_path, args.remote_path)
