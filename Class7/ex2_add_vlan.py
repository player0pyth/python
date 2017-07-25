#!/usr/bin/env python


from pprint import pprint
import pyeapi
import argparse

def pyeapi_result(output):
    #return the result value from the pyeapi output
 return output[0]['result']

def check_vlan_f(eapi_conn, vlan_id):

 cmd = 'show vlan id {}'.format(vlan_id)
 print 'here'
 try: 
  response = eapi_conn.enable(cmd)
  check_vlan = pyeapi_result(response)['vlans']
  print check_vlan 
  print check_vlan[vlan_id]['name']
  return check_vlan[vlan_id]['name']
 except (pyeapi.eapilib.CommandError, KeyError):
        pass

 return False


def main():
   # use eapit to obtain 'show interface' from the switch
 parser = argparse.ArgumentParser(description='This is a python script to add vlans on aritsta switch')
 

 parser.add_argument("vlan_id", help="Vlan number to create or remove", action="store", type=str)
 
 parser.add_argument("-n", help="Specify Vlan name", action="store", dest="vlan_name", type=str)

 parser.add_argument("-r", help="Remove the given VLAN ID", action="store_true")



 parser.add_argument('-ver', action='version', version='%(prog)s 1.0')
 results = parser.parse_args()

 eapi_conn = pyeapi.connect_to('pynet-sw1')

 check_vlan_e = check_vlan_f(eapi_conn, results.vlan_id) 

 if results:
  if results.r:   
     showi = eapi_conn.config("no vlan "+results.vlan_id)
     pprint(showi)
  elif  check_vlan_e:
     print "VLAN exists, removing it"
     showi = eapi_conn.config("no vlan "+results.vlan_id)
     pprint(showi)
  else:
   print "VLAN doesnt exists"  
   cmds=[]
   cmds.append('vlan '+results.vlan_id) 
   cmds.append('name '+results.vlan_name)
   print cmds
   showi = eapi_conn.config(cmds)
   pprint(showi)

 

if __name__ == '__main__':
    main()
 







