import re
import os
import yaml
from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime
from pprint import pprint

#2a)
#Create a list where each of the list elements is a dictionary 
#representing one of the network devices in the lab. 
#Do this for at least four of the lab devices. 
#The dictionary should have keys corresponding 
#to the device_name, host (i.e. FQDN), username, 
#and password. Use a fictional username/password 
#to avoid checking the lab password into GitHub.

cisco3 = {"device_name": "cisco3", "host": "cisco3.lasthop.io"}
cisco4 = {"device_name": "cisco4", "host": "cisco4.lasthop.io"}
arista1 = {"device_name": "arista1", "host": "arista1.lasthop.io"}
arista2 = {"device_name": "arista2", "host": "arista2.lasthop.io"}
arista3 = {"device_name": "arista3", "host": "arista3.lasthop.io"}
arista4 = {"device_name": "arista4", "host": "arista4.lasthop.io"}
srx2 = {"device_name": "srx2", "host": "srx2.lasthop.io"}
nxos1  = {"device_name": "nxos1", "host": "nxos1.lasthop.io"}
nxos2 = {"device_name": "nxos2", "host": "nxos2.lasthop.io"}

lab_devices = [cisco3, cisco4, arista1, arista2, arista3, arista4, srx2, nxos1, nxos2]

for device in lab_devices:
	device["username"] = "username"
	device["password"] = "pass123"

print("#" * 20)
pprint(lab_devices)
print("#" * 20)


#2b. Write the data structure you created in part 2a out to a YAML file. 
#Use expanded YAML format. How could you re-use this YAML file later when 
#creating Netmiko connections to devices?

with open("lab_devices.yml", "w") as file:
	yaml.dump(lab_devices, file, default_flow_style=False)

