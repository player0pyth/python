import snmp_helper
import json


def main():

    IP = '184.105.247.70'
    a_user = 'pysnmp'
    auth_key = 'galileo1'
    encrypt_key = 'galileo1'
    snmp_user = (a_user, auth_key, encrypt_key)
    pynet_rtr1 = (IP, 161)
    pynet_rtr2 = (IP, 161)


    oidlist = {'ccmHistoryRunningLastChanged': '1.3.6.1.4.1.9.9.43.1.1.1.0', 'ccmHistoryRunningLastSaved':'1.3.6.1.4.1.9.9.43.1.1.2.0', 'ccmHistoryStartupLastChanged':'1.3.6.1.4.1.9.9.43.1.1.3.0'}

    
    for key,value in oidlist.iteritems():
     snmp_data = snmp_helper.snmp_get_oid_v3(pynet_rtr1, snmp_user, value)
     output = snmp_helper.snmp_extract(snmp_data)
     print key, output
     oidstatus[key] = output


if __name__ == "__main__":
 main()



