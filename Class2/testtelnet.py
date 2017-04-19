#!/usr/bin/env python

import telnetlib
import time

TELNET_PORT = 23
TELNET_TIMEOUT = 6



def sendcommand(remote_conn,command):
 cmd = command.rstrip()
 remote_conn.write(cmd + '\n')
 time.sleep(1)
 return remote_conn.read_very_eager()


def connection_telnet(ip_addr):
  remote_conn=telnetlib.Telnet(ip_addr,TELNET_PORT,TELNET_TIMEOUT)
  return remote_conn


def login(remote_conn,username,password):
 output = remote_conn.read_until("sername", TELNET_TIMEOUT)
 remote_conn.write(username + '\n')
 output += remote_conn.read_until("word", TELNET_TIMEOUT)
 remote_conn.write(password + '\n')
 return output


def main():

 username = 'pyclass'
 password = '88newclass' 

 remote_conn=connection_telnet("184.105.247.70")
 output = login(remote_conn,username,password) 
 print output
 output=sendcommand(remote_conn,"show ip int brief")  
 print output
 output=sendcommand(remote_conn,"terminal length 0")
 output=sendcommand(remote_conn,"show hardware")
 print output
 remote_conn.close()

if __name__ == "__main__":
   main()



