#!/usr/bin/env python
import pexpect
from getpass import getpass




def main():
 ip_addr = '184.105.247.70'
 username = 'pyclass'
 port = 22
 password = '88newclass'

 ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))
 ssh_conn.timeout = 3

 
 ssh_conn.expect('ssword:')
 ssh_conn.sendline(password)
 ssh_conn.expect('#')
 print ssh_conn.before, ssh_conn.after
 ssh_conn.sendline('show ip int brief')
 ssh_conn.expect('#')
 print ssh_conn.before, ssh_conn.after
if __name__ == "__main__":
  main()
 

