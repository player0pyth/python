#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass
import time






pynetrtr1  = {
 'device_type': 'cisco_ios',
 'ip' : '184.105.247.70',
 'username' : 'pyclass',
 'password' : '88newclass',
 'port': 22
} 


pynetrtr2  = {
 'device_type': 'cisco_ios',
 'ip' : '184.105.247.71',
 'username' : 'pyclass',
 'password' : '88newclass',
 'port': 22
} 

pynet_jnpr_srx1 = {
 'device_type': 'juniper',
 'ip' : '184.105.247.76',
 'username' : 'pyclass',
 'password' : '88newclass',
 'port': 22


}



def main():

 
 pynet_rtr1 = ConnectHandler(**pynetrtr1)
 print pynet_rtr1.find_prompt()
 print pynet_rtr1.send_command('show arp')

 pynet_rtr2 = ConnectHandler(**pynetrtr2)
 print pynet_rtr2.find_prompt()
 print pynet_rtr2.send_command('show arp')

 pynet_jnprsrx1 = ConnectHandler(**pynet_jnpr_srx1)
 print pynet_jnprsrx1.find_prompt()
 print pynet_jnprsrx1.send_command('show arp')

if __name__ == '__main__':
   main()
