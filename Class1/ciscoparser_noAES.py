from ciscoconfparse import CiscoConfParse

cisco_cfg=CiscoConfParse("cisco_config_test.cfg")

crypto_pfs = cisco_cfg.find_objects_wo_child(parentspec=r"^crypto map CRYPTO", childspec=r"AES")

for i in crypto_pfs:
 print i.text
 for a in i.children:
  print a.text












