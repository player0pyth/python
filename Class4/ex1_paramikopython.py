
#!/usr/bin/env python
'''
Use Paramiko to retrieve the entire 'show version' output.
'''

import paramiko
import time
from getpass import getpass

MAX_BUFFER=65535


def clear_buffer(remote_conn):
    '''
    Clear any data in the receive buffer
    '''
    if remote_conn.recv_ready():
        return remote_conn.recv(MAX_BUFFER)

def sendcommanda(remote_conn, cmd='', delay=1):

 if cmd !='':
   cmd =cmd.strip()
 
 remote_conn.send(cmd + '\n')
 time.sleep(delay)

 if remote_conn.recv_ready():
  return remote_conn.recv(MAX_BUFFER)
 else:
  return ''
def turnoffloggining(remote_conn):
   remote_conn.send('terminal length 0' + '\n')
   clear_buffer(remote_conn)

def main():

 ip_addr = '184.105.247.71'
 username = 'pyclass' 
 password = '88newclass'
 port = 22

 remote_conn_pre=paramiko.SSHClient()
 remote_conn_pre.load_system_host_keys()
 remote_conn_pre.connect(ip_addr, port=port, username=username, password=password,
                            look_for_keys=False, allow_agent=False)
 remote_conn = remote_conn_pre.invoke_shell()

 time.sleep(1)
 clear_buffer(remote_conn)
 turnoffloggining(remote_conn)
 output=sendcommanda(remote_conn, cmd='show run')
 print output


if __name__ == "__main__":
    main()


