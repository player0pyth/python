from ciscoconfparse import CiscoConfParse

cisco_cfg=CiscoConfParse("cisco_config_test.cfg")

crypto = cisco_cfg.find_objects(r"^crypto map CRYPTO")

for i in crypto:
 print i.text
 for a in i.children:
  print a.text












