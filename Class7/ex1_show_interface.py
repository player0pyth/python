#!/usr/bin/env python


import pyeapi
from pprint import pprint


def pyeapi_result(output):
    #return the result value from the pyeapi output
 return output[0]['result']
   


def main():
   # use eapit to obtain 'show interface' from the switch
 eapi_conn = pyeapi.connect_to('pynet-sw1')
 showi = eapi_conn.enable('show interfaces')
 interfaces = pyeapi_result(showi) 
 interfaces = interfaces['interfaces']

 data_stats={}

 for int_key,int_value in interfaces.items():
     int_counters = int_value.get('interfaceCounters',{})
     data_stats[int_key] = (int_counters.get('inOctets'), int_counters.get('outOctets'))

 pprint(data_stats)

 print "\n{:20} {:<20} {:<20}".format("Interface:", "inOctets", "outOctets")
 for intf, octets in sorted(data_stats.items()):
  print "{:20} {:<20} {:<20}".format(intf, octets[0], octets[1])
 print

if __name__ == '__main__':
    main()
 







