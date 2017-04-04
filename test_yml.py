import yaml


my_list=list()
my_list=range(9)
my_list.append({})
my_list[-1]['ip']= '192.168.1.1'
my_list[-1]['iap']='10.10.10.10'


for i in my_list:
 print "before yml",i

yaml.dump(my_list)

with open("some_yaml_file_1.yml", "w" ) as f:
 f.write(yaml.dump(my_list, default_flow_style=False))

print "yamal file has been saved"

with open("some_yaml_file.yml") as f:
   new_list = yaml.load(f)

for i in new_list:
 print "after yml",i




