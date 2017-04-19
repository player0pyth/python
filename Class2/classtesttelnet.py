#!/usr/bin/env python

import telnetlib
import time


class NetworkDevice(object):
 def __init__(self, ip, username, password): 
  self.ip = ip
  self.username = username
  self.password = password
  self.TELNET_PORT = 23
  self.TELNET_TIMEOUT = 6

 def connect_to_device(self):
  self.remote_conn=telnetlib.Telnet(self.ip,self.TELNET_PORT,self.TELNET_TIMEOUT)

 def login(self): 
  output = self.remote_conn.read_until("sername", self.TELNET_TIMEOUT)
  self.remote_conn.write(self.username + '\n')
  output += self.remote_conn.read_until("word", self.TELNET_TIMEOUT)
  self.remote_conn.write(self.password + '\n')
  print output
 
 def sendcommand(self,command):
  cmd = command.rstrip()
  self.remote_conn.write(cmd + '\n')
  time.sleep(1)
  print self.remote_conn.read_very_eager()

 def closeconn(self):
  self.remote_conn.close()


def main():

 router_a=NetworkDevice('184.105.247.70','pyclass','88newclass')
 router_a.connect_to_device()
 router_a.login() 
 router_a.sendcommand("show ip int brief")
 router_a.sendcommand("terminal length 0")
 router_a.sendcommand("show hardware")
 router_a.closeconn() 

 router_b=NetworkDevice('184.105.247.71','pyclass','88newclass')
 router_b.connect_to_device()
 router_b.login()
 router_b.sendcommand("show ip int brief")
 router_b.closeconn()

if __name__ == "__main__":
   main()



