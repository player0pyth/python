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

 pynet_rtr2 = ConnectHandler(**pynetrtr2)
 pynet_rtr2.config_mode()
 print pynet_rtr2.find_prompt()
 pynet_rtr2.send_command('logging buffered 10117')
 pynet_rtr2.exit_config_mode()
 print pynet_rtr2.send_command('show run | i logging')
 print pynet_rtr2.find_prompt()



if __name__ == '__main__':
   main()
