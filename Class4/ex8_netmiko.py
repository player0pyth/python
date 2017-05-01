#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass
from test_device import pynet1, pynet2, juniper_srx
import time




def main():

 password = getpass()

 for a_dict in (pynet1, pynet2, juniper_srx):
      
    a_dict['password'] = password
    a_dict['verbose'] = False

 for a_device in (pynet1, pynet2):
    net_connect = ConnectHandler(**a_device)
    net_connect.send_config_from_file(config_file='config_file.txt') 
    output = net_connect.send_command("show run | inc logging")
    print 
    print '#' * 80
    print "Device: {}:{}".format(net_connect.ip, net_connect.port)
    print output
    print '#' * 80
    print



if __name__ == '__main__':
   main()
