#!/usr/bin/env python

import pexpect
import getpass

username = 'root'
hostname = 'szwg-tdw-ftp06.szwg01'
remote_path = '~'
localfile = 'test.dat'
passwd = '123456'

def scp_file(username,hostname,remote_path,localfile,passwd):
    '''a scp function without exception
    '''
    cmd = 'scp %s %s@%s:%s' %(localfile,username,hostname,remote_path)
    scp_child=pexpect.spawn(cmd)

    if scp_child.expect('password:'):
        scp_child.sendline(passwd)
        print scp_child.read()

if __name__ == '__main__':
    scp_file(username,hostname,remote_path,localfile,passwd)
