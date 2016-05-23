from ansible.errors import AnsibleError

import sys
import os
import logging
import tempfile
import subprocess
import argparse

class App (object):
    
    def __init__(self):
        pass

    def build_argument_parser(self):
        p = argparse.ArgumentParser()
        p.add_argument('--var', '-v',
                       default='ANSIBLE_VAULT_PASSWORD',
                       help='Environment variable that contains password to Ansible Vault')

        return p
        
    def parse_args(self):
        p = self.build_argument_parser()
        return p.parse_args()

    def main(self):
        args = self.parse_args()
        
        if args.var not in os.environ.keys():
            raise AnsibleError('Environment variable "%s" is not set!' % args.var)
            
        print os.environ[args.var]

def main():
    App().main()
      
if __name__ == '__main__':
    main()