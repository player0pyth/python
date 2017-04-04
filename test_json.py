import json


my_list=list()
my_list=range(9)
my_list.append({})
my_list[-1]['ip']= '192.168.1.1'
my_list[-1]['iap']='10.10.10.10'


for i in my_list:
 print "before json",i

json.dumps(my_list)

with open("some_json_file_1.json", "w" ) as f:
 json.dump(my_list,f)

print "json file has been saved"

with open("some_json_file.json") as f:
   new_list = json.load(f)

for i in new_list:
 print "after json",i




